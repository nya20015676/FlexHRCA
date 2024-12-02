import collections

from ortools.sat.python import cp_model


class SolutionPrinter(cp_model.CpSolverSolutionCallback):
    """Print intermediate solutions."""

    def __init__(self) -> None:
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.__solution_count = 0

    def on_solution_callback(self) -> None:
        """Called at each new solution."""
        print(
            f"Solution {self.__solution_count}, time = {self.wall_time} s,"
            f" objective = {self.objective_value}"
        )
        self.__solution_count += 1

def flexhrc(jobs, num_humans, num_robots) -> None:
    """solve a small flexible jobshop problem."""
    # Data part.
    jobs = jobs
    # [  # task = (processing_time, machine_id)
    #     [  # Job 0
    #         [(3, 0), (1, 1), (5, 2)],  # task 0 with 3 alternatives
    #         [(2, 0), (4, 1), (6, 2)],  # task 1 with 3 alternatives
    #         [(2, 0), (3, 1), (1, 2)],  # task 2 with 3 alternatives
    #     ],
    #     [  # Job 1
    #         [(2, 0), (3, 1), (4, 2)],
    #         [(1, 0), (5, 1), (4, 2)],
    #         [(2, 0), (1, 1), (4, 2)],
    #     ],
    #     [  # Job 2
    #         [(2, 0), (1, 1), (4, 2)],
    #         [(2, 0), (3, 1), (4, 2)],
    #         [(3, 0), (1, 1), (5, 2)],
    #     ],
    # ]

    num_jobs = len(jobs)
    all_jobs = range(num_jobs)

    num_machines = num_humans + num_robots
    all_machines = range(num_machines)

    # Model the flexible jobshop problem.
    model = cp_model.CpModel()

    horizon = 0
    for job in jobs:
        for task in job:
            max_task_duration = 0
            for alternative in task:
                max_task_duration = max(max_task_duration, alternative[0])
            horizon += max_task_duration

    # print(f"Horizon = {horizon}")

    # Global storage of variables.
    intervals_per_resources = collections.defaultdict(list)
    starts = {}  # indexed by (job_id, task_id).
    presences = {}  # indexed by (job_id, task_id, alt_id).
    job_ends: list[cp_model.IntVar] = []

    # Scan the jobs and create the relevant variables and intervals.
    for job_id in all_jobs:
        job = jobs[job_id]
        num_tasks = len(job)
        previous_end = None
        for task_id in range(num_tasks):
            task = job[task_id]

            min_duration = task[0][0]
            max_duration = task[0][0]

            num_alternatives = len(task)
            all_alternatives = range(num_alternatives)

            for alt_id in range(1, num_alternatives):
                alt_duration = task[alt_id][0]
                min_duration = min(min_duration, alt_duration)
                max_duration = max(max_duration, alt_duration)

            # Create main interval for the task.
            suffix_name = f"_j{job_id}_t{task_id}"
            start = model.new_int_var(0, horizon, "start" + suffix_name)
            duration = model.new_int_var(
                min_duration, max_duration, "duration" + suffix_name
            )
            end = model.new_int_var(0, horizon, "end" + suffix_name)
            interval = model.new_interval_var(
                start, duration, end, "interval" + suffix_name
            )

            # Store the start for the solution.
            starts[(job_id, task_id)] = start

            # Add precedence with previous task in the same job.
            if previous_end is not None:
                model.add(start >= previous_end)
            previous_end = end

            # Create alternative intervals.
            if num_alternatives > 1:
                l_presences = []
                for alt_id in all_alternatives:
                    alt_suffix = f"_j{job_id}_t{task_id}_a{alt_id}"
                    l_presence = model.new_bool_var("presence" + alt_suffix)
                    l_start = model.new_int_var(0, horizon, "start" + alt_suffix)
                    l_duration = task[alt_id][0]
                    l_end = model.new_int_var(0, horizon, "end" + alt_suffix)
                    l_interval = model.new_optional_interval_var(
                        l_start, l_duration, l_end, l_presence, "interval" + alt_suffix
                    )
                    l_presences.append(l_presence)

                    # Link the primary/global variables with the local ones.
                    model.add(start == l_start).only_enforce_if(l_presence)
                    model.add(duration == l_duration).only_enforce_if(l_presence)
                    model.add(end == l_end).only_enforce_if(l_presence)

                    # Add the local interval to the right machine.
                    if (job_id+1)%5 == 0:
                        machine = task[alt_id][1]
                        h_idx = (machine - (num_humans + num_robots)) // num_robots
                        r_idx = (machine - (num_humans + num_robots)) % num_robots + num_humans
                        intervals_per_resources[h_idx].append(l_interval)
                        intervals_per_resources[r_idx].append(l_interval)
                    else:
                        intervals_per_resources[task[alt_id][1]].append(l_interval)

                    # Store the presences for the solution.
                    presences[(job_id, task_id, alt_id)] = l_presence

                # Select exactly one presence variable.
                model.add_exactly_one(l_presences)
            else:
                intervals_per_resources[task[0][1]].append(interval)
                presences[(job_id, task_id, 0)] = model.new_constant(1)

        if previous_end is not None:
            job_ends.append(previous_end)

    # Create machines constraints.
    for machine_id in all_machines:
        intervals = intervals_per_resources[machine_id]
        if len(intervals) > 1:
            model.add_no_overlap(intervals)

    # Makespan objective
    makespan = model.new_int_var(0, horizon, "makespan")
    model.add_max_equality(makespan, job_ends)
    model.minimize(makespan)

    # Solve model.
    solver = cp_model.CpSolver()
    solution_printer = SolutionPrinter()
    status = solver.solve(model)

    # 假设以下变量已经定义
    # status: 求解状态
    # solver: 包含求解结果的对象
    # all_jobs: 所有作业的列表
    # jobs: 每个作业的任务及其替代选择的列表
    # starts: 任务的开始时间变量
    # presences: 任务的替代选择变量

    scheduling_data = {}

    if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        # print(f"Optimal objective value: {solver.objective_value}")
        for job_id in all_jobs:
            # 为每个作业创建一个空列表来存储任务信息
            scheduling_data[f'Job {job_id}'] = []
            # print(f"Job {job_id}")
            for task_id, task in enumerate(jobs[job_id]):
                start_value = solver.value(starts[(job_id, task_id)])
                machine: int = -1
                task_duration: int = -1
                selected: int = -1
                for alt_id, alt in enumerate(task):
                    if solver.boolean_value(presences[(job_id, task_id, alt_id)]):
                        task_duration, machine = alt
                        selected = alt_id
                # 将任务信息以元组形式添加到调度数据中
                scheduling_data[f'Job {job_id}'].append((f'task_{job_id}_{task_id}', start_value, machine))
                # print(
                #     f"  task_{job_id}_{task_id} starts at {start_value} (alt"
                #     f" {selected}, machine {machine}, duration {task_duration})"
                # )

    # print(solver.response_stats())
    return solver.objective_value, scheduling_data