
def countingSort(arr):


    count_arr = [0] * 100

    for ii in arr:
        count_arr[ii] += 1

    return count_arr