



def quick_sort(arr, low, high):

    if low < high:
        mid = partition(arr, low, high)
        quick_sort(arr, low, mid - 1)
        quick_sort(arr, mid +1, high)



def partition(arr, low, high):
    pivot = arr[low + ((high - low) // 2)]


    while( low <= high):

        while(arr[low] < pivot):
            low += 1
        print(f"{high = }, {pivot = }, {low = }")
        print(arr)
        while(arr[high] > pivot):
            print(high)
            high -= 1

        swap(arr, low, high)

    return low




def swap(arr, low, high):
    temp = arr[low]
    arr[low] = arr[high]
    arr[high] = temp





arr = [10, 7, 8, 6, 3, 1, 2]

quick_sort(arr, 0, len(arr) - 1)

print(arr)