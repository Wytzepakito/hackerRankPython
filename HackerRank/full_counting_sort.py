string = """20
0 ab
6 cd
0 ef
6 gh
4 ij
0 ab
6 cd
0 ef
6 gh
0 ij
4 that
3 be
0 to
1 be
5 question
1 or
2 not
4 is
2 to
4 the"""

import io

buf = io.StringIO(string)


def countSort(arr):


    

    result = [[] for i in range(10000000)]
    
    for i in range(n //2):
        result[int(arr[i][0])].append("-")
        
    for i in range(n//2, n):
        result[int(arr[i][0])].append(arr[i][1])
        


    for string in result:
        if string:
            print(*string, end = " ")
        


            



 
        


n = int(buf.readline())

arr = []

for _ in range(n):
    data = buf.readline().rstrip().split()
    arr.append([int(data[0]), data[1]])

countSort(arr)





