

def get_largest_k(arr, k):

    temp = arr[:k]

    for i in range(k, len(arr)):
        num = arr[i]
        mini = min(temp)
        if num > mini:
            temp[temp.index(mini)] = num

    print(temp)







  
# Driver code to test above
arr = [64, 11, 3 , 34, 25, 12, 22, 11, 90]

get_largest_k(arr, 3)
  
