import json
from operator import sub
import numpy as np
import matplotlib.pyplot as plt
import random
import matplotlib.patches as mpatches

def load_data(data):
    # data = {
    #     "machines": self.n_human+self.n_robot,
    #     "jobs": self.product.n_job,
    #     "xlabel": "time",
    #     "title": "gantt",
    #     "packages": custom_packages
    # }
    # custom_packages = [
        #     {"start_low":0, "start": 0.0, "start_up":0, "end_low":1, "end": 1, "end_up":1, "machine": 5, "job": 8},
        #     {"start_low":0, "start": 0.0, "start_up":0, "end_low":4, "end": 4, "end_up":4, "machine": 2, "job": 1},
        # ]
    packages = []
    machine = [pkg['machine'] for pkg in data['packages']]
    job = [pkg['job'] for pkg in data['packages']]
    title = data.get('title', 'Gantt for JSP')
    xticks = data.get('xticks', "")
    machines = data.get('machines', 100)
    labels = [pkg['machine'] for pkg in data['packages']]
    def custom_sort(s):
        if "Human" in s:
            return (0, int(s[-1]))
        elif "Robot" in s:
            return (1, int(s[-1]))

    labels = sorted(set(labels), key=custom_sort)

    jobs = data.get('jobs', 100)
    operations = [0] * jobs

    for pkg in data['packages']:
        packages.append({
            'start_low': pkg['start_low'],
            'start': pkg['start'],
            'start_up': pkg['start_up'],
            'end_low': pkg['end_low'],
            'end': pkg['end'],
            'end_up': pkg['end_up'],
            'machine': pkg['machine'],
            'job': pkg['job'],
            'operation': operations[pkg['job']-1] 
        })
        operations[pkg['job']-1] += 1 

    return packages, machine, job, title, xticks, labels, machines, jobs

def process_data(packages, machines):
    start = [pkg['start'] for pkg in packages]
    end = [pkg['end'] for pkg in packages]
    start_low = [pkg['start_low'] for pkg in packages]
    end_low = [pkg['end_low'] for pkg in packages]
    start_up = [pkg['start_up'] for pkg in packages]
    end_up = [pkg['end_up'] for pkg in packages]
    durations = list(map(sub, end, start))
    ypos = np.arange(machines, 0, -1)

    return start_low, start, start_up, end_low, end, end_up, durations, ypos

def random_color():
    red = random.randint(150, 255)
    green = random.randint(150, 255)
    blue = random.randint(150, 255)
    return "#{:02X}{:02X}{:02X}".format(red, green, blue)

def render_gantt(packages, machines, start_low, start, start_up, end_low, end, end_up, ypos, job, jobs, xticks, labels):
    def on_hover(event): 
        for i, rect in enumerate(rectangles):
            if rect.contains(event)[0]:
                rect.set_height(0.6)  
                rect.set_edgecolor('black')  
                rect.set_linewidth(2)  
            else:
                
                original_prop = original_properties[i]
                rect.set_height(original_prop['height'])  
                rect.set_edgecolor(original_prop['edgecolor'])  
                rect.set_linewidth(original_prop['linewidth'])  
        plt.draw()

    fig, ax = plt.subplots()
    ax.yaxis.grid(False)
    ax.xaxis.grid(True)

    rectangles = []
    text = ax.text(0.5, 1.05, '', transform=ax.transAxes, ha='center', va='center', color='black', fontsize=12)

    job_colors = [random_color() for _ in range(jobs)]
    colors = [job_colors[pkg['job']-1] for pkg in packages]

    for i, pkg in enumerate(packages):
        machine = pkg['machine']
        n_human = len({pkg['machine'] for pkg in packages if "Human" in pkg['machine']})
        if "Human" in machine:
            order = int(machine[-1])-1
        else:
            order = int(machine[-1])+n_human-1
        rect = mpatches.Rectangle((start[i], machines - order - 0.25),
                                  end[i] - start[i], 0.4, facecolor=colors[i], edgecolor='blue', linestyle='dashed')
        rectangles.append(rect)
        plt.gca().add_patch(rect)

        rect_low = mpatches.Rectangle((start_low[i], machines - order - 0.25),
                                  end_up[i] - start_low[i], 0.5, facecolor="white", edgecolor='red', linestyle='dashed')
        rect_low.set_alpha(0.5)
        rectangles.append(rect_low)
        plt.gca().add_patch(rect_low)

        rect_up = mpatches.Rectangle((start_up[i], machines - order - 0.25),
                                  end_up[i] - start_up[i], 0.3, facecolor="white", edgecolor='green', linestyle='dashed')
        rect_up.set_alpha(0.5)
        rectangles.append(rect_up)
        plt.gca().add_patch(rect_up)

    plt.rc('font', family='serif', size=15)
    job_i = 0
    for i, rect in enumerate(rectangles):
        rect_height = rect.get_height()
        if rect_height != 0.4:
            continue
        x_center = rect.get_x() + rect.get_width() / 2
        y_center = rect.get_y() + rect.get_height() / 2
        plt.text(x_center, y_center, str(job[job_i]), ha='center', va='center')
        job_i += 1

    plt.tick_params(axis='both', which='both', bottom='on', top='off', left='off', right='off')
    plt.xlim(0, max(end_up))
    plt.ylim(0.5, machines + 0.5)
    plt.yticks(ypos, labels)
    original_properties = []
    for i, rect in enumerate(rectangles):
        original_properties.append({
            'height': rect.get_height(),
            'edgecolor': rect.get_edgecolor(),
            'linewidth': rect.get_linewidth()
        })
    fig.canvas.mpl_connect('motion_notify_event', on_hover)

    if xticks:
        plt.xticks(xticks, map(str, xticks))

def show_plot():
    plt.show()


def gantt_HRC(data):
    packages, machine, job, title, xticks, labels, machines, jobs = load_data(data)
    start_low, start, start_up, end_low, end, end_up, durations, ypos = process_data(packages, machines)
    render_gantt(packages, machines, start_low, start, start_up, end_low, end, end_up, ypos, job, jobs, xticks, labels)
    show_plot()
    # save_plot(title, 'gantt.png')
