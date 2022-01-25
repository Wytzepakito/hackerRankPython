def balancedSums(arr):
    # Write your code here

    left_side = 0
    right_side = sum(arr)

    for i in range( len(arr) ):
        if i > 0:
            left_side += arr[i -1]
        right_side -= arr[i]

        if left_side == right_side:
            return "YES"
    return "NO"




print(balancedSums([2, 0,0,0]))
print(balancedSums([1, 2, 3, 3]))
print(balancedSums([1, 2, 3]))
