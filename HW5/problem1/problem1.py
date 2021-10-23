def transpose(matrix):
    t = []
    for j in range(len(matrix[0])):
        rows = []
        for i in range(len(matrix)):
           rows.append(matrix[i][j])
        t.append(rows)
    return t