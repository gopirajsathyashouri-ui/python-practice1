# multi dimensional : navigating in the matrix

Matrix = [
           [1 ,2, 3],
           [4, 5, 6],
           [7, 8, 9]
        ]
row_2 = Matrix[1]
column_2 = [row[1 : 3] for row in Matrix]
print(column_2)
submatrix = [row[1 : 3] for row in Matrix[1 : 3]]
print(submatrix) 
