


def get_bit(num, offset):
    val = 1 << offset
    return num & val != 0
    


def flip_bit(num, offset):
    val =  1 << offset
    return num | val



def get_longest_seq(num):
    longest_seq = 0
    current_count =0
    for i in range(32):
        if get_bit(num, i):
            current_count += 1
        else:
            if current_count > longest_seq:
                longest_seq = current_count
                current_count = 0
    return longest_seq
        


def longest_seq_with_bit_flip(num):

    bits_to_flip = []
    for i in range(32):
        if get_bit(~num, i):
            bits_to_flip.append(i)
    longest_seq = 0
    for bit in bits_to_flip:
        flipped_num = flip_bit(num, bit)
        long_seq = get_longest_seq(flipped_num)
        if longest_seq < long_seq:
            longest_seq = long_seq

    return longest_seq



print(longest_seq_with_bit_flip(1775))