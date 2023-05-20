from matrix import Matrix

if __name__ == "__main__":
    # #  @@@@@@@@@@@@@@constuctors
    # matrix = Matrix([[1,2,3],[4,5,6]])
    # matrix.print_data()
    # matrix1 = Matrix(3,3)
    # matrix1.print_data()

    ## @@@@@@@@@@@__add__@@@@@@
    # print("##########3__add__tests")
    # matrix = Matrix([[1,2,3], [4,5,6]])
    # matrix1 = Matrix([[1,1,1], [2,2,2]])
    # matrix2 = matrix.__add__(matrix1)
    # matrix2.print_data()
    # #####@@@@@@@@@@@ __radd__@@@@@@@
    # print("########### __radd_test######")
    # matrix = Matrix([[1,2,3],[4,5,6],[7,8,9]])
    # matrix1 = Matrix([[1,1,1],[2,2,2],[3,3,3]])
    # result = matrix + matrix1
    # result.print_data()
    ## @@@@@@@@@@@@  __sub__tests
    # print("##########    __sub_tesst#######")
    # matrix = Matrix([[1,2,3], [4,5,6]])
    # matrix1 = Matrix([[1,1,1], [1,1,6]])
    # result = matrix.__sub__(matrix1)
    # result.print_data()
    # print('#############  __rsub__tests######')
    # matrix = Matrix([[1,2,3], [4,5,6]])
    # matrix1 = Matrix([[1,1,1], [1,1,6]])
    # result = matrix - matrix1
    # result.print_data()

    # print('#############  __truediv__tests######')
    # matrix = Matrix([[1,2,3], [4,5,6]])
    # result = matrix.__truediv__(0)
    # result.print_data()
    # print('#############  __rtruediv__tests######')
    # matrix = Matrix([[1,2,3], [4,5,6]])
    # result = 4 / matrix
    # result.print_data()
    # print("############  .T transpose tests#######")
    # matrix = Matrix([[1,1,1],[2,2,2],[3,3,3]])
    # result = matrix.T()
    # result.print_data()

    # print('#############  __mul__tests(scalar)######')
    # matrix = Matrix([[1,2,3], [4,5,6]])
    # result = matrix * 2
    # result.print_data()
    # print("#########__mul__ tests####3")
    # A = Matrix([[1,2,3], [2,2,2],[1,1,1]])
    # B = Matrix([[1,1,1],[2,2,2],[1,1,1]])
    # result = A * B
    # result.print_data()
    # print('#############  __rmul__tests(matrix)######')
    # print("to remember: __rmull__ dosen't work when i use")
    # print("the operator * direcltely. I don't know why")
    # print("it doesn't make sense , but the mentioned in the subject that")
    # print("an error might happen with mul and rmul")
    # A = Matrix([[1,2,3], [2,2,2],[1,1,1]])
    # B = Matrix([[1,1,1],[2,2,2],[1,1,1]])
    # result = A.__rmul__(B)
    # result.print_data()
    
    