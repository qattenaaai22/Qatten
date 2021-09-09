#!/usr/bin/env bash
bash run.sh 0 python3 src/main.py --config=qatten --env-config=sc2 with env_args.map_name=2s3z env_args.seed=0 > out_2s3z_0.log 2>&1 &
sleep 3s
bash run.sh 0 python3 src/main.py --config=qatten --env-config=sc2 with env_args.map_name=2s3z env_args.seed=1 > out_2s3z_1.log 2>&1 &
sleep 3s
bash run.sh 0 python3 src/main.py --config=qatten --env-config=sc2 with env_args.map_name=2s3z env_args.seed=2 > out_2s3z_2.log 2>&1 &
sleep 3s
bash run.sh 1 python3 src/main.py --config=qatten --env-config=sc2 with env_args.map_name=2s3z env_args.seed=3 > out_2s3z_3.log 2>&1 &
sleep 3s
bash run.sh 1 python3 src/main.py --config=qatten --env-config=sc2 with env_args.map_name=2s3z env_args.seed=4 > out_2s3z_4.log 2>&1 &
sleep 3s
bash run.sh 1 python3 src/main.py --config=qatten --env-config=sc2 with env_args.map_name=2s3z env_args.seed=5 > out_2s3z_5.log 2>&1 &

