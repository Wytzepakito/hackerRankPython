
def merge_sort(arr):
    helper_arr = [0] * len(arr)
    merge_sorting(arr, helper_arr, 0, len(arr) -1)



def merge_sorting(arr, helper_arr, low, high):
    if low < high:
        mid = low + ((high-low) // 2)
        merge_sorting(arr, helper_arr, low, mid)
        merge_sorting(arr, helper_arr, mid +1, high)
        merge(arr, helper_arr, low, mid, high)


def merge(arr, helper_arr, low, mid, high):
    for i in range(low, high + 1):
        helper_arr[i] = arr[i]

    helper_left = low
    helper_right = mid + 1
    current = low

    while(helper_left <=mid and helper_right <= high):
        if helper_arr[helper_left] <= helper_arr[helper_right]:
            arr[current] = helper_arr[helper_left]
            helper_left += 1
        else:
            arr[current] = helper_arr[helper_right]
            helper_right += 1
        current += 1

    remaining = mid - helper_left
    for i in range(remaining +1 ):
        arr[current + i] = helper_arr[helper_left + i]


arr = [8, 2, 1, 5, 4, 3, 5, 6, 7, 8, 9, 2, 1, 10, 13, 14, 1]

merge_sort(arr)
print(arr)