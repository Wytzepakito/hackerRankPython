

global maximum



def _lis(arr, n):


    global maximum

    if n == 1:
        return 1

    maxEndingHere = 1

    for i in range(1, n):
        res = _lis(arr, i)
        if arr[i - 1] < arr[n - 1] and res +1 > maxEndingHere:
            maxEndingHere = res + 1


    return maxEndingHere


def lis(arr):
    

    global maximum

    n = len(arr)

    maximum = 1

    _lis(arr,n)


    return maximum
















print(lis([4, 5, 6, 10, 11, 18, 7, 1, 8, 9, 3, 4, 22]))