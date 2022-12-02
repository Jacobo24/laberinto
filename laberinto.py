def laberinto(tamaño, limite):
    laberinto = []
    for i in range(tamaño):
        fila = []
        for j in range(tamaño):
            if tuple([i, j]) in limite:
                fila.append('X')
            else:
                fila.append(' ')
        laberinto.append(fila)
    return laberinto

