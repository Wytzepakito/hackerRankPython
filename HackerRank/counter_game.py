def get_lowest_two(n):
    count = 0
    while(n != 0):
        n = n >> 1
        count += 1
    return 2 ** (count - 1)




def counterGame(n):
    # Write your code here
    turns = 0
    while n != 1:
        print(n)
        # Is a power of two
        if (n & n - 1) == 0:
            n = n // 2
        else:
            n = n - get_lowest_two(n)
        turns += 1

    if turns % 2 == 0:
        return("Lou")
    else:
        return("Richard")







print(counterGame(6))