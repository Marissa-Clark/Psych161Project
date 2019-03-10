import pandas as pd
from geneticalg import (gen_chromosome,
                        calc_fitness_all,
                        mutate,
                        crossover,
                        list_duplicates,
                        del_duplicates,
                        sort_chromosomes)

video_data = pd.read_csv("./data/video_ts_data.csv", index_col=None)
video_lengths = pd.read_csv("./data/video_lengths.csv").iloc[:, 0].values
video_list = pd.read_csv("./data/video_list.csv", index_col=None).iloc[:, 0].values

# Define Variables
max_seconds = 120 * 60
max_attempts = 10
num_generations = 20
popSize = 20

# Generate Empty Chromosomes
chromosomes = []
max_chromosome = []

for i in range(popSize):
    chromosomes.append(gen_chromosome(max_seconds, video_lengths))


for gen in range(num_generations):
    for child in crossover(chromosomes[0], chromosomes[1], max_attempts, video_lengths, max_seconds):
        chromosomes.append(child)
    chromosomes.append(mutate(chromosomes[0], max_attempts, video_lengths, max_seconds))

    chromosomes = del_duplicates(chromosomes, video_list, video_data)
    chromosomes = sort_chromosomes(chromosomes, video_list, video_data)
    chromosomes = chromosomes[0: 20]
    max_chromosome.append(chromosomes[0])


calc_fitness_all(max_chromosome, video_list, video_data)
