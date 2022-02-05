def quick_sort(arr, low, high, ind_arr):
    index = partition(arr, low, high, ind_arr)
    print(arr)
    if( low < index - 1):
        quick_sort(arr, low, index - 1, ind_arr)
    if ( high > index):
        quick_sort(arr, index, high, ind_arr)


def swap(arr, low, high, ind_arr):
    temp = arr[low]
    arr[low] =  arr[high]
    arr[high] = temp
    temp = ind_arr[low]
    ind_arr[low] = ind_arr[high]
    ind_arr[high]= temp

def partition(arr, low, high, ind_arr):
    pivot = arr[low + ((high - low) // 2)]
    print(f"{arr[pivot] = }, {low =}, {high =}")

    while( low <= high):

        while (arr[low] < pivot):
            low += 1

        while(arr[high] > pivot):
            high -= 1

        if (low <= high):
            swap(arr, low, high, ind_arr)
            low += 1
            high -= 1

    return low


arr = [8, 2, 1, 5, 4, 3, 5, 6, 7, 8, 9, 2, 1, 10, 13, 14, 1]
ind_arr = [i for i in range(len(arr))]

print(arr)
quick_sort(arr, 0, len(arr)-1, ind_arr)
print(arr)

print(ind_arr)
