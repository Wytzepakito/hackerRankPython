


def getWays(n,c):
    c.sort()

    vector = [0] * (n + 1) 
    vector[0] = 1

    for coin in c:

        for i in range(coin, n + 1):
            vector[i] += vector[i - coin]

    return(vector[len(vector) - 1])




print(getWays(3, [8, 3, 1, 2]))