
import math


def cross_off(bit_map, prime):

    for i in range(prime * prime, len(bit_map), prime):
        bit_map[i] = False

def get_next(bit_map, prime):
    start = prime + 1
    for i in range(start, len(bit_map)):
        if bit_map[i]:
            return i
def seave(max):

    bit_map = [True] * max
    bit_map[0] = False
    bit_map[1] = False

    prime = 2

    while(prime <= math.sqrt(max)):
        cross_off(bit_map, prime)

        prime = get_next(bit_map, prime)
    return bit_map




bit_map = seave(1000)

for i in range(len(bit_map)):
    if bit_map[i]:
        print(i)