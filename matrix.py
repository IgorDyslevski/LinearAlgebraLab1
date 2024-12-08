class DenseMatrix():
    def __init__(self, matrix):
        self.matrix = matrix
        self.n = len(matrix)
        self.m = len(matrix[0])

    def __getitem__(self, idx):
        return self.matrix[idx]


class SparseMatrix():
    def __init__(self, sparse, n, m):
        assert len(sparse[0]) == len(sparse[1]) and len(sparse[0]) > 0 and len(sparse[2]) > 0
        self.sparse = sparse
        self.n = n
        self.m = m


class Matrix:
    def __init__(self, matrix: DenseMatrix | SparseMatrix):
        if type(matrix) is DenseMatrix:
            matrix = self.dense2sparse(matrix)
        self.matrix = matrix

    def dense2sparse(self, dense: DenseMatrix) -> SparseMatrix:
        assert dense.n > 0 and dense.m > 0
        values = []
        col_indices = []
        row_ptr = [0]
        for i in range(dense.n):
            for j in range(dense.m):
                value = dense[i][j]
                if value != 0:
                    values.append(value)
                    col_indices.append(j)
            row_ptr.append(len(values))
        return SparseMatrix([values, col_indices, row_ptr], dense.n, dense.m)

    def sparse2dense(self, sparse: SparseMatrix) -> DenseMatrix:
        values, col_indices, row_ptr = sparse.sparse
        rows = sparse.n
        cols = sparse.m
        matrix = [[0] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(row_ptr[i], row_ptr[i + 1]):
                matrix[i][col_indices[j]] = values[j]
        return DenseMatrix(matrix)

    def __str__(self):
        return str(self.matrix.sparse)

    def __repr__(self):
        return f'Matrix(SparseMatrix({str(self.matrix.sparse)}, {self.matrix.n}, {self.matrix.m}))'