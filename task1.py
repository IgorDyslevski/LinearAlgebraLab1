from matrix import *

def dense2sparse(n, m, matrix):
    dense = DenseMatrix(matrix)
    sparse = MatrixUtils.dense2sparse(dense)
    return sparse.matrix()
    
def trace(n, m, matrix):
    if n != m:
        print("N дожно быть равно M для подсчета следа")
        return None
    sparse = MatrixUtils.dense2sparse(DenseMatrix(matrix))
    return sparse.trace()

def get_by_idx(n, m, matrix, i, j):
    sparse = MatrixUtils.dense2sparse(DenseMatrix(matrix))
    return sparse[i][j]


if __name__ == '__main__':
    dense = MatrixUtils.read2dense('Введите N и M', 'Введите матрицу')
    print('sparse:', dense2sparse(dense.n(), dense.m(), dense.matrix()))
    if dense.n() == dense.m():
        print('trace:', trace(dense.n(), dense.m(), dense.matrix()))
    i, j = map(int, input('Введите i и j\n').split())
    print(f'matrix[{i}][{j}]:', get_by_idx(dense.n(), dense.m(), dense.matrix(), i, j))
