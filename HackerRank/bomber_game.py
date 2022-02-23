import os







def bomberMan2(n, grid):

    org_n = n

    for i in range(len(grid)):
        grid[i] = list(grid[i])
        for j in range(len(grid[i])):
            if grid[i][j] == "O":
                grid[i][j] = 3
            if grid[i][j] == ".":
                grid[i][j] = 0

                
    while(n != 0):

        just_exploded = set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):

                if not (i, j) in just_exploded:
                    if grid[i][j] == 0 and org_n != n:
                        grid[i][j] = 3
                    elif grid[i][j] == 1:
                        grid[i][j] = 0
                        just_exploded.add((i,j))
                        if i + 1 < len(grid) and grid[i + 1][j] != 1:
                            grid[i + 1][j] = 0
                            just_exploded.add((i + 1, j))
                        if i - 1 > -1 and grid[i - 1][j] != 1:
                            grid[i - 1][j] = 0
                            just_exploded.add((i - 1, j))
                        if j + 1 < len(grid[i]) and grid[i][j + 1] != 1:
                            grid[i][j + 1] = 0
                            just_exploded.add((i, j + 1))
                        if j - 1 > -1 and grid[i][j - 1] != 1:
                            grid[i][j - 1] = 0
                            just_exploded.add((i, j - 1))
                        
                    elif grid[i][j] > 0:
                        grid[i][j] -= 1

        for row in grid:
            string = ""
            for num in row:
                if num > 0:
                    string += "O"
                else:
                    string += "."
            print(string)
        print("="*50)
        n -= 1

    res_grid = []
    for row in grid:
        string = ""
        for num in row:
            if num > 0:
                string += "O"
            else:
                string += "."
        res_grid.append(string)
    return(res_grid)

    

    

        
def flipped(grid):

    res_grid = []
    for i in range(len(grid)):
        string = ""
        for j in range(len(grid[i])):
            if (grid[i][j] == "O") or (i + 1 < len(grid) and grid[i + 1][j] == "O") or (grid[i - 1][j] == "O" and i - 1 > -1)  or (j + 1 < len(grid[i]) and grid[i][j + 1] == "O") or (grid[i][j - 1] == "O" and j - 1 > -1):
                string +=  "."
            else:
                string += "O"
        res_grid.append(string)
    return res_grid  

def fill_up(grid):
    res_grid = []
    for i in range(len(grid)):
        res_grid.append("O" * len(grid[i]))
    return res_grid      



def bomberMan(n, grid):
    if n ==1:
        return grid
    elif (n - 1) % 4 ==0:
        res = flipped(grid)
        return flipped(res)
    elif n % 2 ==0:
        return fill_up(grid)
    return(flipped(grid))




#print(bomberMan2(3, ["...", ".O.", "..."]))


#print(bomberMan2(3, [".......", "...O...", "....O..", ".......", "OO.....", "OO....."]))


#print(bomberMan(12, [".......", "...O.O.", "....O..", "..O....", "OO...OO", "OO.O..."]))


print("Second iteration:")
#res = bomberMan2(5, [".......", "...O.O.", "....O..", "..O....", "OO...OO", "OO.O..."])







#print(flipped( [".......", "...O...", "....O..", ".......", "OO.....", "OO....."]))





    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()

    


