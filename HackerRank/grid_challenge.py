


def gridChallenge(grid):
    # Write your code here
    
    current_row_ind = 0
    next_row_ind = 1
    while(next_row_ind < len(grid)):
        
        current_row = [ord(letter) for letter in grid[current_row_ind]]
        next_row = [ord(letter) for letter in grid[next_row_ind]]
        current_row.sort()
        next_row.sort()
        for cur,nex in zip(current_row, next_row):
            if cur > nex:
                print("NO")
                return

        current_row_ind += 1
        next_row_ind += 1
    print("YES")
    return
         
         
         























gridChallenge(["abc","ade", "efg"])

gridChallenge(['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv'])
