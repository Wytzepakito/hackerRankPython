import itertools


def make_stack_len(stack, height):

    sum_stack = sum(stack)

    len_to_try = sum_stack - height

    for items_to_remove in range(0,len(stack)):
        sum_removed_items = sum(stack[:items_to_remove])
        if sum_stack - sum_removed_items == height:
            return True
        elif sum_stack - sum_removed_items < height:
            return False
        



    return False







def equalStacks(h1, h2, h3):
    stack_list = [h1, h2, h3]
    mini = min([sum(stack) for stack in stack_list])
    found = False

    while(found == False):

        found = True
        for stack in stack_list:
            if make_stack_len(stack, mini) == False:
                found = False
        if found == False:
            mini -= 1


    return mini



def equalStacks2(h1,h2,h3):
    sum_h1 = sum(h1)
    remove_h1 = 0

    sum_h2 = sum(h2)
    remove_h2 = 0

    sum_h3 = sum(h3)
    remove_h3 = 0

    equal = False

    while(equal == False):
        if sum_h1 == sum_h2 and sum_h1 == sum_h3:
            equal = True
        elif sum_h1 > sum_h2 and sum_h1 > sum_h3:
            sum_h1 = sum_h1 - h1[remove_h1]
            remove_h1 += 1
        elif sum_h2 > sum_h1 and sum_h2 > sum_h3:
            sum_h2 = sum_h2  - h2[remove_h2]
            remove_h2 += 1
        elif sum_h3 > sum_h1  and sum_h3 > sum_h1:
            sum_h3 = sum_h3 - h3[remove_h3]
            remove_h3 += 1
        elif sum_h1 == sum_h2 and sum_h1 > sum_h3:
            sum_h1 = sum_h1 - h1[remove_h1]
            remove_h1 += 1
            sum_h2 = sum_h2 - h2[remove_h2]
            remove_h2 += 1
        elif sum_h1 == sum_h3 and sum_h1 > sum_h2:
            sum_h1 = sum_h1 - h1[remove_h1]
            remove_h1 += 1
            sum_h3 = sum_h3 - h3[remove_h3]
            remove_h3 += 1
        elif sum_h2 == sum_h3 and sum_h2 > sum_h1:
            sum_h2 = sum_h2 - h2[remove_h2]
            remove_h2 += 1
            sum_h3 = sum_h3 - h3[remove_h3]
            remove_h3 += 1

    return sum_h1






print(equalStacks2([1, 2, 1, 1 ], [1, 1, 2], [1, 1]))



