import random

#def mostrar_matriz(matriz):

    #for fila in range(11):
      #for columna in range(11):
        #print(matriz[fila][columna], end = " ")
      #print()

def aleatorio_vertical_horizontal():

  lista = [1,2]

  x = random.choice(lista)

  return x

class Juego():

  def __init__(self,disparos,puntos,aciertos,no_aciertos,disparos_repetidos):

    self.disparos = disparos
    self.puntos = puntos
    self.aciertos = aciertos
    self.no_aciertos = no_aciertos
    self.disparos_repetidos = disparos_repetidos
    
  def mostrar_tablero(self,matriz):

    for fila in range(11):
      for columna in range(11):
        print(matriz[fila][columna], end = " ")
      print()
  
  def registrar_datos_partida(self):
    with open("Base_Datos_Juego.txt", "a+") as jugador: 
      jugador.write("{},{},{},{},{}\n".format(self.disparos,self.puntos,self.aciertos,self.no_aciertos,self.disparos_repetidos))

class Submarino(Juego):

  capacidad = "Tiene la capacidad de poder sumergirse y emerger del agua"

  def __init__(self,disparos,puntos,aciertos,no_aciertos,disparos_repetidos,estado):

    self.estado = estado
    
    super().__init__(disparos,puntos,aciertos,no_aciertos,disparos_repetidos)

  def mostrar_info(self):
    print("""
    <<<<<< SUBMARINO >>>>>>
    CAPACIDAD: {}
    ESTADO: {}
    """.format(Submarino.capacidad,self.estado))

  def colocar_submarinos(self):

    rango = [i+1 for i in range(10)]

    posiciones_x = tuple(random.sample(rango,k=4))
    posiciones_y = tuple(random.sample(rango,k=4))

    posiciones_x_y = tuple(zip(posiciones_x,posiciones_y))

    #for x,y in posiciones_x_y:
    #  matriz[x][y] = "♦♦"
    
    #mostrar_tablero(matriz)

    #print(posiciones_x_y)

    return posiciones_x_y

class Buque2(Juego):

  capacidad = "Tiene la capacidad de comunicarse con tierra y los otros miembros de la flota"

  def __init__(self,disparos,puntos,aciertos,no_aciertos,disparos_repetidos,estado):

    self.estado = estado

    super().__init__(disparos,puntos,aciertos,no_aciertos,disparos_repetidos)
  
  def mostrar_info(self):
    print("""
    <<<<<< BUQUE CORTO >>>>>>
    CAPACIDAD: {}
    ESTADO: {}
    """.format(Buque2.capacidad,self.estado))

  def colocar_buque2(self):

    rango = [i+1 for i in range(10)]
    
    v_h = aleatorio_vertical_horizontal()
    
    #print(v_h)
    
    if v_h == 1:

      posiciones_x = random.choice(rango)
      posiciones_y = random.choice(rango)

      if posiciones_y == 10:
        primera_posicion = (posiciones_x,posiciones_y)
        segunda_posicion = (posiciones_x,posiciones_y-1)
      else:
        primera_posicion = (posiciones_x,posiciones_y)
        segunda_posicion = (posiciones_x,posiciones_y+1)

      posiciones_x_y = (primera_posicion,segunda_posicion)

      #for x,y in posiciones_x_y:
      # matriz[x][y] = "♦♦"
    
      #mostrar_tablero(matriz)

      #print(posiciones_x_y)

      return posiciones_x_y

    elif v_h == 2:

      posiciones_y = random.choice(rango)
      posiciones_x = random.choice(rango)

      if posiciones_x == 10:
        primera_posicion = (posiciones_x,posiciones_y)
        segunda_posicion = (posiciones_x-1,posiciones_y)
      else:
        primera_posicion = (posiciones_x,posiciones_y)
        segunda_posicion = (posiciones_x+1,posiciones_y)

        #print(primera_posicion,segunda_posicion)

      posiciones_x_y = (primera_posicion,segunda_posicion)

      #for x,y in posiciones_x_y:
        #matriz[x][y] = "♦♦"
    
      #mostrar_tablero(matriz)

      #print(posiciones_x_y)

      return posiciones_x_y

class Buque3(Juego):

  capacidad = "Aterrizar helicópteros en él para el transporte de tropas"

  def __init__(self,disparos,puntos,aciertos,no_aciertos,disparos_repetidos,estado):

    self.estado = estado

    super().__init__(disparos,puntos,aciertos,no_aciertos,disparos_repetidos)
  
  def mostrar_info(self):
    print("""
    <<<<<< BUQUE LARGO >>>>>>
    CAPACIDAD: {}
    ESTADO: {}
    """.format(Buque3.capacidad,self.estado))

  def colocar_buque3(self):

    rango = [i+1 for i in range(10)]

    v_h = aleatorio_vertical_horizontal()
    
    #print(v_h)

    if v_h == 1:

      posiciones_x = random.choice(rango)
      posiciones_y = random.choice(rango)

      if posiciones_y == 10:
        primera_posicion = (posiciones_x,posiciones_y)
        segunda_posicion = (posiciones_x,posiciones_y-1)
        tercera_posicion = (posiciones_x,posiciones_y-2)
      elif posiciones_y == 9:
        primera_posicion = (posiciones_x,posiciones_y)
        segunda_posicion = (posiciones_x,posiciones_y-1)
        tercera_posicion = (posiciones_x,posiciones_y-2)
      else:
        primera_posicion = (posiciones_x,posiciones_y)
        segunda_posicion = (posiciones_x,posiciones_y+1)
        tercera_posicion = (posiciones_x,posiciones_y+2)

      posiciones_x_y = (primera_posicion,segunda_posicion,tercera_posicion)

      #for x,y in posiciones_x_y:
        #matriz[x][y] = "♦♦"
    
      #mostrar_tablero(matriz)

      #print(posiciones_x_y)

      return posiciones_x_y

    elif v_h == 2:

      posiciones_x = random.choice(rango)
      posiciones_y = random.choice(rango)

      if posiciones_x == 10:
        primera_posicion = (posiciones_x,posiciones_y)
        segunda_posicion = (posiciones_x-1,posiciones_y)
        tercera_posicion = (posiciones_x-2,posiciones_y)
      elif posiciones_x == 9:
        primera_posicion = (posiciones_x,posiciones_y)
        segunda_posicion = (posiciones_x-1,posiciones_y)
        tercera_posicion = (posiciones_x-2,posiciones_y)
      else:
        primera_posicion = (posiciones_x,posiciones_y)
        segunda_posicion = (posiciones_x+1,posiciones_y)
        tercera_posicion = (posiciones_x+2,posiciones_y)

      posiciones_x_y = (primera_posicion,segunda_posicion,tercera_posicion)

      #for x,y in posiciones_x_y:
        #matriz[x][y] = "♦♦"
    
      #mostrar_tablero(matriz)

      #print(posiciones_x_y)

      return posiciones_x_y 

