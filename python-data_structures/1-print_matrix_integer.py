def print_matrix_integer(matrix=[[]]):
    if len(matrix)==0:
        print(" \n")
        return
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("{:d}".format(matrix[i][j]), end= " " if j !=len(matrix[i])-1 else '')
        print()

if __name__ == "__main__":
    print_matrix_integer(
 )