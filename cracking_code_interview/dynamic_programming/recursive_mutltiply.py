

def has_bit(num, bit_offset):
    val_with_offset = 1 << bit_offset

    return ((num & val_with_offset) != 0)

print(has_bit(3, 0))
print(has_bit(3, 1))
print(has_bit(3, 2))


def multiply(x, y):

    if x == 0  or y == 0:
        return 0

    if x < y:
        smaller = x
        larger = y
    else:
        smaller = y
        larger = x

    result = 0

    result = get_result(larger, smaller, 0, result)

    return result


def get_result(larger, smaller, count, result):
    if count == 32:
        return result

    if has_bit(smaller, count):
        print("Had bit")
        result += larger << count

    return get_result(larger, smaller, count + 1, result)






print(multiply(4,7))
print(multiply(500,3))


    

