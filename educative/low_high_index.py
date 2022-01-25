def find_low_index(arr,key):

    low = 0 
    high = len(arr)
    mid = int(len(arr)/2)

    while(low <= high):
        print(f"{low =}, {high =}")
        print(f"{arr[mid] =}, {mid =}")

        if arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

        mid = int((high - low)/2) + low

        if low < len(arr) and arr[low] == key:
            return low
    return -1


def find_high_index(arr, key):

    low = 0 
    high = len(arr)
    mid = int(len(arr)/2)

    while(low < high):


        if arr[mid] < key:
            low = mid + 1
        else:
            high = mid + 1
        
        mid = low + int((high - low)/ 2)

        if high > 0 and arr[high] == key:
            return high



arr = [1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 6, 6]

print(arr[8:10])
print(find_low_index(arr, 3))
print(find_high_index(arr, 3))