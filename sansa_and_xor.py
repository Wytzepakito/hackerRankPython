def sansaXor(arr):
    # Write your code here
    
    val = None
    super_arr = []
    for length in range(1, len(arr) + 1):
        for i in range(0, len(arr) - (length - 1)):
            sub_arr = arr[i:  i + length]
            if val == None:
                val = sub_arr[0]
                super_arr.append(val)
            elif len(sub_arr) == 1:
                val = val ^ sub_arr[0]
                super_arr.append(sub_arr[0])
            elif len(sub_arr) > 1:
                sub_val = sub_arr[0]
                super_arr.append(sub_val)
                for i in range(1, len(sub_arr)):
                    sub_val = sub_val ^ sub_arr[i] 
                    super_arr.append(sub_arr[i]) 
                val = val ^ sub_val     

    print(super_arr.count(4))
    print(super_arr.count(5))
    print(super_arr.count(7)) 
    return val


def sansaXor2(arr):

    val = arr[0]
    if len(arr) % 2 != 0:
        for i in range(1,len(arr)):
            if i % 2 == 0:
                val = val ^ arr[i]
    else:
        for i in range(1, len(arr)):
            if i % 2 == 0:
                val = val ^ arr[i]


    return val



















print(sansaXor([4,5,7, 5]))







