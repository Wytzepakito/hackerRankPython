




def bubble_sort(array):

    had_swap = True
    offset = False
    even = True
    if len(array) % 2 != 0:
        even = False
    even_offset = None


    while(had_swap == True):
        if even:
            even_offset = offset
        else:
            even_offset = not offset

        had_swap = False
        for i in range(0 + offset, len(array)- even_offset , 2):
            if array[i] > array[i + 1]:
                had_swap = True
                temp = array[i + 1]
                array[i + 1] = array[i]
                array[i] = temp
        offset = not offset
        
    print(array)





















print(bubble_sort([2, 1, 7, 5, 4, 6, 3]))

print(bubble_sort([2, 1, 7, 5, 4, 6, 3, 1]))
