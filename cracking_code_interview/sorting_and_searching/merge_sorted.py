


def sorted_merge(A, B):
    if A is None or len(A) ==0:
        return B
    elif B is None or len(B) == 0:
        return A
    

    A_ind = len(B) - 1
    B_ind = len(B) - 1
    insert_pos = len(A) -1

    while(A_ind != 0 or B_ind != 0):
        if A[A_ind] > B[B_ind]:
            A[insert_pos] = A[A_ind]
            A_ind -= 1
        else:
            A[insert_pos] = B[B_ind]
            B_ind -= 1
        insert_pos -= 1

    print(A)


    








A = [2, 4, 5, 6, 8, 11, 12, 13, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0]
B = [3, 6, 7, 8, 9, 10, 14, 16, 17]


sorted_merge(A,B)