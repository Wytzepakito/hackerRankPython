def birthday(s, d, m):
    # Write your code here
    count_ways = 0

    for ii in range(len(s) + 1):
        if ii > (m - 1):
            if sum(s[ii-m:ii]) == d:
                count_ways += 1

    return count_ways









print(birthday([2, 2, 1, 3, 2], 4, 2))