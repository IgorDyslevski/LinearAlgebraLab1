from matrix import *
from task1 import *

def test_dense2sparse():
    n, m = 7, 7
    matrix = [[9, 0, 0, 3, 1, 0, 1],
              [0, 11, 2, 1, 0, 0, 2],
              [0, 1, 10, 2, 0, 0, 0],
              [2, 1, 2, 9, 1, 0, 0],
              [1, 0, 0, 1, 12, 0, 1],
              [0, 0, 0, 0, 0, 8, 0],
              [2, 2, 0, 0, 3, 0, 8]]
    assert dense2sparse(n, m, matrix) == ([9, 3, 1, 1, 11, 2, 1, 2, 1, 10, 2, 2, 1, 2, 9, 1, 1, 1, 12, 1, 8, 2, 2, 3, 8],
                                             [0, 3, 4, 6, 1, 2, 3, 6, 1, 2, 3, 0, 1, 2, 3, 4, 0, 3, 4, 6, 5, 0, 1, 4, 6],
                                             [0, 4, 8, 11, 16, 20, 21, 25])

def test_trace():
    n, m = 5, 5
    matrix = [[5, 3, 7, 9, 0],
              [5, 134, 7, 9, 0],
              [5, 3, 231, 9, 0],
              [5, 135, 7, 553, 0],
              [5, 3, 7, 9, 10113]]
    assert trace(n, m, matrix) == 11036

def test_get_by_idx():
    n, m = 4, 5
    matrix = [[5, 3, 7, 9, 0],
              [5, 134, 7, 9, 0],
              [5, 3, 231, 9, 0],
              [5, 135, 7, 553, 0]]
    assert get_by_idx(n, m, matrix, 2, 2) == 231
