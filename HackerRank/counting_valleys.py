

def countingValleys(steps, path):
    # Write your code here

    tot_val = 0

    mount_bool = False
    val_bool = False
    down_count = 0
    up_count = 0
    for char in path:
        if char == 'U' and val_bool == False:
            mount_bool = True
            up_count += 1 
        elif char == 'U' and val_bool == True:
            down_count -= 1
            if down_count == 0:
                val_bool = False
                tot_val += 1
        elif char == 'D' and mount_bool == False:
            val_bool = True
            down_count += 1
        elif char == 'D' and mount_bool == True:
            up_count -= 1
            if up_count == 0:
                mount_bool = False
    return tot_val


print(countingValleys(8, "UDDDUDUU"))
