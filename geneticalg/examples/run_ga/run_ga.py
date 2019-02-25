import pandas as pd

from ga import *

allvts = pd.read_csv("./data/video_ts_data.csv", index_col=None)
maxduration = 60

vidlenghts = pd.read_csv("./data/video_lengths.csv").iloc[:,0].values
video_list = pd.read_csv("./data/video_list.csv", index_col=None).iloc[:,0].values

gen_chrom(60)
