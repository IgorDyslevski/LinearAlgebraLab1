class Matrix:
    def __init__(self, matrix=None, sparse=None):
        assert not (matrix is None and sparse is None)
        if matrix is None:
            self.sparse = sparse
        else:
            self.sparse = self.matrix2sparse(matrix)

    def matrix2sparse(self, matrix):
        assert len(matrix) > 0 and len(matrix[0]) > 0
        values = []
        col_indices = []
        row_ptr = [0]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                value = matrix[i][j]
                if value != 0:
                    values.append(value)
                    col_indices.append(j)
            row_ptr.append(len(values))
        return values, col_indices, row_ptr

    def sparse2matrix(self, sparse):
        values, col_indices, row_ptr = sparse
        assert len(values) == len(col_indices) and len(values) > 0 and len(row_ptr) > 0
        rows = len(row_ptr) - 1
        cols = max(col_indices) + 1
        matrix = [[0] * cols for _ in range(rows)]
        for i in range(len(row_ptr) - 1):
            for j in range(row_ptr[i], row_ptr[i + 1]):
                matrix[i][col_indices[j]] = values[j]
        return matrix

    def __str__(self):
        return str(self.sparse)

    def __repr__(self):
        return f'Matrix(sparse={str(self.sparse)})'