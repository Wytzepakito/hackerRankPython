
import math


def has_bit(num, offset):
    val = 1 << offset
    return val & num != 0




def get_sub_arrs(arr):
    sub_arrs = []

    for i in range(len(arr)):
        low_bound = 0
        high_bound = i + 1
        while( high_bound <= len(arr)):

            sub_arrs.append(arr[low_bound:high_bound])
            low_bound += 1
            high_bound += 1

    return sub_arrs





def print_sub_arr_sum_zero(arr):

    sub_arrs = get_sub_arrs(arr)

    for sub_arr in sub_arrs:
        if sum(sub_arr) == 0:
            print(sub_arr)













print_sub_arr_sum_zero([6, 3, -1, -3, 4, -2, 2, 4, 6, -12, -7])




