





def flippingBits(n):
    # Write your code here

    byte = '{:032b}'.format(n)


    a = 0xFFFFFFFF

    new_bits = bin(n ^ a)
    return(int(new_bits, 2))

        




flippingBits(9)
