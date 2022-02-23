def twoArrays(k, A, B):
    # Write your code here

    A.sort()
    B.sort()
    B = B[::-1]

    for jj,ii in zip(A, B):
        target = k - ii
        if jj < target:
            return "NO"
    return "YES"




A = [2, 1, 3]
B = [7, 8, 9]
k = 10


print(twoArrays(k, A, B))



A = [1, 2, 2,  1]
B = [3, 3, 3, 4]
k = 5


print(twoArrays(k, A, B))

