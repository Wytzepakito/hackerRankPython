def find_missing(inp):
    missing_sum = sum(inp)
    maxi = max(inp)

    real_sum = sum(range(maxi + 1))
    return real_sum - missing_sum





print(find_missing([3, 7, 1, 2, 8, 4, 5]))