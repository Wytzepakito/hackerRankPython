


# def binary_search(num, arr, low, high):



#     while (low <= high):

#         mid = low +  ((high - low) // 2)

#         if arr[mid] > num:
#             low = mid + 1
#         else:



import os






def get_number_of_ranks(ranked):

    index = 0
    position = 1
    while(index < len(ranked)):
        if index > 0:
            if ranked[index - 1] > ranked[index]:
                position += 1

        index += 1

    return position


def get_front_ranking(ranked, num):
    index = 0
    position = 1

    while(index < len(ranked) and ranked[index] > num):
        if index > 0:
            if ranked[index - 1] > ranked[index]:
                position += 1

        index += 1
    if index == 0:
        return position
    else:
        return position + 1


def get_back_ranking(ranked, num, number_of_ranks):

    position = number_of_ranks
    index = len(ranked) - 1
    while(ranked[index] < num):
        if index != len(ranked) -1:
            if ranked[index] > ranked[index + 1]:
                position -= 1

        index -= 1

    if index == len(ranked) - 1:
        return position + 1
    else:
        return position
    

def climbingLeaderboard(ranked, player):

    new_pos = []

    mid = ranked[len(ranked) // 2]

    number_of_ranks = get_number_of_ranks(ranked)

    for num in player:

        if mid < num:
            position = get_front_ranking(ranked, num)
        else:
            position = get_back_ranking(ranked, num, number_of_ranks)

        new_pos.append(position)
    return new_pos
            





def climbingLeaderboard2(ranked, player):

    index = 0
    position = 1
    num = player.pop()
    new_pos = []
    while(index <= len(ranked) - 1 and num != None):
        if index > 0:
            if ranked[index - 1] > ranked[index]:
                position += 1

        if num >= ranked[index]:
            while(len(player) != 0 and num >= ranked[index]):

                new_pos.append(position)
                num = player.pop()

            if num >= ranked[index]:
                new_pos.append(position)
                num = None
                




        

    
        index += 1

    if num != None:
        
        new_pos.append(position +1)
        if len(player) > 0:
            for _ in player:
                new_pos.append(position + 1)

    return new_pos[::-1]



# print(climbingLeaderboard2([100, 100, 50, 40, 40, 20, 10], [5,5,25, 25, 35, 50, 120]))



# print(climbingLeaderboard2([100, 90, 90, 80, 75, 60], [50, 65, 77, 90, 102]))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard2(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    print("I am finish")
