import numpy as np
import pandas as pd
from numpy import linalg
import random
from random import randint

def gen_chrom(maxduration):
    num_mins = 1000
    while num_mins > maxduration:
        chrom  = np.random.choice([0, 1], size=(len(video_list),), p=[4./5, 1./5])
        num_mins = sum(chrom*vidlenghts) / 60
    return chrom

def calc_duration(chrom):
    return sum(chrom*vidlenghts) / 60
