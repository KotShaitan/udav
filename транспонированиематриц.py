def trans(матрица):
    матрица_массив=[[0]*len(матрица) for i in range(len(матрица[0]))]
    for i in range(len(матрица)):
        for j in range(len(матрица[0])):
            матрица_массив[j][i] = матрица[i][j]
    return матрица_массив
матрица=[[1, 2, 3],[4, 5, 6]]
print(trans(матрица))
