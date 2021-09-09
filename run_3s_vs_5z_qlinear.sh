#!/usr/bin/env bash
bash run.sh 0 python3 src/main.py --config=qlinear --env-config=sc2 with env_args.map_name=3s_vs_5z env_args.seed=0 > out_3s_vs_5z_0.log 2>&1 &
sleep 3s
bash run.sh 0 python3 src/main.py --config=qlinear --env-config=sc2 with env_args.map_name=3s_vs_5z env_args.seed=1 > out_3s_vs_5z_1.log 2>&1 &
sleep 3s
bash run.sh 1 python3 src/main.py --config=qlinear --env-config=sc2 with env_args.map_name=3s_vs_5z env_args.seed=2 > out_3s_vs_5z_2.log 2>&1 &
sleep 3s
bash run.sh 1 python3 src/main.py --config=qlinear --env-config=sc2 with env_args.map_name=3s_vs_5z env_args.seed=3 > out_3s_vs_5z_3.log 2>&1 &
sleep 3s
bash run.sh 2 python3 src/main.py --config=qlinear --env-config=sc2 with env_args.map_name=3s_vs_5z env_args.seed=4 > out_3s_vs_5z_4.log 2>&1 &
sleep 3s
bash run.sh 2 python3 src/main.py --config=qlinear --env-config=sc2 with env_args.map_name=3s_vs_5z env_args.seed=5 > out_3s_vs_5z_5.log 2>&1 &

