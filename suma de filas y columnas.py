
matriz=[
    [3, 8, 5, 9, 3],
    [7, 5, 3, 8, 7],
    [1, 4, 7, 5, 5],
    [9, 1, 4, 9, 3],
    [6, 9, 6, 2, 2],
    ]
print(matriz)

columna=[]
def columnas(matriz):
    for i in range(0,5):
        col1=[row[0] for row in matriz]  #recoge la primera columna de cada fila de la matriz
        columna.append(col1)
    print(columna)

    

columnas(matriz)



