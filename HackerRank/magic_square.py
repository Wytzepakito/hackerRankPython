

def flip_square(s):

    res_mat = [[] * len(s)] * len(s)

    first_row = s[0]
    second_row = s[1]
    third_row = s[2]

    for i in range(len(s)):
        res_mat[i] = [third_row[i], second_row[i], first_row[i]]

        

    return res_mat

def transform_square(s):
    
    res = []  
    for i in range(len(s)):
        row = s[i][::-1]

        res.append(row)
    return(res)

def get_score(s, magic):
    score = 0

    for i in range(len(s)):
        for j in range(len(s)):
            score += abs(magic[i][j] - s[i][j])
    return(score)





def formingMagicSquare(s):

    magic_square = [[8, 1, 6], [3, 5, 7], [4, 9, 2]]
    score = 99999999

    for i in range(4):
        magic_square = flip_square(magic_square)
        score_1 = get_score(s, magic_square)
        if score > score_1:
            score = score_1

        transformed = transform_square(magic_square)
        score_2 = get_score(s, transformed)
        if score > score_2:
            score = score_2

    return score



    


print(formingMagicSquare([[5, 3, 4], [1, 5, 8], [6, 4, 2]] ))


print(formingMagicSquare([[4, 9, 2], [3, 5, 7], [8, 1, 5]]))