class ABCMatrix:
    def __init__(self, matrix, n, m):
        self._matrix = matrix
        self._n = n
        self._m = m

    def matrix(self):
        return self._matrix

    def n(self):
        return self._n

    def m(self):
        return self._m

    def __getitem__(self, idx):
        pass

    def __add__(self, val):
        pass

    def __mul__(self, val):
        pass

    def __repr__(self):
        return f'ABCMatrix(matrix={self.matrix()}, n={self.n()}, m={self.m()})'


class DenseMatrix(ABCMatrix):
    def __init__(self, matrix, n=None, m=None):
        if not (n is None and m is None):
            assert len(matrix) == n and len(matrix[0]) == m
        else:
            n, m = len(matrix), len(matrix[0])
        super().__init__(matrix, n, m)

    def __getitem__(self, idx):
        return self.matrix()[idx]

    def __repr__(self):
        return f'DenseMatrix(matrix={self.matrix()}, n={self.n()}, m={self.m()})'


    def trace(self):
        result = 0
        n, m = self.n(), self.m()
        assert n == m, "Матрица должна быть квадратной"
        for i in range(n):
            result += self.matrix()[i][i]
        return result

    def __add__(self):
        assert self.n() == val.n() and self.m() == self.m(), "Размеры матриц должны совпадать"
        matrix = [[0] * self.m() for _ in range(self.n())]
        for i in range(self.n()):
            for j in range(self.m()):
                matrix[i][j] = self.matrix()[i][j] + val.matrix()[i][j]
        return DenseMatrix(matrix)

    def __mul__(self, val):
        if isinstance(val, (int, float)):
            matrix = [[0] * self.m() for _ in range(self.n())]
            for i in range(self.n()):
                for j in range(self.m()):
                    matrix[i][j] = self.matrix()[i][j] * val
            return DenseMatrix(matrix)
        else:
            assert self.m() == val.n(), "Количество столбцов первой матрицы должно совпадать с количеством строк второй"
            matrix = [[0] * val.m() for _ in range(self.n())]
            
            for i in range(self.n()):
                for j in range(val.m()):
                    for k in range(val.n()):
                        matrix[i][j] += self.matrix()[i][k] * val.matrix()[k][j]
            
            return DenseMatrix(matrix)

    def det(self):
        if self.n() == 1:
            return matrix[0][0]
        if self.n() == 2:
            return self[0][0] * self[1][1] - self[0][1] * self[1][0]
        det = 0
        for col in range(self.n()):
            minor = [[self[i][j] for j in range(self.n()) if j != col] for i in range(1, self.n())]
            det += ((-1) ** col) * self[0][col] * det(minor)
    
        return det

        

class Row():
    def __init__(self, values, col_indices):
        self.values, self.col_indices = values, col_indices

    def __getitem__(self, idx):
        try:
            return self.values[self.col_indices.index(idx)]
        except:
            return 0

    def __repr__(self):
        return f'{self.values},  {self.col_indices}'


