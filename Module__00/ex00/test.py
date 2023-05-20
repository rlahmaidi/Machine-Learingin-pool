from matrix import Matrix

if __name__ == "__main__":
    # #  @@@@@@@@@@@@@@constuctors
    # matrix = Matrix([[1,2,3],[4,5,6]])
    # matrix.print_data()
    # matrix1 = Matrix(3,3)
    # matrix1.print_data()

    ## @@@@@@@@@@@__add__@@@@@@
    print("##########3__add__tests")
    matrix = Matrix([[1,2,3], [4,5,6]])
    matrix1 = Matrix([[1,1,1], [2,2,2]])
    matrix2 = matrix.__add__(matrix1)
    matrix2.print_data()
    #####@@@@@@@@@@@ __radd__@@@@@@@
    print("########### __radd_test######")
    matrix = Matrix([[1,2,3],[4,5,6],[7,8,9]])
    matrix1 = Matrix([[1,1,1],[2,2,2],[3,3,3]])
    result = matrix + matrix1
    result.print_data()