import pandas as pd
from geneticalg import gen_chrom, calc_duration


allvts = pd.read_csv("./data/video_ts_data.csv", index_col=None)

video_lengths = pd.read_csv("./data/video_lengths.csv").iloc[:, 0].values
video_list = pd.read_csv("./data/video_list.csv", index_col=None).iloc[:, 0].values

# Define Variables
max_seconds = 120 * 60
numAttempts = 10
numGenerations = 20
popSize = 20


# Generate Empty Chromosomes
chromosomes = []

for i in range(popSize):
    chromosomes.append(gen_chrom(max_seconds, video_list, video_lengths))

for chrom in chromosomes:
    print(calc_duration(chrom, video_lengths))
