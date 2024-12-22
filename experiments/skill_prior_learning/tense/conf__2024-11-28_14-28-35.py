import os
import gym
from spirl.models.bc_mdl import BCMdl
from spirl.components.logger import Logger
from spirl.utils.general_utils import AttrDict
from spirl.configs.default_data_configs.tense import data_spec
from spirl.components.evaluator import DummyEvaluator
from gym.envs.registration import register
import tensegrity_env.tensegrity_env.envs.tensegrity_env as t_env

# import importlib
# importlib.import_module('tensegrity_env.tensegrity_env.envs.tensegrity_env')
current_dir = os.path.dirname(os.path.realpath(__file__))


configuration = {
    'model': BCMdl,
    'logger': Logger,
    'data_dir': '.',
    'epoch_cycles_train': 10,
    'evaluator': DummyEvaluator,
}
configuration = AttrDict(configuration)

env_id = 'tensegrity_env-v0'

if env_id in gym.envs.registry.env_specs:
    print(f"Environment {env_id} is registered.")
else:
    register(
     id='tensegrity_env-v0',
     entry_point='t_env',  # 检查路径拼写
    )


model_config = AttrDict(
    state_dim=data_spec.state_dim,
    action_dim=data_spec.n_actions,
)

# Dataset
data_config = AttrDict()
data_config.dataset_spec = data_spec
data_config.dataset_spec.subseq_len = 1 + 1  # flat last action from seq gets cropped