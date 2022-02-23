def gamingArray(arr):
    
    highest_num = 0
    lowest_highest = 0
    number_of_steps = 0
    for i in range(len(arr), 0, -1):
        num = arr[i]
        if num < arr[0]:
            pass
        elif num > highest_num:
            highest_num = num
            number_of_steps = 1
        elif num < highest_num and num > lowest_highest and lowest_highest == 0:
            lowest_highest = num
            number_of_steps += 1
        elif num < highest_num and num > lowest_highest and lowest_highest != 0:
            lowest_highest = num


def gamingArray2(arr):
    arr_copy = arr.copy()

    arr.sort()
    arr.reverse()
    steps = 0
    last_index = len(arr) + 1

    for num in arr:
        ind = arr_copy.index(num)
        if ind > 0 and ind < last_index:
            steps += 1
            last_index = ind
        elif ind == 0:
            steps += 1
            break
    
    if steps % 2 == 0:
        return "ANDY"
    else:
        return "BOB"


def gamingArray3(arr):

    decreasing_stack = []

    for i in range(len(arr) -1, -1, -1):
        print(i)
        num = arr[i]
        while decreasing_stack and decreasing_stack[-1] < num:
            decreasing_stack.pop()

        decreasing_stack.append(num)

    if len(decreasing_stack) % 2 == 0:
        return "ANDY"
    else:
        return "BOB"








print(gamingArray3([2, 3, 5,  4, 6, 1]))
