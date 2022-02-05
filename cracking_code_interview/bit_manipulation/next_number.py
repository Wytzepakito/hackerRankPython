
def get_bit(num, offset):
    val = 1 << offset
    return num & val != 0


def next_larger(indices):
    copy = []
    for num in indices:
        copy.append(num)
    first = copy[0]
    i = 0

    while(first == copy[i]):
        first += 1
        i += 1
    copy[0] = first
    return copy


def next_smaller(indices):
    copy = []
    for num in indices:
        copy.append(num)

    first = copy[0]
    i = 0

    while(first == copy[i]):
        first += 1 
        i += 1
    copy[i] = first
    return copy


def num_with_indices(indices):
    result = 0

    for ind in indices:
        result = result | (1 << ind)
    return result






def next_number(num):

    indices = []
    for i in range(32):
        if get_bit(num, i):
            indices.append(i)

    next_small = next_smaller(indices)
    
    next_large = next_larger(indices)
    print(num_with_indices(next_small))

    
    print(num_with_indices(next_large))


#print(next_smaller([0, 1, 2,  4, 5, 6, 7]))

next_number(1775)



    
