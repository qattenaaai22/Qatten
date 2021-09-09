#!/usr/bin/env bash
bash run.sh 0 python3 src/main.py --config=qlinear --env-config=sc2 with env_args.map_name=5m_vs_6m env_args.seed=0 > out_5m_vs_6m_0.log 2>&1 &
sleep 3s
bash run.sh 0 python3 src/main.py --config=qlinear --env-config=sc2 with env_args.map_name=5m_vs_6m env_args.seed=1 > out_5m_vs_6m_1.log 2>&1 &
sleep 3s
bash run.sh 1 python3 src/main.py --config=qlinear --env-config=sc2 with env_args.map_name=5m_vs_6m env_args.seed=2 > out_5m_vs_6m_2.log 2>&1 &
sleep 3s
bash run.sh 1 python3 src/main.py --config=qlinear --env-config=sc2 with env_args.map_name=5m_vs_6m env_args.seed=3 > out_5m_vs_6m_3.log 2>&1 &
sleep 3s
bash run.sh 2 python3 src/main.py --config=qlinear --env-config=sc2 with env_args.map_name=5m_vs_6m env_args.seed=4 > out_5m_vs_6m_4.log 2>&1 &
sleep 3s
bash run.sh 2 python3 src/main.py --config=qlinear --env-config=sc2 with env_args.map_name=5m_vs_6m env_args.seed=5 > out_5m_vs_6m_5.log 2>&1 &

