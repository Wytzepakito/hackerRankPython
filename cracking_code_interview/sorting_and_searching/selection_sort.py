import math


def selection_sort(arr):

    current_swap = 0

    while(current_swap != len(arr) - 1):

        min_element = math.inf
        min_ind = None
        for i in range(current_swap,len(arr)):
            if arr[i] < min_element:
                min_element = arr[i]
                min_ind = i

        temp = arr[current_swap]
        arr[current_swap] = arr[min_ind]
        arr[min_ind] = temp
        current_swap +=1


    return arr













print(selection_sort([2, 1, 7, 5, 4, 6, 3]))

print(selection_sort([2, 1, 7, 5, 4, 6, 3, 1]))