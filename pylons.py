



def pylons(k, arr):
    # Write your code here
    arr_ind = 0

    power_spots = []
    while(arr_ind != len(arr)):
        print(power_spots)
        if arr[arr_ind] == 0:
            if arr_ind == (len(arr) - 1):
                last = power_spots[-1]
                if arr_ind - last >= k + 1:
                    return(-1)
                else:
                    return(len(power_spots))
            else:
                arr_ind+=1
        if arr[arr_ind] == 1:
            if power_spots:
                last = power_spots[-1]
                if arr_ind - last == k + 1:
                    power_spots.append(arr_ind)
                    arr_ind += 1
                elif arr_ind - last < k + 1:
                    arr_ind += 1
                else:
                    return(-1)
            else:
                # Start of powergrid 
                if arr_ind == k:
                    return(-1)
                else:
                    power_spots.append(arr_ind)
                    arr_ind += 1

    return(len(power_spots))


def rindex(lst, value):
    lst.reverse()
    i = lst.index(value)
    lst.reverse()
    return len(lst) - i - 1



def pylons2(k, arr):

    current_coverage = -1
    pylons = 0

    while (current_coverage + 1 + k - 1) < len(arr):
        if current_coverage == -1:
            if 1 in arr[:k]:
                current_coverage = rindex(arr[:k], 1)
                pylons += 1
            else:
                return(-1)

        else:
            begin = current_coverage + 1
            end = current_coverage + 1 + (k -1) *2 + 1
            print(f"{begin =}, {end =}")
            if 1 in arr[current_coverage +1: end]:
                current_coverage = rindex(arr[begin: end], 1) + begin
                pylons += 1
            else:
                return(-1)
    return(pylons)



print(pylons2(2, [0, 1, 1, 1, 1, 0]))


print(pylons2(3, [0, 1, 1, 1, 0, 0, 0]))


# arr2 = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# print(rindex(arr2[:20], 1))

# print(rindex(arr2[30:68], 1))

# #print(rindex(arr2[86:], 1))

print(pylons2(20,[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))