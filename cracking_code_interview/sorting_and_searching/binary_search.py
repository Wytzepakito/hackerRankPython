


def binary_search(arr, target):

    low = 0
    high = len(arr)-1

    while(low <= high):
        mid = low + ((high - low) // 2)

        # search left
        if (arr[mid] > target):
            high = mid - 1
        # search right
        elif (arr[mid] < target):
            low = mid + 1
        else:
            return mid
    return -1


    









print(binary_search([2, 2, 4, 5, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 18], ))