class SparseMatrix(ABCMatrix):
    def __init__(self, matrix, n, m):
        assert len(matrix[0]) == len(matrix[1]) and len(matrix[2]) > 0, "Входные данные неправильные"
        super().__init__(matrix, n, m)

    def __getitem__(self, idx):
        start_j, finish_j = self.matrix()[2][idx], self.matrix()[2][idx + 1]
        values, col_indices = self.matrix()[0][start_j:finish_j], self.matrix()[1][start_j:finish_j]
        return Row(values, col_indices)

    def __repr__(self):
        return f'SparseMatrix(matrix={self.matrix()}, n={self.n()}, m={self.m()})'


    def trace(self):
        result = 0
        values, col_indices, row_ptr = self.matrix()
        n, m = self.n(), self.m()
        assert n == m, "Матрица должна быть квадратной"
        for i in range(n):
            for j in range(row_ptr[i], row_ptr[i + 1]):
                if i == col_indices[j]:
                    result += values[j]
        return result


    def __add__(self, val):
        assert self.n() == val.n() and self.m() == self.m(), "Размеры матриц должны совпадать"
        values1, col_indices1, row_ptr1 = self.matrix()
        values2, col_indices2, row_ptr2 = val.matrix()

        new_values = []
        new_col_indices = []
        new_row_ptr = [0]
        sparse1_ind = 0
        sparse2_ind = 0
        for i in range(self.n()):
            val_count = row_ptr1[i + 1] + row_ptr2[i + 1] - row_ptr1[i] - row_ptr2[i]
            for j in range(self.m()):
                value = 0
                if col_indices1[sparse1_ind] == j:
                    value += values1[sparse1_ind]
                    sparse1_ind += 1
                    val_count -= 1
                if col_indices2[sparse2_ind] == j and val_count > 0:
                    value += values2[sparse2_ind]
                    sparse2_ind += 1
                    val_count -= 1
                if value != 0:
                    new_values.append(value)
                    new_col_indices.append(j)

                if val_count <= 0:
                    break
            new_row_ptr.append(len(new_values))
        return SparseMatrix((new_values, new_col_indices, new_row_ptr), self.n(), self.m())

    def __mul__(self, val):
        if isinstance(val, (int, float)):
            values, col_indices, row_ptr = self.matrix()
            values = [i * val for i in values]
            return SparseMatrix((values, col_indices, row_ptr), self.n(), self.m())
        else:
            assert self.m() == val.n(), "Количество столбцов первой матрицы должно совпадать с количеством строк второй"
            values1, col_indices1, row_ptr1 = self.matrix()
            n1, m1 = self.n(), self.m()
            values2, col_indices2, row_ptr2 = val.matrix()
            n2, m2 = val.n(), val.m()
            
            new_values = []
            new_col_indices = []
            new_row_ptr = [0]
            
            for i in range(n1):
                row_result = {}
                for j in range(row_ptr1[i], row_ptr1[i + 1]):
                    col1 = col_indices1[j]
                    val1 = values1[j]
                    for k in range(row_ptr2[col1], row_ptr2[col1 + 1]):
                        col2 = col_indices2[k]
                        val2 = values2[k]
                        if col2 in row_result:
                            row_result[col2] += val1 * val2
                        else:
                            row_result[col2] = val1 * val2
                for col, value in sorted(row_result.items()):
                    if value != 0:
                        new_values.append(value)
                        new_col_indices.append(col)
                new_row_ptr.append(len(new_values))
            
            return SparseMatrix((new_values, new_col_indices, new_row_ptr), n1, m2)

    def det(self):
        assert self.n() == self.m()
        
        def minor(matrix, x, y): 
            values, col_indices, row_ptr = matrix.matrix()

            new_values = []
            new_col_indices = []
            new_row_ptr = [0]
            sparse_ind = 0
            for i in range(matrix.n()):
                val_count = row_ptr[i + 1] - row_ptr[i]
                if i == y:
                    sparse_ind += val_count
                    continue
                for j in range(matrix.m()):
                    if sparse_ind == len(values) or val_count == 0:
                        break
                    if j == x:
                        if col_indices[sparse_ind] == j:
                            sparse_ind += 1
                            val_count -= 1
                        continue
                    value = 0
                    if col_indices[sparse_ind] == j:
                        value += values[sparse_ind]
                        sparse_ind += 1
                        val_count -= 1
                    if value != 0:
                        new_values.append(value)
                        if j > x:
                            new_col_indices.append(j - 1)
                        else:
                            new_col_indices.append(j)
                new_row_ptr.append(len(new_values))
            return SparseMatrix((new_values, new_col_indices, new_row_ptr), matrix.n() - 1, matrix.m() - 1)

        def det(matrix):
            if matrix.n() == 2:
                return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
            ans = 0
            for i in range(matrix.n()):
                ans += matrix[0][i] * det(minor(matrix, i, 0)) * (-1) ** i
            return ans
        
        return det(self)


class MatrixUtils:
    def dense2sparse(self, dense: DenseMatrix) -> SparseMatrix:
        assert dense.n() > 0 and dense.m() > 0
        values = []
        col_indices = []
        row_ptr = [0]
        for i in range(dense.n()):
            for j in range(dense.m()):
                value = dense[i][j]
                if value != 0:
                    values.append(value)
                    col_indices.append(j)
            row_ptr.append(len(values))
        return SparseMatrix([values, col_indices, row_ptr], dense.n(), dense.m())

    def sparse2dense(self, sparse: SparseMatrix) -> DenseMatrix:
        values, col_indices, row_ptr = sparse.matrix()
        rows = sparse.n()
        cols = sparse.m()
        matrix = [[0] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(row_ptr[i], row_ptr[i + 1]):
                matrix[i][col_indices[j]] = values[j]
        return DenseMatrix(matrix)
