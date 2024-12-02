import torch
from rl4co.envs import HRCEnv
from rl4co.models.zoo.l2d import L2DModel
from rl4co.models.zoo.l2d.policy import L2DPolicy
from rl4co.models.zoo.l2d.decoder import L2DDecoder
from rl4co.models.nn.graph.hgnn import HetGNNEncoder
from rl4co.utils.trainer import RL4COTrainer

if torch.cuda.is_available():
    accelerator = "gpu"
    batch_size = 256
    train_data_size = 2_000
    embed_dim = 128
    num_encoder_layers = 4
else:
    print("No GPU, exit!")
    exit()

params_H1R1 = {
  "num_jobs": 15, 
  "num_humans": 1, 
  "num_robots": 1, 
  "min_ops_per_job": 1,  
  "max_ops_per_job": 3,  
  "min_processing_time": 8, 
  "max_processing_time": 233,  
  "min_eligible_oper_per_op": 1, 
  "max_eligible_oper_per_op": 2, 
}

params_H2R2 = {
  "num_jobs": 15, 
  "num_humans": 2, 
  "num_robots": 2, 
  "min_ops_per_job": 1,  
  "max_ops_per_job": 3,  
  "min_processing_time": 8, 
  "max_processing_time": 233,  
  "min_eligible_oper_per_op": 1, 
  "max_eligible_oper_per_op": 4, 
}

params_H2R4 = {
  "num_jobs": 15, 
  "num_humans": 2, 
  "num_robots": 4, 
  "min_ops_per_job": 1,  
  "max_ops_per_job": 3,  
  "min_processing_time": 8, 
  "max_processing_time": 233,  
  "min_eligible_oper_per_op": 1, 
  "max_eligible_oper_per_op": 6, 
}

params_H3R1 = {
  "num_jobs": 15, 
  "num_humans": 3, 
  "num_robots": 1, 
  "min_ops_per_job": 1,  
  "max_ops_per_job": 3,  
  "min_processing_time": 8, 
  "max_processing_time": 233,  
  "min_eligible_oper_per_op": 1, 
  "max_eligible_oper_per_op": 4, 
}

params_H3R3 = {
  "num_jobs": 15, 
  "num_humans": 3, 
  "num_robots": 3, 
  "min_ops_per_job": 1,  
  "max_ops_per_job": 3,  
  "min_processing_time": 8, 
  "max_processing_time": 233,  
  "min_eligible_oper_per_op": 1, 
  "max_eligible_oper_per_op": 6, 
}

params_H4R1 = {
  "num_jobs": 15, 
  "num_humans": 4, 
  "num_robots": 1, 
  "min_ops_per_job": 1,  
  "max_ops_per_job": 3,  
  "min_processing_time": 8, 
  "max_processing_time": 233,  
  "min_eligible_oper_per_op": 1, 
  "max_eligible_oper_per_op": 5, 
}

params_H4R2 = {
  "num_jobs": 15, 
  "num_humans": 4, 
  "num_robots": 2, 
  "min_ops_per_job": 1,  
  "max_ops_per_job": 3,  
  "min_processing_time": 8, 
  "max_processing_time": 233,  
  "min_eligible_oper_per_op": 1, 
  "max_eligible_oper_per_op": 6, 
}

params_H5R1 = {
  "num_jobs": 15, 
  "num_humans": 5, 
  "num_robots": 1, 
  "min_ops_per_job": 1,  
  "max_ops_per_job": 3,  
  "min_processing_time": 8, 
  "max_processing_time": 233,  
  "min_eligible_oper_per_op": 1, 
  "max_eligible_oper_per_op": 6, 
}

params_H5R2 = {
  "num_jobs": 15, 
  "num_humans": 5, 
  "num_robots": 2, 
  "min_ops_per_job": 1,  
  "max_ops_per_job": 3,  
  "min_processing_time": 8, 
  "max_processing_time": 233,  
  "min_eligible_oper_per_op": 1, 
  "max_eligible_oper_per_op": 7, 
}

# H1R1
env = HRCEnv(generator_params=params_H1R1)
td = env.reset(batch_size=[10])
encoder = HetGNNEncoder(embed_dim=32, num_layers=2, env_name = env.name)
decoder = L2DDecoder(env_name=env.name, embed_dim=32)
policy = L2DPolicy(embed_dim=embed_dim, num_encoder_layers=num_encoder_layers, env_name=env.name, encoder=encoder, decoder=decoder)
model_H1R1 = L2DModel(env,
                 policy=policy, 
                 baseline="rollout",
                 batch_size=batch_size,
                 train_data_size=train_data_size,
                 val_data_size=1_000,
                 optimizer_kwargs={"lr": 2e-5})

