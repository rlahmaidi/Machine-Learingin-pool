import sys
from multipledispatch import dispatch

class Matrix:
    @dispatch(list)
    def __init__(self,data = [[]]):
        if not isinstance(data, list):
            print("Error:please provide a proper matrix or a proper shape of matrix")
            sys.exit()
        self.data = data
        self.shape = (len(data),len(data[0]))
    @dispatch(int,int)
    def __init__(self, lines, columns):
        self.data = []
        if not isinstance(lines, int)\
            or not isinstance(columns, int):
            print("Error:please provide a proper matrix or a proper shape of matrix")
            sys.exit()
        for i in range(lines):
            self.data.append([0] * columns)
        self.shape = (lines, columns)

# add : only matrices of same dimensions.
    def __add__(self, matrix):
        if not isinstance(matrix, Matrix):
            print("Error: a matix can only be added to another proper matrix")
            sys.exit()
        elif self.shape != matrix.shape:
            print("Error: a matrix can only be added to another matrix with some dimensions")
            sys.exit()
        else:
            lst = []
# __radd__
# # sub : only matrices of same dimensions.
# __sub__
# __rsub__
# # div : only scalars.
# __truediv__
# __rtruediv__
# # mul : scalars, vectors and matrices , can have errors with vectors and matrices,
# # returns a Vector if we perform Matrix * Vector mutliplication.
# __mul__
# __rmul__
# __str__
# __repr__

    def print_data(self):
        print("the data in the matrix is:")
        print(self.data) 
        print("the shape  of the matrix is:")
        print(self.shape)



    # data: list of lists
    # shape: the dimensions of the matrix as a tuple (rows, columns)