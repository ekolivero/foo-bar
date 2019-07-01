# I use this function for creating the dataset

def solution(start, lenght):
    dataSet = createDataset(start, lenght)
    mat = createMatrix(lenght, lenght, dataSet)
    matrice = []
    for x in range(len(mat)):
        temp = (mat[x].index('/'))
        matrice.append(mat[x][:temp])


    flat_list = [item for sublist in matrice for item in sublist]
    print(flat_list)

    result = reduce(lambda a,b : a^b, flat_list)
    return result


def createDataset(start, lenght):
    rowCount = lenght + 1
    columnCount = lenght
    totalCount = rowCount * columnCount
    dataSet = []
    for i in range(totalCount):
        dataSet.append(start + i)
    return dataSet


def createMatrix(rowCount, colCount, dataSet):
    mat = []
    for i in range(rowCount):
        rowList = []
        _temp = colCount - i
        for j in range(colCount+1):
            if j == _temp:
                rowList.append('/')
                # the rest after checkpoint doesn't matter anymore for this problem.
                break
            else:
                rowList.append(dataSet[rowCount * i + j])
        mat.append(rowList)

    return mat

