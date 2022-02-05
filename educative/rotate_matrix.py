
import math



def rotateMatrix(mat):
    size = len(mat)

    for i in range(0, (size//2)):

        for j in range(i, size - i - 1):
            #print(f"{i =}, {j =}")
            
            temp = mat[i][j]
            #print(temp)

            # move left bottom to left top
            mat[i][j] = mat[j][size  - 1 - i]

            # move right bottom to left bottom
            mat[j][size - 1 - i] = mat[size - 1 - i][size  - 1 - j]

            # move right top to right bottom
            mat[size - 1 - i][size - 1 - j] = mat[size - 1 - j][i]

            # move left top to right top
            mat[size - 1 - j][i] = temp




def rotateMatrix2(mat):

    control_sets = []

    for i in range(len(mat)//2):
        for j in range(math.ceil(len(mat)/2)):
            control_sets.append((i,j))
            print((i,j))

    uneven = False
    uneven_special = None
    if len(mat) % 2 == 1:
        uneven = True
        uneven_special = len(mat)//2



    for (i,j) in control_sets:
        # if uneven_special is not None and i == uneven_special or j == uneven_special:


        #     temp = mat[i][j] ## (0, 2) 3 ## (1, 2) ## 7

        #     mat[i][j] = mat[len(mat) - j - 1][i] ## (0, 2) 3 = 9 ##(1, 2) 7 = 10

        #     mat[len(mat) - j - 1][i] =  mat[len(mat) - i - 1][j] ## (0, 2) 9 = 20 ## (1,2) 10 = 15

        #     mat[len(mat) - i - 1][j] = mat[len(mat) - j - 1][len(mat) - i - 1] ## (0, 2) 20 = 8 ## (1, 2)  15 = 12

        #     mat[len(mat) - j - 1][len(mat) - i - 1] = temp ## (0, 2) 8 = 3 ## (1, 2) 12 = 7


        # else:

        temp = mat[i][j] # (0, 0) 1 # (0, 1) 2 # (1, 0) 5 $ (1, 1) 6

        mat[i][j] = mat[len(mat) - j - 1][i] ## (0, 0) 1 = 13 ## (0, 1)  2 = 9 ## (1, 0) 5 = 14 ## (1, 1) 6 = 10

        mat[len(mat) - j - 1][i] =  mat[len(mat) - i - 1][len(mat) - j - 1] # (0, 0) 13 = 16 # (0, 1) 9 = 15 # (1, 0) 14 = 12 # (1, 1) 10 = 11

        mat[len(mat) - i - 1][len(mat) - j - 1] = mat[j][len(mat) - i - 1] # (0, 0) 16 = 4 # (0, 1) 15 = 8 # (1, 0) 12 = 3 # (1, 1) 11 = 7

        mat[j][len(mat)- i - 1] = temp # (0, 0) 4 = 1 # (0, 1) 8 = 2 # (1, 0) 3 = 5 # (1, 1) 7 = 6

        

        

        


    
    





            
def displayMatrix(mat):

    for i in range(len(mat)):

        for j in range(len(mat[i])):
            print(mat[i][j], end = " ")

        print("")



mat1 = [[0 for x in range(4)] for y in range(4)]


mat2 = [[1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]]


mat3 = [[1, 2, 3, 4, 5],
        [5, 6, 7, 8, 6],
        [9, 10, 11, 12, 8],
        [13, 14, 15, 16, 17],
        [18, 19, 20, 21, 22]]

mat3_2 = [[1, 2, 3, 4, 5],
        [5, 6, 7, 8, 6],
        [9, 10, 11, 12, 8],
        [13, 14, 15, 16, 17],
        [18, 19, 20, 21, 22]]


displayMatrix(mat3)
# print("=" * 20)
# displayMatrix(mat3_2)


rotateMatrix(mat3_2)
rotateMatrix2(mat3)

print("="* 20)

print("Rotated:")
displayMatrix(mat3)
# print("=" * 20)
# displayMatrix(mat3_2)
