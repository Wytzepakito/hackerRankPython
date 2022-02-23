

def flippingMatrix(matrix):
    score_mat_size = int(len(matrix)/ 2)
    final_score = 0
    mat_size = len(matrix) -1

    for ii in range(score_mat_size):
        for jj in range(score_mat_size):
            possibities = [matrix[ii][jj], matrix[ii][mat_size-jj], matrix[mat_size-ii][jj], matrix[mat_size-ii][mat_size-jj]]
            final_score += max(possibities)
    return final_score
        
            

        





mat = [[112, 42, 114, 119], [56, 125, 101, 49], [15, 78, 56, 43], [62, 98, 83, 108]]

print(flippingMatrix(mat))