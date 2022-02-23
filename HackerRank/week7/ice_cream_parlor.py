


def icecreamParlor(m, arr):

    dic = {}

    for i,price in enumerate(arr):
        needed = m - price
        if needed in dic:
            return [dic[needed], i + 1]
        else:
            dic[price] = i + 1
