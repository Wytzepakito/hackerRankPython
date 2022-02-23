

def print_mat(a, b, mat):
    print(a)
    for i in range(len(mat)):
        print(mat[i])







def longest_substring(a,b):
    mat = []
    for col in range(len(b) + 1):
        row = [0] * (len(a) + 1)
        mat.append(row)


    highest_score = 0

    for c in range(len(b)):
        for r in range(len(a)):
            
            if r == 0 or c == 0:
                mat[c][r] = 0
            else:
                #score = max(mat[c - 1][r], mat[c][r -1], mat[c -1][r -1])
                


                if b[c - 1] == a[r  - 1]:
                    print(f"Had a match! at {c}, {r}")
                    # We have a Match!!

                    score = mat[c - 1][r - 1] + 1
                    mat[c][r] = score


                    if score > highest_score:
                        highest_score = score


    print_mat(a,b, mat)

    print(highest_score)



            
















print(longest_substring("tutorialhorizon", "dynamictutorialProgramming"))