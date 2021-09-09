```
- Feb 7 2020 - Qatten beta. 
```

# Q-value Attention network (Qatten)

This is the source codes for paper "Qatten: A General Framework for Cooperative Multiagent Reinforcement
Learning". It is developed based on PyMARL framework for deep multi-agent reinforcement learning.
PyMARL is written in PyTorch and uses [SMAC](https://github.com/oxwhirl/smac) as its environment.

## Installation steps
1. Install SMAC environment (see https://github.com/oxwhirl/smac)
2. Install PyMARL framework (see https://github.com/oxwhirl/pymarl)
3. Install Nvidia Docker (see https://github.com/NVIDIA/nvidia-docker)
3. Build the Dockerfile using 
```shell
cd Qatten
cd docker
bash build.sh
```

Set up StarCraft II and SMAC maps--copy from pymarl:
```shell
cp -r YOURPATH/pymarl/3rdparty YOURPATH/Qatten
or install again
bash install_sc2.sh
```

## Run an experiment 

To run experiments using the Docker container:
```shell
bash run.sh $GPU python3 src/main.py --config=qatten --env-config=sc2 with env_args.map_name=2s3z
```

The config files act as defaults for an algorithm or environment. 

They are all located in `src/config`.
`--config` refers to the config files in `src/config/algs`
`--env-config` refers to the config files in `src/config/envs`

All results will be stored in the `Results` folder.

## Saving and loading learnt models

### Saving models

You can save the learnt models to disk by setting `save_model = True`, which is set to `False` by default. The frequency of saving models can be adjusted using `save_model_interval` configuration. Models will be saved in the result directory, under the folder called *models*. The directory corresponding each run will contain models saved throughout the experiment, each within a folder corresponding to the number of timesteps passed since starting the learning process.

### Loading models

Learnt models can be loaded using the `checkpoint_path` parameter, after which the learning will proceed from the corresponding timestep. 

## Watching StarCraft II replays

`save_replay` option allows saving replays of models which are loaded using `checkpoint_path`. Once the model is successfully loaded, `test_nepisode` number of episodes are run on the test mode and a .SC2Replay file is saved in the Replay directory of StarCraft II. Please make sure to use the episode runner if you wish to save a replay, i.e., `runner=episode`. The name of the saved replay file starts with the given `env_args.save_replay_prefix` (map_name if empty), followed by the current timestamp. 

The saved replays can be watched by double-clicking on them or using the following command:

```shell
python -m pysc2.bin.play --norender --rgb_minimap_size 0 --replay NAME.SC2Replay
```

**Note:** Replays cannot be watched using the Linux version of StarCraft II. Please use either the Mac or Windows version of the StarCraft II client.
