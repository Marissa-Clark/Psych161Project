#!/usr/bin/python


import numpy as np


def gen_chrom(max_seconds, video_list, video_lengths):
    num_seconds = 100000000
    while num_seconds > max_seconds:
        chrom = np.random.choice([0, 1], size=(len(video_list),),
                                 p=[4./5, 1./5])
        num_seconds = sum(chrom*video_lengths)
    return chrom


def calc_duration(chrom, video_lengths):
    return sum(chrom*video_lengths) / 60
