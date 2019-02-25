#!/usr/bin/python


import numpy as np


def gen_chrom(maxduration, video_list, video_lengths):
    num_mins = 10000
    while num_mins > maxduration:
        chrom = np.random.choice([0, 1], size=(len(video_list),)
        , p=[4./5, 1./5])
        num_mins = sum(chrom*video_lengths)
    return chrom


def calc_duration(chrom, video_lengths):
    return sum(chrom*video_lengths)
