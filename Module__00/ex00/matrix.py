import sys
from multipledispatch import dispatch

class Matrix:
    @dispatch(list)
    def __init__(self,data = [[]]):
        if not isinstance(data, list):
            print("Error:please provide a proper matrix or a proper shape of matrix")
            sys.exit()
        for i in data:
            if len(i) != len(data[0]):
                print('matrix lines should be the same size')
                print("matices always have a rectangular shape!!!")
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
            for x,y in zip(self.data, matrix.data):
                tmp_lst = []
                for i in range(len(x)):
                    tmp_lst.append(x[i] + y[i])
                lst.append(tmp_lst)
        return Matrix(lst)

    # __radd__
    def __radd__(self, matrix):
        if not isinstance(matrix, Matrix):
            print("Error: a matix can only be added to another proper matrix")
            sys.exit()
        elif self.shape != matrix.shape:
            print("Error: a matrix can only be added to another matrix with some dimensions")
            sys.exit()
        else:
            lst = []
            for x,y in zip(self.data, matrix.data):
                tmp_lst = []
                for i in range(len(x)):
                    tmp_lst.append(x[i] + y[i])
                lst.append(tmp_lst)
        return Matrix(lst)

# # sub : only matrices of same dimensions.
# __sub__
    def __sub__(self, matrix):
        if not isinstance(matrix, Matrix):
            print("Error: a matix can only be added to another proper matrix")
            sys.exit()
        elif self.shape != matrix.shape:
            print("Error: a matrix can only be added to another matrix with some dimensions")
            sys.exit()
        else:
            lst = []
            for x,y in zip(self.data, matrix.data):
                tmp_lst = []
                for i in range(len(x)):
                    tmp_lst.append(x[i] - y[i])
                lst.append(tmp_lst)
        return Matrix(lst)


# __rsub__
    def __rsub__(self, matrix):
        if not isinstance(matrix, Matrix):
            print("Error: a matix can only be added to another proper matrix")
            sys.exit()
        elif self.shape != matrix.shape:
            print("Error: a matrix can only be added to another matrix with some dimensions")
            sys.exit()
        else:
            lst = []
            for x,y in zip(self.data, matrix.data):
                tmp_lst = []
                for i in range(len(x)):
                    tmp_lst.append(x[i] - y[i])
                lst.append(tmp_lst)
        return Matrix(lst)

# # div : only scalars.
# __truediv__
    def __truediv__(self,scalar):
        if not isinstance(scalar, (int, float)):
            print("Error: you can only divise a matix\
            by a scalar(i.e int or float)")
            sys.exit()
        elif scalar == 0: 
            print("you can't devide a matrix by zero??!!!!!")
            sys.exit()
        else:
            lst = []
            for inside_lst in self.data:
                lst.append([x / scalar for x in inside_lst])
        return Matrix(lst)

# __rtruediv__
    def __rtruediv__(self,scalar):
        if not isinstance(scalar, (int, float)):
            print("Error: you can only divise a matix\
            by a scalar(i.e int or float)")
            sys.exit()
        elif scalar == 0: 
            print("you can't devide a matrix by zero??!!!!!")
            sys.exit()
        else:
            lst = []
            for inside_lst in self.data:
                lst.append([x / scalar for x in inside_lst])
        return Matrix(lst)

# # mul : scalars, vectors and matrices , can have errors with vectors and matrices,
# # returns a Vector if we perform Matrix * Vector mutliplication.
# __mul__
    @dispatch(int or float)
    def __mul__(self,scalar):
        # ishould test for error when passing wrong types
        lst = []
        for inside_lst in self.data:
            lst.append([x * scalar for x in inside_lst])
        return Matrix(lst)
            
    @dispatch(Matrix)
    def __mul__(self, matrix):
        # ishould test with wrong type
        if self.shape[1] != matrix.shape[0]:
            print("matix-matrix Mutiplication can only happen\
             between two matrices of compatible dimension: (m × n) and (n × p),")
             print("i.e: the number of columns of the first matrice is\
             the number of lines in the second!!!")
             sys.exit()
        else:
            for inside_lst in self.data:
                for z in zip([line for line in matrix.data]):
                    



    # @dispatch(Vector)
    # def __mul__(self, vector):

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