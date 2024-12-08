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

    def __call__(self):
        return self.sparse

class Row():
    def __init__(self, values, col_indices):
        self.values, self.col_indices = values, col_indices

    def __getitem__(self, idx):
        try:
            return self.values[self.col_indices.index(idx)]
        except:
            return 0


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

    def n(self):
        return self.matrix.n

    def m(self):
        return self.matrix.m

    def trace(self):
        result = 0
        values, col_indices, row_ptr = self.matrix()
        n, m = self.n(), self.m()
        assert n == m
        for i in range(n):
            for j in range(row_ptr[i], row_ptr[i + 1]):
                if i == col_indices[j]:
                    result += values[j]
        return result

    def __str__(self):
        return str(self.matrix.sparse)

    def __repr__(self):
        return f'Matrix(SparseMatrix({str(self.matrix.sparse)}, {self.matrix.n}, {self.matrix.m}))'

    def __getitem__(self, idx) -> Row:
        start_j, finish_j = self.matrix()[2][idx], self.matrix()[2][idx + 1]
        values, col_indices = self.matrix()[0][start_j:finish_j], self.matrix()[1][start_j:finish_j]
        return Row(values, col_indices)