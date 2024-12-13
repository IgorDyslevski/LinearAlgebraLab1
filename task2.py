from matrix import *


def matrix_sum(sparse1, sparse2):
    if sparse1.n() != sparse2.n() or sparse1.m() != sparse2.m():
        print("N1 и N2 должны быть равны и M1 и M2 должны быть равны")
        return None
    return (sparse1 + sparse2).matrix()

def matrix_scalar_mul(sparse, scalar):
    return (sparse * scalar).matrix()

def matrix_matrix_mul(sparse1, sparse2):
    if sparse1.m() != sparse2.n():
        print("Матрицы не согласованы")
        return None
    return (sparse1 * sparse2).matrix()


if __name__ == '__main__':
    sparse1 = MatrixUtils.dense2sparse(MatrixUtils.read2dense('Введите N и M', 'Введите матрицу'))
    sparse2 = MatrixUtils.dense2sparse(MatrixUtils.read2dense('Введите N и M', 'Введите матрицу'))
    if sparse1.n() == sparse2.n() and sparse1.m() == sparse2.m():
        print('sum:', matrix_sum(sparse1, sparse2))
    if sparse2.n() == sparse1.m():
        print('mul:', matrix_matrix_mul(sparse1, sparse2))
    scalar = int(input())
    print(f'm1 * {scalar}:', matrix_scalar_mul(sparse1, scalar))
    print(f'm2 * {scalar}:', matrix_scalar_mul(sparse2, scalar))
