#!/usr/bin/python


import numpy as np


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
        Lenghs (in seconds) of each video

    Returns
    -------
    int
        Length of set of videos

    """
    return sum(chromosome*video_lengths)


def calc_fitness(chromsome, video_data):

    # If calculating fitness for one chromosome
    if type(chromsome) == np.ndarray:
        keep_videos = list(set(video_data*chromsome) - {0})
        video_mat = video_data.loc[video_data].isin(keep_videos)
        video_mat = video_mat.reset_index(drop=True).drop('video', axis=1)
        return video_mat
