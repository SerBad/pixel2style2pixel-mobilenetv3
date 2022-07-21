"""
This file runs the main training/val loop
"""
import os
import json
import sys
import pprint

sys.path.append(".")
sys.path.append("..")
os.chdir('../')
print(os.getcwd())
from options.train_options import TrainOptions
from training.coach import Coach
import shutil

def main():
    opts = TrainOptions().parse()
    opts.dataset_type = "ffhq_encode"
    opts.exp_dir = "./output"
    opts.workers = 8
    opts.atch_size = 8
    opts.test_batch_size = 8
    opts.test_workers = 8
    opts.val_interval = 2500
    opts.save_interval = 5000
    opts.encoder_type = "MobileGradualStyleEncoder"
    opts.start_from_latent_avg = True
    opts.lpips_lambda = 0.8
    opts.l2_lambda = 1
    opts.id_lambda = 0.1
    if os.path.exists(opts.exp_dir):
        shutil.rmtree(opts.exp_dir)

    os.makedirs(opts.exp_dir)

    opts_dict = vars(opts)
    pprint.pprint(opts_dict)
    with open(os.path.join(opts.exp_dir, 'opt.json'), 'w') as f:
        json.dump(opts_dict, f, indent=4, sort_keys=True)

    coach = Coach(opts)
    coach.train()


if __name__ == '__main__':
    main()
