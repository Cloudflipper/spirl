from gym.envs.registration import register

register(
    id='tensegrity_env-v0',  # 环境的唯一ID
    entry_point='d4rl.d4rl.tensegrity_env.tensegrity_env.envs:tensegrity_env',  # 自定义环境类的路径
)