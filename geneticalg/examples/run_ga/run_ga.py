import pandas as pd
import geneticalg


allvts = pd.read_csv("./data/video_ts_data.csv", index_col=None)
maxduration = 120

video_lengths = pd.read_csv("./data/video_lengths.csv").iloc[:, 0].values
video_list = pd.read_csv("./data/video_list.csv", index_col=None).iloc[:, 0].values

chrom = geneticalg.gen_chrom(maxduration, video_list, video_lengths)

geneticalg.calc_duration(chrom, video_lengths)

chrom
