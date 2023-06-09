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
    def T(self):
        lst = []
        for i in range(len(self.data)):
            tmp_lst = []
            for line in self.data:
                tmp_lst.append(line[i])
            lst.append(tmp_lst)
        return Matrix(lst)
    def __str__(self):
        return "This is a matrix class :\
            \nGoal: Manipulation and understanding of basic matrix operations.\
            \nType of operation:\
            \n- matrix-matrix operations( *, +, -)\
            \n- scalar-matrix operation(*, /)\
            \n- vector-matrix operations(*)"

    def __repr__(self):
        return "This is a matrix class :\
            \nGoal: Manipulation and understanding of basic matrix operations.\
            \nType of operation:\
            \n- matrix-matrix operations( *, +, -)\
            \n- scalar-matrix operation(*, /)\
            \n- vector-matrix operations(*)"

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
    # @dispatch(int or float)
    def __mul__(self,matrix):
        # ishould test for error when passing wrong types
        if isinstance(matrix, (float, int)):
            lst = []
            for inside_lst in self.data:
                lst.append([x * matrix for x in inside_lst])
            return Matrix(lst)
        elif isinstance(matrix,Matrix):
            if self.shape[1] != matrix.shape[0] or not isinstance(matrix, Matrix):
                print("matix-matrix Mutiplication can only happen\
                \nbetween two matrices of compatible dimension: (m × n) and (n × p),")
                print("i.e: the number of columns of the first matrice is\
                    \nthe number of lines in the second!!!")
                sys.exit()
            else:
                transpose = matrix.T().data
                new_matrix = []
                for line in self.data:
                    line_of_new_matrix = []
                    for column in transpose:
                        line_of_new_matrix.append(sum(line[i] * column[i] for i in range(len(line))))
                    new_matrix.append(line_of_new_matrix)
                return Matrix(new_matrix)
        # elif isinstance(matrix, Vector):
        #not implemented yet
        else:
            print("Error: NotImplemented")
            print("Hint: Implemented multiplications")
            print("- matrix * matrix")
            pirnt("- scalar matrix")
            print("-vectr * matrix")
            sys.exit()

    def __rmul__(self,matrix):
        # ishould test for error when passing wrong types
        print("are we even entring rmul")
        if isinstance(matrix, (float, int)):
            lst = []
            for inside_lst in self.data:
                lst.append([x * matrix for x in inside_lst])
            return Matrix(lst)
        elif isinstance(matrix,Matrix):
            if self.shape[1] != matrix.shape[0] or not isinstance(matrix, Matrix):
                print("matrix-matrix Mutiplication can only happen\
                \nbetween two matrices of compatible dimension: (m × n) and (n × p),")
                print("i.e: the number of columns of the first matrice is\
                    \nthe number of lines in the second!!!")
                sys.exit()
            else:
                transpose = matrix.T().data
                new_matrix = []
                for line in self.data:
                    line_of_new_matrix = []
                    for column in transpose:
                        line_of_new_matrix.append(sum(line[i] * column[i] for i in range(len(line))))
                    new_matrix.append(line_of_new_matrix)
                return Matrix(new_matrix)
        # elif isinstance(matrix, Vector):
        #not implemented yet
        else:
            print("Error: NotImplemented")
            print("Hint: Implemented multiplications")
            print("- matrix * matrix")
            pirnt("- scalar matrix")
            print("-vectr * matrix")
            sys.exit()


# __str__
# __repr__

    def print_data(self):
        print("the data in the matrix is:")
        print(self.data) 
        print("the shape  of the matrix is:")
        print(self.shape)


class Vector(Matrix):
    def __init__(self,data):
        if not isinstance(data,list) or len(data) == 0 or len(data[0]) == 0:
            print("Error: please provide a proper list to initialize your vector")
            sys.exit()
        for element in data:
            if not all([isinstance(el,(float, int)) for el in element]):
                print("Error: please provide a proper list to initialize your vector")
                sys.exit()
        if len(data) > 1:
            for element in data:
                if len(element) != 1:
                    print("Error: please provide a proper list to initialize your vector")
                    sys.exit()
        self.data = data
        self.shape = (len(data), len(data[0]))
        
    def dot(self,vector):
        summ = 0
        if not isinstance(vector, Vector):
            print("please provide a proper vector")
        elif vector.shape != self.shape:
            print(". product can only done between 2 vectors of the same shape")
        elif self.shape[0] == 1:
            # summ = [self.data[x] + vector.data[x] for x in range(0,len(self.data))]
            for i in range(len(self.data[0])):
                summ += self.data[0][i] * vector.data[0][i]
        else:
            for i in range(len(self.data)):
                summ += self.data[i][0] * vector.data[i][0]
        return summ
