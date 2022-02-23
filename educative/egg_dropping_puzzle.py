
import math

def egg_drop(floors, eggs):
    if floors ==1 or floors ==0:
        return floors

    if eggs == 1:
        return floors

    min = math.inf


    for i in range(1,floors):

        # doesn't break, breaks

        res = max(egg_drop(floors - i, eggs), egg_drop(i - 1, eggs -1))
        print(f"{i = }, {res = }")
        if res < min:
            min = res
    return min + 1


def egg_drop2(floors, eggs):

    attempts = 0
    while(eggs != 1):
        eggs -= 1
        floors = floors -  (floors // 2)
        attempts += 1

    return floors + attempts





print(egg_drop(7, 3))
print(egg_drop2(7, 3))
