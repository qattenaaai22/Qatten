# -*- coding: utf-8 -*-
import multiprocessing
import os
import time
from datetime import datetime


def subprocess(seed, map_name, config):
    os.system('python src/main.py --config={} --env-config=sc2 with env_args.map_name={} env_args.seed={} '
              '> out_{}_{}.log 2>&1 &'
              .format(config, map_name, seed, map_name, seed))
    # print('python src/main.py --config={} --env-config=sc2 with env_args.map_name={} env_args.seed={} '
    #       '> out_{}_{}.log 2>&1 &'
    #       .format(config, map_name, seed, map_name, seed))
    # print('sleep 3s')


def mainprocess():
    pool = multiprocessing.Pool(3)  # run 3 process at the same time

    for i in range(0, 3):
        pool.apply_async(subprocess, args=(i, '5m_vs_6m', 'qatten', ))
        time.sleep(3)
    pool.close()
    pool.join()


if __name__ == '__main__':
    # 主函数
    mainprocess()
