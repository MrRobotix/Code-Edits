#Jadhav Yashodip
#Matrix addition,substraction,multiplication
print("Basic Matrix Operations using Python")
n1 = 0
n = 0
n2 = 0
res = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

print("Please input data for matrix operations")
row1 = int(input("Enter no. of rows in first matrix:"))
col1 = int(input("Enter number of columns in first matrix:"))
row2 = int(input("Enter number of rows in second matrix:"))
col2 = int(input("Enter number of columns in second matrix:"))


def sub_mat(n1, n2, row1, col1):
    pass


def main():
    print(
        " 1. Accept two matrices from user: \n 2. Show the matrices value: \n 3. Addition of two matrices: \n 4. Subtraction of two matrices: \n 5. Multiplication of matrices: \n 6. Transpose of a matrix: \n 7. Exit")
    ch = int(input("Enter your choice:"))
    if ch == 1:
        print("Enter values for first matrix:")
        accept(n1, row1, col1)
        print("Enter values for second matrix:")
        accept(n2, row2, col2)
        main()
    elif ch == 2:
        print("Value of first matrix is as follows:")
        show(n1, row1, col1)
        print("Value of second matrix is as follows:")
        show(n2, row2, col2)
        main()
    elif ch == 3:
        print("Addition of the two matrices is as follows:")
        if ((row1 == row2) and (col1 == col2)):
            add_mat(n1, n2, row1, col1)
            show(res, row1, col1)
        else:
            print("Addition is not possible.")
            main()
    elif ch == 4:
        print("Subtraction of the two matrices is as follows:")
        if ((row1 == row2) and (col1 == col2)):
            sub_mat(n1, n2, row1, col1)
            show(res, row1, col1)
        else:
            print("Subtarction is not possible")
        main()
    elif ch == 5:
        print("Multiplication of the matrices is as follows:")
        if (col1 == row2):
            mul_mat(n1, n2, row2, col1)
            show(res, row2, col1)
        else:
            print("Multiplication is not possible")
        main()


    elif ch == 6:
        print("Before transpose, matrix is:")
        show(n1, row1, col1)
        print("After transpose, matrix is:")
        trans_mat(n1, row1, col1)
        show(res, row1, col1)
        main()
    elif ch == 7:
        exit
    else:
        print("Entered choice is not valid")


# Function name: accept
# use: To accept elements from user and store itin matrix

def accept(n, row, col):
    for i in range(row):
        c = []
    for j in range(col):
        no = int(input("Enter value of matrix[" + str(i) + "][" + str(j) + "]::"))
        c.append(no)
    print("-------------------------------")
    n.append(c)


# Function name: show
# use: To display elements from the matrices

def show(n, row, col):
    for i in range(row):
        for j in range(col):
            print(n[i][j], end="")
        print()


# Functionname: add_mat
# use: To perform addition of the given matrices

def add_mat(n1, n2, row, col):
  for i in range(row):
    for j in range(col):
      res[i][j] = n1[i][j] + n2[i][j]


# Function name: mul_mat
# use: To perform multiplication of the given matrics

def mul_mat(n1, n2, row, col):
    for i in range(row):
        for j in range(col):
            for k in range(col):
                res[i][j] = res[i][j] + n1[i][k] * n2[k][j]


# Function name: trans_mat
# use: To perform transpose of a matrix

def trans_mat(n, row, col):
    for i in range(row):
        for j in range(col):
            res[i][j] = n[j][i]


main()
