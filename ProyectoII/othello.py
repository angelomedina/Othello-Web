# 0: null
# 1: white
# 2: black

#grid 8x8

grid = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 2, 0, 0, 0],
        [0, 0, 0, 2, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]
      ];

#coloca las fichas en la matriz
def selectCell(row,col,player):
    #validacion verifica que el moviemotno en filas y columnas en valido
    valicion = invalido(row,col)
    if(valicion == True):
        #si la fila, columna esta vacia coloca el valor dej jugador
        if ((player==1) and (grid[row][col]==0)):
            grid[row][col] = 1
            #envia a las posibles jugadas
            isValid(row, col,player)
            return "OK"
        elif((player==2) and (grid[row][col]==0)):
            grid[row][col] = 2
            isValid(row, col,player)
            return "OK"
    else:
        return "Movimiento Invalido: turno perdido"

#redirecciona a los posibles movimientos
def isValid(row,col,player):
     horizontal(row,col,player)
     vertical(row, col, player)
     diagonal(row, col, player)

#verifica las jugadas horizontales
def horizontal(row,col,player):
        lenG = lenGrid()
        #DERECHA
        if(row<=lenG-1 and col<=lenG-1):
            if(player==1):
                #dere
                if (col+1 <= lenG-1):
                    if(grid[row][col+1]==2):
                        grid[row][col+1] = 1
                        horizontal(row, col+1, player)
                else:
                    if (grid[row][col] == 2):
                        grid[row][col] = 1
                        horizontal(row, col, player)

            if (player == 2):
                #dere
                if (col+1 <= lenG-1):
                    if (grid[row][col+1] == 1):
                        grid[row][col+1] = 2
                        horizontal(row, col+1, player)
                else:
                    if (grid[row][col] == 1):
                        grid[row][col] = 2
                        horizontal(row,col, player)
        #IZQUIERDA
        if(row>=0 and col>=0):
            if(player==1):
                #izq
                if (col-1 >= 0):
                    if(grid[row][col-1]==2):
                        grid[row][col-1] = 1
                        horizontal(row, col-1, player)
                else:
                    if (grid[row][col] == 2):
                        grid[row][col] = 1
                        horizontal(row, col, player)
            if (player == 2):
                #izq
                if(col-1 >= 0):
                    if (grid[row][col-1] == 1):
                        grid[row][col-1] = 2
                        horizontal(row, col-1, player)
                else:
                    if (grid[row][col] == 1):
                        grid[row][col] = 2
                        horizontal(row,col, player)

#verifica las jugadas verticales
def vertical(row,col,player):
    lenG=lenGrid()
    #ARRIBA
    if(row>= 0 and col>=0 ):
        up=grid[row-1][col]
        if (player == 1):
            if (up == 2):
                grid[row-1][col] = 1
                vertical(row-1,col, player)
        if (player == 2):
            if (up == 1):
                grid[row-1][col] = 2
                vertical(row-1, col, player)
    #ABAJO
    if(row <= lenG-1 and col <= lenG-1):
        if(row+1 <= lenG-1):
            dow=grid[row+1][col]
            if (player == 1):
                if (dow == 2):
                    grid[row+1][col] = 1
                    vertical(row+1,col, player)
            if (player == 2):
                if (dow == 1):
                    grid[row+1][col] = 2
                    vertical(row+1,col, player)
        else:
            actual = grid[row][col]
            if (player == 1):
                    if (actual == 2):
                        grid[row][col] = 1
                        vertical(row, col, player)
            if (player == 2):
                if (actual == 1):
                    grid[row][col] = 2
                    vertical(row, col, player)

