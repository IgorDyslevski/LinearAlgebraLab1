from matrix import *


def matrix_sum(n1, m1, matrix1, n2, m2, matrix2):
    if n1 != n2 or m1 != m2:
        print("N1 и N2 должны быть равны и M1 и M2 должны быть равны")
        return None
    sparse1 = MatrixUtils.dense2sparse(DenseMatrix(matrix1))
    sparse2 = MatrixUtils.dense2sparse(DenseMatrix(matrix2))
    return (sparse1 + sparse2).matrix()

def matrix_scalar_mul(n, m, matrix, scalar):
    sparse = MatrixUtils.dense2sparse(DenseMatrix(matrix))
    return (sparse * scalar).matrix()

def matrix_matrix_mul(n1, m1, matrix1, n2, m2, matrix2):
    if m1 != n2:
        print("Матрицы не согласованы")
        return None
    sparse1 = MatrixUtils.dense2sparse(DenseMatrix(matrix1))
    sparse2 = MatrixUtils.dense2sparse(DenseMatrix(matrix2))
    return (sparse1 * sparse2).matrix()


if __name__ == '__main__':
    dense1 = MatrixUtils.read2dense('Введите N и M', 'Введите матрицу')
    dense2 = MatrixUtils.read2dense('Введите N и M', 'Введите матрицу')
    if dense1.n() == dense2.n() and dense1.m() == dense2.m():
        print('sum:', matrix_sum(dense1.n(), dense1.m(), dense1.matrix(), dense2.n(), dense2.m(), dense2.matrix()))
    if dense2.n() == dense1.m():
        print('mul:', matrix_matrix_mul(dense1.n(), dense1.m(), dense1.matrix(), dense2.n(), dense2.m(), dense2.matrix()))
    scalar = int(input())
    print(f'm1 * {scalar}:', matrix_scalar_mul(dense1.n(), dense1.m(), dense1.matrix(), scalar))
    print(f'm2 * {scalar}:', matrix_scalar_mul(dense2.n(), dense2.m(), dense2.matrix(), scalar))
