#!/usr/bin/python
import numpy as np
from numpy import linalg
import random


def gen_chromosome(max_seconds, video_list, video_lengths):
    """Generate a dummy-coded chromosome whose total time is less than the max
    time listed

    Parameters
    ----------
    max_seconds : int
        Maximum number of seconds for video combinations.
    video_list : np.ndarray
        List of all video titles (in this case number identifiers)
    video_lengths : np.ndarray
        Lengths of each invidual video, in seconds

    Returns
    -------
    np.ndarray
        Returns a dummy coded "chromosome" of a set of videos
        under the maximum number of seconds (our scan time limit)

    """
    num_seconds = 100000000
    while num_seconds > max_seconds:
        chrom = np.random.choice([0, 1], size=(len(video_list),),
                                 p=[4./5, 1./5])
        num_seconds = sum(chrom*video_lengths)
    return chrom


def calc_duration(chromosome, video_lengths):
    """Calculates the duration of the set of videos when combined
    Parameters
    ----------
    chromosome : np.ndarray
        Dummy-coded chromosome of videos
    video_lengths : np.ndarray
        Lenghts (in seconds) of each video
    Returns
    -------
    int
        Length of set of videos
    """
    return sum(chromosome*video_lengths)


def calc_fitness_individual(chromosome, video_list, video_data):
    """Calculate the "fitness" of an individual chromosome
    Fitness is the determinant of the covariance matrix of the ts data for each
    emotion

    Parameters
    ----------
    chromosome : np.ndarray
        Dummy-coded chromosome of videos
    video_list : np.ndarray
        List of all video titles (in this case number identifiers)
    video_data : pd dataframe
        Dataframe of Emotion by Time w/ video as a column

    Returns
    -------
    float
        Determinant of the covariance matrix of all emotions by time

    """
    keep_videos = list(set(video_list*chromosome)-{0})
    video_mat = video_data.loc[video_data['video'].isin(keep_videos)]
    video_mat = video_mat.reset_index(drop=True).drop('video', axis=1)
    video_cov = video_mat.cov()
    return linalg.det(video_cov)


def calc_fitness_all(chromosomes, video_list, video_data):
    """Calculates fitness for all chromosomes

    Parameters
    ----------
    chromosomes : np.ndarrray
        List of chromosomes
    video_list : np.ndarray
        List of all video titles (in this case number identifiers)
    video_data : pd dataframe
        Dataframe of Emotion by Time w/ video as a column

    Returns
    -------
    list
        Determinant of the covariance matrix of all emotions by time

    """
    fitness = []
    for chromosome in chromosomes:
        fitness.append(calc_fitness_individual(chromosome, video_list,
                       video_data))
    return fitness


def mutate(chromosome, max_attempts, video_lengths, max_seconds):
    """Point mutation by removing one "gene" and adding another

    Parameters
    ----------
    chromosome : np.ndarray
        Dummy-coded chromosome of videos
    max_attempts : int
        Maximum number of tries to mutate (it may be possible theres no combo
        that fits our criteria (< max_seconds))
    video_lengths : np.ndarray
        Lengths (in seconds) of each video
    max_seconds : int
        Maximum number of seconds allowed for all videos

    Returns
    -------
    list
        New chromosome with mutation

    """
    for attempt in range(max_attempts):
        mutated = chromosome.copy()
        # Pick a random point to mutated - copied from stack_overflow,
        # find better way to write out
        mutation_pt_rm = random.choice([i for i,
                                        x in enumerate(chromosome) if x == 1])
        mutation_pt_add = random.choice([i for i,
                                         x in enumerate(chromosome) if x == 0])
        mutated[mutation_pt_rm] = 0
        mutated[mutation_pt_add] = 1

        if (calc_duration(mutated, video_lengths) < max_seconds) and (
        calc_duration(mutated, video_lengths) !=
        calc_duration(chromosome, video_lengths)):
            return mutated

    return gen_chromosome()