#verifica las jugadas diagonales
def diagonal(row,col,player):
    lenG = lenGrid()
    if (player == 1):
        #upDer
        if (row >= 0 and col >= 0):
            if(row-1 >= 0 and col+1 <= lenG-1):
                    upDer = grid[row - 1][col + 1]
                    if (upDer  == 2):
                        grid[row-1][col+1] = 1
                        diagonal(row-1,col+1,player)
        #upIzq
        if (row >= 0 and col >= 0):
            if (row-1>= 0 and col-1>=0):
                upIzq = grid[row-1][col-1]
                if (upIzq == 2):
                    grid[row-1][col-1] = 1
                    diagonal(row-1,col-1,player)
        #dowDer
        if (row <= lenG - 1 and col <= lenG - 1):
            if (row+1<= lenG-1 and col+1 <= lenG-1):
                dowDer = grid[row+1][col+1]
                if (dowDer == 2):
                    grid[row+1][col+1] = 1
                    diagonal(row+1,col+1,player)


        #dowIzq
        if (row <= lenG - 1 and col <= lenG - 1):
            if (row + 1 <= lenG-1 and col - 1 >= 0):
                dowIzq = grid[row + 1][col - 1]
                if (dowIzq == 2):
                    grid[row+1][col-1] = 1
                    diagonal(row+1,col-1,player)

    if (player == 2):
        #upDer
        if (row >= 0 and col >= 0):
            if(row-1 >= 0 and col+1 <= lenG-1):
                    upDer = grid[row - 1][col + 1]
                    if (upDer  == 1):
                        grid[row-1][col+1] = 2
                        diagonal(row-1,col+1,player)
        #upIzq
        if (row >= 0 and col >= 0):
            if (row-1>= 0 and col-1>=0):
                upIzq = grid[row-1][col-1]
                if (upIzq == 1):
                    grid[row-1][col-1] = 2
                    diagonal(row-1,col-1,player)
        #dowDer
        if (row <= lenG - 1 and col <= lenG - 1):
            if (row+1<= lenG-1 and col+1 <= lenG-1):
                dowDer = grid[row+1][col+1]
                if (dowDer == 1):
                    grid[row+1][col+1] = 2
                    diagonal(row+1,col+1,player)


        #dowIzq
        if (row <= lenG - 1 and col <= lenG - 1):
            if (row + 1 <= lenG-1 and col - 1 >= 0):
                dowIzq = grid[row + 1][col - 1]
                if (dowIzq == 1):
                    grid[row+1][col-1] = 2
                    diagonal(row+1,col-1,player)

#verifica que alcolocar la pieza lo haga solo en cuando hay otra pieza cerca
def invalido(row,col):
    lenG=lenGrid()
    #de abajo hacia arriba
    if (row >= 0):
        if(row-1 >= 0):
            if(grid[row-1][col]!=0 ):
                return True
    #de arriba hacia abajo
    if(row <= lenG-1):
        if(row+1 <= lenG-1):
            if(grid[row+1][col]):
                return True
    #de izquierda hacia derecha
    if(col <= lenG-1):
        if(col+1 <= lenG-1):
            if(grid[row][col+1] != 0):
                return True
    #de derecha hacia izquierda
    if(col >= 0):
        if(col-1 >= 0):
            if(grid[row][col-1] != 0):
                return True
    #de diagonal hacia arriba: derecha --> arriba
    if(row >= 0 and col >= 0):
        if(row-1 >= 0 and col-1 >= 0):
            if(grid[row-1][col-1] != 0):
                return True
    #de diagonal hacia abajo: izquierda --> abajo
    if (row <= lenG-1 and col  <= lenG-1):
        if (row + 1 <= lenG-1 and col + 1 <= lenG-1):
             if (grid[row + 1][col + 1] != 0):
                return True
    #de diagonal abajo hacia arriba: izquierda --> arriba
    if (row >= 0 and col <= lenG - 1):
          if (row - 1 >=  0 and col + 1 <= lenG - 1):
              if (grid[row - 1][col + 1] != 0):
                  return True

    #de diagonal arriba hacia abajo: derecha --> abajo
    if (row <= lenG-1 and col >= 0):
             if (row + 1 <= lenG-1 and col - 1 >= 0):
                 if (grid[row + 1][col - 1] != 0):
                     return True

#devuelve el lenght de la matriz
def lenGrid():
    cont=0
    for x in grid:
        cont+=1
    return cont





