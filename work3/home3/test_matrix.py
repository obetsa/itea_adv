import pytest

from .home3_2 import Matrix


@pytest.mark.parametrize(
    "first_matrix, second_matrix, result_matrix", [
        (
            [[2, 2, 2],
             [2, 2, 2],
             [2, 2, 2]],
            [[1, 1, 1],
             [1, 1, 1],
             [1, 1, 1]],
            [[3, 3, 3],
             [3, 3, 3],
             [3, 3, 3]],
        ),
        (
            [[2, 2, 2],
             [-1, -1, -1],
             [12, 12, 12]],
            [[-1, 1, 1],
             [1, 0, 1],
             [1, 1, 7]],
            [[1, 3, 3],
             [0, -1, 0],
             [13, 13, 19]],
        ),
                (
            [[2, 2],
             [2, 2]],
            [[1, 1],
             [1, 1],],
            [[3, 3],
             [3, 3]],
        ),
    ])

def matrix_add(first_matrix, second_matrix, result_matrix):
    res_matrix = Matrix(first_matrix) + Matrix(second_matrix)
    assert res_matrix == Matrix(result_matrix)