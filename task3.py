from matrix import *


def det(n, m, matrix):
    if n != m:
        print("N дожно быть равно M для подсчета определителя")
        return None
    sparse = MatrixUtils.dense2sparse(DenseMatrix(matrix))
    dense = MatrixUtils.sparse2dense(sparse)
    det = dense.det_gauss()
    print(dense.det())
    return det

def inv_exist(n, m, matrix):
    if det(n, m, matrix) != 0:
        print('да')
    else:
        print('нет')


if __name__ == '__main__':
    dense = MatrixUtils.read2dense('Введите N и M', 'Введите матрицу')
    if dense.n() == dense.m():
        print('det:', det(dense.n(), dense.m(), dense.matrix()))
        print('inv:', end=' ')
        inv_exist(dense.n(), dense.m(), dense.matrix())
