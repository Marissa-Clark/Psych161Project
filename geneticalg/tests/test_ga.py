from geneticalg import gen_chrom, calc_duration
import numpy as np


def test_gen_chrom():
    assert sum(gen_chrom(10, [1, 2], [1, 1])) <= 2
    assert sum(gen_chrom(10, [1, 2], [5, 7])) < 2


def test_calc_duration():
    assert calc_duration([0, 0], np.array([1, 4])) == 0
    assert calc_duration([0, 1], np.array([5, 5])) == 5
    assert calc_duration([1, 1], np.array([2, 7])) == 9