trainer = RL4COTrainer(
    max_epochs=2000,
    accelerator=accelerator,
    devices=1,
    logger=None,
)
trainer.fit(model_H1R1)
torch.save(model_H1R1, 'L2DModel_{}.pth'.format("H1R1"))

# H2R2
env = HRCEnv(generator_params=params_H2R2)
td = env.reset(batch_size=[10])
encoder = HetGNNEncoder(embed_dim=32, num_layers=2, env_name = env.name)
decoder = L2DDecoder(env_name=env.name, embed_dim=32)
policy = L2DPolicy(embed_dim=embed_dim, num_encoder_layers=num_encoder_layers, env_name=env.name, encoder=encoder, decoder=decoder)
model_H2R2 = L2DModel(env,
                 policy=policy, 
                 baseline="rollout",
                 batch_size=batch_size,
                 train_data_size=train_data_size,
                 val_data_size=1_000,
                 optimizer_kwargs={"lr": 2e-5})
trainer = RL4COTrainer(
    max_epochs=2000,
    accelerator=accelerator,
    devices=1,
    logger=None,
)
trainer.fit(model_H2R2)
torch.save(model_H2R2, 'L2DModel_{}.pth'.format("H2R2"))

# H2R4
env = HRCEnv(generator_params=params_H2R4)
td = env.reset(batch_size=[10])
encoder = HetGNNEncoder(embed_dim=32, num_layers=2, env_name = env.name)
decoder = L2DDecoder(env_name=env.name, embed_dim=32)
policy = L2DPolicy(embed_dim=embed_dim, num_encoder_layers=num_encoder_layers, env_name=env.name, encoder=encoder, decoder=decoder)
model_H2R4 = L2DModel(env,
                 policy=policy, 
                 baseline="rollout",
                 batch_size=batch_size,
                 train_data_size=train_data_size,
                 val_data_size=1_000,
                 optimizer_kwargs={"lr": 2e-5})
trainer = RL4COTrainer(
    max_epochs=2000,
    accelerator=accelerator,
    devices=1,
    logger=None,
)
trainer.fit(model_H2R4)
torch.save(model_H2R4, 'L2DModel_{}.pth'.format("H2R4"))

# H3R3
env = HRCEnv(generator_params=params_H3R3)
td = env.reset(batch_size=[10])
encoder = HetGNNEncoder(embed_dim=32, num_layers=2, env_name = env.name)
decoder = L2DDecoder(env_name=env.name, embed_dim=32)
policy = L2DPolicy(embed_dim=embed_dim, num_encoder_layers=num_encoder_layers, env_name=env.name, encoder=encoder, decoder=decoder)
model_H3R3 = L2DModel(env,
                 policy=policy, 
                 baseline="rollout",
                 batch_size=batch_size,
                 train_data_size=train_data_size,
                 val_data_size=1_000,
                 optimizer_kwargs={"lr": 2e-5})
trainer = RL4COTrainer(
    max_epochs=2000,
    accelerator=accelerator,
    devices=1,
    logger=None,
)
trainer.fit(model_H3R3)
torch.save(model_H3R3, 'L2DModel_{}.pth'.format("H3R3"))

# H4R2
env = HRCEnv(generator_params=params_H4R2)
td = env.reset(batch_size=[10])
encoder = HetGNNEncoder(embed_dim=32, num_layers=2, env_name = env.name)
decoder = L2DDecoder(env_name=env.name, embed_dim=32)
policy = L2DPolicy(embed_dim=embed_dim, num_encoder_layers=num_encoder_layers, env_name=env.name, encoder=encoder, decoder=decoder)
model_H4R2 = L2DModel(env,
                 policy=policy, 
                 baseline="rollout",
                 batch_size=batch_size,
                 train_data_size=train_data_size,
                 val_data_size=1_000,
                 optimizer_kwargs={"lr": 2e-5})
trainer = RL4COTrainer(
    max_epochs=2000,
    accelerator=accelerator,
    devices=1,
    logger=None,
)
trainer.fit(model_H4R2)
torch.save(model_H4R2, 'L2DModel_{}.pth'.format("H4R2"))