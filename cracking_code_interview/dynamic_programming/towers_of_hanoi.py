

def get_place(stacks, piece, current):
    if current != 2 and (len(stacks[2]) == 0 or stacks[2][0] > piece):
        return 2
    if current != 1 and (len(stacks[1]) == 0 or stacks[1][0] > piece):
        return 1
    if current != 0  and (len(stacks[0]) == 0 or stacks[0][0] > piece):
        return 0
    else:
        return -1
    
def tower_of_hanoi(stacks,n, from_, to_, buf_):
    
    if n ==1:
        piece = stacks[from_].pop(0)
        stacks[to_].insert(0, piece)
    else:
        tower_of_hanoi(stacks,n - 1, from_, buf_, to_)
        piece = stacks[from_].pop(0)
        stacks[to_].insert(0, piece)
        tower_of_hanoi(stacks,n - 1, buf_, to_, from_)
    print(stacks)



def solve_towers(stacks):
    n = len(stacks[0])

    tower_of_hanoi(stacks,n, 0, 2, 1)
    print(stacks)










stacks = [[1, 2, 3, 4, 5, 6, 7, 8], [], []]

solve_towers(stacks)