from Usuario import Usuario
from Juego import Juego
from Juego import Submarino
from Juego import Buque2
from Juego import Buque3
from Estadística import Estadistica

tablero = [
  ["♥","  1","  2","  3","  4","  5","  6","  7","  8","  9","  10"],
  [" 1","[O]","[O]","[O]","[O]","[O]","[O]","[O]","[O]","[O]","[O]"],
  [" 2","[O]","[O]","[O]","[O]","[O]","[O]","[O]","[O]","[O]","[O]"],
  [" 3","[O]","[O]","[O]","[O]","[O]","[O]","[O]","[O]","[O]","[O]"],
  [" 4","[O]","[O]","[O]","[O]","[O]","[O]","[O]","[O]","[O]","[O]"],
  [" 5","[O]","[O]","[O]","[O]","[O]","[O]","[O]","[O]","[O]","[O]"],
  [" 6","[O]","[O]","[O]","[O]","[O]","[O]","[O]","[O]","[O]","[O]"],
  [" 7","[O]","[O]","[O]","[O]","[O]","[O]","[O]","[O]","[O]","[O]"],
  [" 8","[O]","[O]","[O]","[O]","[O]","[O]","[O]","[O]","[O]","[O]"],
  [" 9","[O]","[O]","[O]","[O]","[O]","[O]","[O]","[O]","[O]","[O]"],
  ["10","[O]","[O]","[O]","[O]","[O]","[O]","[O]","[O]","[O]","[O]"]
  ]

def mostrar_top10():
  """
  FUNCIÓN QUE IMPRIME LOS 10 JUGADORES CON MEJOR PUNTUACIÓN DE LA BASE DE DATOS

  PRINT: 1 -> LUIS
         2 -> JOSE... 
  """
  pass

def usuarios_jugadores():
  """
  Función que calcula el rango de edades donde estan los usuarios que más juegan.

  RETURN: STRING CON EL RANGO DE EDADES

  """

  edades_nPartidas = []

  rango1 = []
  rango2 = []
  rango3 = []
  rango4 = []

  with open("Base_Datos.txt", "r") as info:
    jugadores = info.readlines()
  
  for jugador in jugadores:
    usuario = jugador[:-1].split(",")
    aux = int(usuario[2]),int(usuario[5]) 
    edades_nPartidas.append(aux)
  
  edades_nPartidas_tupla = tuple(edades_nPartidas)

  for x,y in edades_nPartidas_tupla:
    if x < 5:
      continue
    elif x >= 5 and x <= 18:
      rango1.append(y)
    elif x >= 19 and x <= 45:
      rango2.append(y)
    elif x >= 46 and x <= 60:
      rango3.append(y)
    elif x >= 61 and x <= 100:
      rango4.append(y)

  if sum(rango1) > sum(rango2) and sum(rango1) > sum(rango3) and sum(rango1) > sum(rango4):
    return "5-18"
  elif sum(rango2) > sum(rango1) and sum(rango2) > sum(rango3) and sum(rango2) > sum(rango4):
    return "19-45"
  elif sum(rango3) > sum(rango1) and sum(rango3) > sum(rango2) and sum(rango3) > sum(rango4):
    return "46-60"
  elif sum(rango4) > sum(rango1) and sum(rango4) > sum(rango2) and sum(rango4) > sum(rango3):
    return "61-100"
    

  #rangos de edades ([[5-18],[19-45],[46-60],[61-100]])

def puntosPorGenero():
  """
  Función que calcula el total de puntos que hay en la base de datos por género

  RETURN TUPLA CON AMBOS VALORES

  """

  punto_genero = []

  puntos_m = []
  puntos_f = []

  with open("Base_Datos.txt", "r") as info:
    jugadores = info.readlines()
  
  for jugador in jugadores:
    usuario = jugador[:-1].split(",")
    aux = usuario[3], int(usuario[4])
    punto_genero.append(aux)

  punto_genero_tupla = tuple(punto_genero)

  for x,y in punto_genero_tupla:

    if x == "Masculino":
      puntos_m.append(y)
    elif x == "Femenino":
      puntos_f.append(y)
    else:
      continue
  
  puntos_totales_m = sum(puntos_m)
  puntos_totales_f = sum(puntos_f)

  return puntos_totales_m,puntos_totales_f

def promedio_disparos_ganar():
  """
  FUNCIÓN QUE CALCULA EL PROMEDIO DE DISPAROS REALIZADOS PARA GANAR

  RETURN: VALOR DEL PROMEDIO

  """

  juegos = []

  with open("Base_datos_Juego.txt", "r") as info:
    juego = info.readlines()
  
  for punto in juego:
    usuario = punto[:-1].split(",") 
    juegos.append(int(usuario[0]))

  promedio_disparos = sum(juegos)//len(juegos)

  return promedio_disparos

def mostrar_usuarios():
  """
  FUNCIÓN QUE MUESTRA UNA LISTA DE LOS USUARIOS EN LA BASE DE DATOS

  PRINT: 1- HECTOR
         2- LUIS...
  """
  usuarios = []

  with open("Base_Datos.txt", "r") as info:
    jugadores = info.readlines()
  
  for jugador in jugadores:
    usuario = jugador[:-1].split(",") 
    usuarios.append(Usuario(usuario[0], usuario[1], usuario[2], usuario[3], int(usuario[4]), int(usuario[5])))

  for i,usuario in enumerate(usuarios):
    print("--> ",i+1, usuario.username)

def actualizar_info(seleccion):
  """
  FUNCIÓN QUE MUSTRA MENÚ DE LA INFORMACIÓN QUE EL USUARIO DESEE EDITAR

  INPUT: INDICE +1 DEL USUARIO REGISTRADO EN BASE DE DATOS

  """
  print("""

    ¿Que desea cambiar?

    1 - Username
    2 - Nombre
    3 - Edad
    4 - Género
    """)

  option  = input("Seleccione una opción: ")

  while not option.isdigit() or int(option) < 1 or int(option) > 4:
    option = input('Ingrese su opción correctamente: ')

  with open("Base_Datos.txt", 'r') as info:
    jugadores = info.readlines()
    usuario = jugadores[seleccion - 1][:-1].split(',')

  usuario[int(option) - 1] = input("Ingrese el nuevo valor: ")
  nuevo_valor = ""

  for i in range(len(usuario)):
    if i != len(usuario) -1:
      nuevo_valor += usuario[i] + ','
    else:
      nuevo_valor += usuario[i] + '\n'

  jugadores[seleccion - 1] = nuevo_valor
  with open("Base_Datos.txt", "w") as info:
    info.writelines(jugadores)
  
def verificar_usuario(username):
  """
  FUNCIÓN QUE VERIFICA SI UN USUARIO EXISTE EN BASE DE DATOS

  RETURN: TRUE SI EL USUARIO EXISTE

  RETURN: FALSE SI EL USUARIO NO EXISTE

  """
  try:
      
    with open("Base_Datos.txt","r") as info:
      jugadores = info.readlines()

    for jugador in jugadores:
      usuario = jugador[:-1].split(',') 
      if usuario[0] == username:
        return True
    return False
  except:
    print("Todavia no se ha registrado ningún usuario")
    return False

def buscar_jugador(username):
  """
  FUNCIÓN QUE BUSCA UN JUGADOR SI EXISTE EN LA BASE DE DATOS

  INPUT: NOMBRE DE USUARIO

  RETURN: USUARIO COMO OBJETO

  """

  with open("Base_Datos.txt", "r") as info:
        jugadores = info.readlines()

  for jugador in jugadores:
    usuario = jugador[:-1].split(',') 
    if usuario[0] == username:
      return Usuario(usuario[0], usuario[1], usuario[2], usuario[3], int(usuario[4]), int(usuario[5]))
  
def validar_posiciones(posiciones_sub,posiciones_buque2,posiciones_buque3):

  """
  FUNCIÓN QUE VERIFICA SI ALGÚN BARCO ESTA ABYACENTE A OTRO

  INPUT: POSICIONES DE TODOS LOS BARCOS EN TUPLAS

  RETURN: TRUE SI UN BARCO ESTA ABYACENTE A OTRO
  """

  #Validar repetidos. si solo 1 coordenada se repite crea nuevas coordenadas y las valida
  #print(posiciones_sub,posiciones_buque2,posiciones_buque3)

  for submarino in posiciones_sub:
    for pos_buque2 in posiciones_buque2:
        if (submarino in posiciones_buque2) or (submarino in posiciones_buque3):
            #print("a")
            return True
        elif pos_buque2 in posiciones_buque3:
            #print("a")
            return True
        else:
            #print("a")
            continue
    continue
          
  #valida si un submarino esta adyacente a un buque de 2
  #print("b")

  for x,y in posiciones_sub:
    for i,j in posiciones_buque2:

      if validar_alrededor(x,y,i,j) == True:
          #print("b")
          return True
          
      else:
          #print("b")
          continue
    continue
      
  # valida si un submarino esta adyacente a un buque de 3
  #print("c")
  for x,y in posiciones_sub:
    for i,j in posiciones_buque3:

      if validar_alrededor(x,y,i,j) == True:
          #print("c")
          return True
      else:
          #print("c")
          continue
    continue

  # valida si un buque 2 esta adyacente a un buque 3

  for x,y in posiciones_buque2:
    for i,j in posiciones_buque3:

        #print(x,y,i,j)
        
        if validar_alrededor(x,y,i,j) == True:
            #print("d")
            return True
        else:
            #print("d")
            continue
    continue
  
  # valida si un submarino esta adyacente a otro

  for submarino in posiciones_sub:
      for i in range(4):
        segundo_submarino = posiciones_sub[i]
        x = submarino[0]
        y  = submarino[1]
        i = segundo_submarino[0]
        j = segundo_submarino[1]
        if validar_alrededor(x,y,i,j) == True:
            return True
        else:
            continue
     
def validar_alrededor(x,y,i,j):
  """
  FUNCIÓN QUE VALIDA TODOS LOS CASOS SI DOS POSICIONES ESTAN ADYACENTE

  INPUT: X,Y -> POSICIONES DE PRIMER BARCO I,J -> POSICIONES DE SEGUNDO BARCO

  """

  # validar esquinas

  if x == 1 and y == 10:

    if (x == i and y-1 == j) or (x+1 == i and y-1 == j) or (x+1 == i and y == j):
      return True
    else:
      return False
        
  elif x == 1 and y == 1:

    if (x == i and y+1 == j) or (x+1 == i and y == j) or (x+1 == i and y+1 == j):
      return True
    else:
      return False
        
  elif x == 10 and y == 10:

    if (x-1 == i and y == j) or (x-1 == i and y-1 == j) or (x == i and y-1 == j):
      return True
    else:
      return False

  elif x == 10 and y == 1:

    if (x-1 == i and y == j) or (x-1 == i and y+1 == j) or (x == i and y+1 == j):
      return True
    else:
      return False

  #validar lados

  # lado superior

  elif y == 1 and x > 1:

    if (x-1 == i and y == j) or (x-1 == i and y+1 == j) or (x == i and y+1 == j) or (x+1 == i and y+1 == j) or (x+1 == i and y+1 == j) or (x+1 == i and y == j):
      return True
    else:
      return False

  # lado inferior

  elif y == 10 and x > 1:

    if (x-1 == i and y == j) or (x-1 == i and y-1 == j) or (x == i and y-1 == j) or (x+1 == i and y-1 == j) or (x+1 == i and y == j):
      return True
    else:
      return False

  #lado derecho

  elif x == 10 and y > 1:

    if (x == i and y-1 == j) or (x-1 == i and y-1 == j) or (x-1 == i and y == j) or (x-1 == i and y+1 == j) or (x == i and y+1 == j):
      return True
    else:
      return False

  #lado izquierdo

  elif x == 1 and y > 1:

    if (x == i and y-1 == j) or (x+1 == i and y-1 == j) or (x+1 == i and y == j) or (x+1 == i and y+1 == j) or (x == i and y+1 == j):
      return True
    else:
      return False  
  
  #todas las demas 60 posiciones

  elif x >= 2 and y >= 2:

    if (x-1 == i and y-1 == j) or (x == i and y-1 == j) or (x+1 == i and y-1 == j) or (x-1 == i and y == j) or (x+1 == i and y == j) or (x+1 == i and y+1 == j) or (x == i and y+1 == j) or (x-1 == i and y+1 == j):
      return True
    else:
      return False

def colocar_barcos(posicion_sub,posicion_buque2,posicion_buque3,objeto1,objeto2,objeto3):
  """
  FUNCIÓN QUE CREA LA FLOTA Y LA VALIDA

  INPUT: POSICIONES DE TODOS LOS BARCOS Y OBJETOS INSTACIADOS DE LA CLASE DEL RESPECTIVO BARCO

  RETURN: FLOTA ->  TUPLA CON LAS POSICIONES DE LOS BARCOS

  """
  while validar_posiciones(posicion_sub,posicion_buque2,posicion_buque3) == True:

    posicion_sub = objeto1.colocar_submarinos()
    posicion_buque2 = objeto2.colocar_buque2()
    posicion_buque3 = objeto3.colocar_buque3()

    validar_posiciones(posicion_sub,posicion_buque2,posicion_buque3)
      
  else:

    flota = posicion_sub,posicion_buque2,posicion_buque3

    #for barco in flota:
      #for x,y in barco:
        #matriz[x][y] = "♦♦"
    
      #mostrar_tablero(matriz)

    return flota

def mostrar_ultima_matriz(lista_disparos,tupla_barcos,objeto,matriz):
  """
  FUNCIÓN QUE IMPRIME LA ÚLTIMA MATRIZ CON LOS ACIERTOS Y DESACIERTOS

  INPUT: TODOS LOS DISPAROS DEL USUARIO, FLOTA, OBJETO(CLASS USUARIO), TABLERO

  PRINT: TABLERO MODIFICADO

  """

  for barco in tupla_barcos: # posiciones donde se disparó
    for x,y in barco:
      matriz[x][y] = "[F]"
  
  for barco in tupla_barcos:
    for i in barco:
      for disparo in lista_disparos:
        if i == disparo:
          lista_disparos.remove(i)
        else:
          continue
  
  aux = tuple(lista_disparos) # posiciones donde se disparó y no se acertó
  for x,y in aux:
    matriz[x][y] = "[X]"

  objeto.mostrar_tablero(matriz)

def evaluar_flota(flota,lista):
  """
  FUNCIÓN QUE DECIDE EL FIN DEL JUEGO. EVALUA SI YA LA FLOTA FUE DESTRUIDA

  INPUT: TUPLA DE POSICIONES DE LOS BARCOS, LISTA DE LOS DISPAROS REALIZADOS

  RETURN: CONTADOR QUE LLEVA LA CUENTA DE LAS POSICIONES IGUALES EN LA LISTA Y LA FLOTA
  SI ES 9 SE DETIENE EL JUEGO

  """

  contador = 0
  
  for disparo in lista:
    for barco in flota:
      if disparo in barco:
        contador += 1
      else:
        contador += 0

  if contador == 9:
    return contador
  else:
    return contador

def validar_disparo(disparo,lista):

  """
  FUNCIÓN QUE VALIDA SI UN DISPARO ES REPETIDO

  INPUT: DISPARO REALIZADO, LISTA DE LOS DISPAROS ANTERIORES

  RETURN: TRUE SI ES REPETIDO
          FALSE SI NO ES REPETIDO        
  """

  if len(lista) == 0:
    return False
  else:
    for i in lista:
      #print(i)
      if disparo == i:
        return True
      else:
        continue

    return False

def comprobar_acierto(posicion_disparo, flota):
  """
  FUNCIÓN QUE COMPRUEBA SI UN DISPARO FUE ACERTADO O NO.

  INPUT: DISPARO REALIZADO, POSICIONES DE LOS BARCOS

  RETURN: TRUE SI ES ACERTADO
          FALSE SI NO ES ACERTADO

  """

  if posicion_disparo in flota[0] or posicion_disparo in flota[1] or posicion_disparo in flota[2]:
    return True
  else:
    return False

def crear_new_usuario():

  """
  FUNCIÓN QUE SOLICITA INFORMACIÓN DE UN NUEVO JUGADOR

  SI SU NOMBRE DE USUARIO INGRESADO YA EXISTE INICIARÁ EL JUEGO

  RETURN: OBJETO INSTANCIADO EN LA CLASE USUARIO 
  """

  username = input("Ingrese su nombre de jugador (No debe: tener mas de 30 caracteres, tener espacios, tener letras mayusculas): ")

  #verificar si existe en el doc

  while len(username) > 30 or " " in username or not username.islower():
    username = input("Ingrese su nombre de jugador correctamente: ")

  if verificar_usuario(username):
    print("Este nombre de usuario ya existe.")

    usuario = buscar_jugador(username)

    play_juego(usuario)
    
  nombre = input("Ingrese su nombre completo: ")

  while nombre.isdigit() or len(nombre) < 1:
    nombre = input("Ingrese su nombre correctamente: ")

  edad = input("Ingrese su edad: ")

  while not edad.isdigit() or int(edad) < 1:
    edad = input('Ingrese su edad correctamente: ')

  genero = input("Seleccione su género. Masculino (M), Femenino (F): ")

  while genero.isdigit() or len(genero) > 1:
    genero = input("Seleccione su genero correctamente. Masculino (M), Femenino (F): ")

  if genero.upper() == "M":
    genero = "Masculino"
  elif genero.upper() == "F":
    genero = "Femenino"
  else:
    genero = "Desconocido"

  puntos_totales = 0

  partidas_jugadas = 0

  return Usuario(username,nombre,int(edad),genero,puntos_totales,partidas_jugadas)

def play_juego(objeto):

  """
  FUNCIÓN QUE CONTROLA EL DESARROLLO DEL JUEGO.

  INICIALIZA UN OBJETO(PARTIDA) DE LA CLASE JUEGO

  INPUT: OBJETO DE LA CLASE USUARIO
  """

  disparos = 0

  puntos = 0

  aciertos = 0

  no_aciertos = 0

  disparos_repetidos = 0

  objeto.partidas_jugadas += 1

  partida = Juego(disparos,puntos,aciertos,no_aciertos,disparos_repetidos)

  iniciar = True

  while iniciar:

    estado = "Activo"

    submarino = Submarino(disparos,puntos,aciertos,no_aciertos,disparos_repetidos,estado)
    buque2 = Buque2(disparos,puntos,aciertos,no_aciertos,disparos_repetidos,estado)
    buque3 = Buque3(disparos,puntos,aciertos,no_aciertos,disparos_repetidos,estado)

    posiciones_submarinos = submarino.colocar_submarinos()
    posiciones_buque2 = buque2.colocar_buque2()
    posiciones_buque3 = buque3.colocar_buque3()

    flota = colocar_barcos(posiciones_submarinos,posiciones_buque2,posiciones_buque3,submarino,buque2,buque3)

    todos_los_disparos = [] #guarda todos los disparos de la partida para no repetir, y se reinicia con la partida.

    #print(flota)
    #print(todos_los_disparos)
    #print("incio del juego\n")

    naves_destruidas = evaluar_flota(flota,todos_los_disparos)

    while naves_destruidas < 9:
      
      partida.mostrar_tablero(tablero)

      print("""
      PUNTUACIÓN: {} ------------- USUARIO: {} -------------- DISPAROS: {}
      """.format(partida.puntos,objeto.username,partida.disparos))

      print(flota)
     
      #print(todos_los_disparos)

      disparo_x = input("\nIngrese la coordenada x de su disparo: ")
      disparo_y = input("ingrese la coordenada y de su disparo: ")

      while not disparo_x.isdigit() or int(disparo_x) < 1 or int(disparo_x) > 10 or not disparo_y.isdigit() or int(disparo_y) < 1 or int(disparo_y) > 10:

        print("\n<<<<< HA OCURRIDO UN ERROR >>>>>\t \n")
        disparo_x = input("Ingrese la coordenada x de su disparo correctamente: ")
        disparo_y = input("ingrese la coordenada y de su disparo correctamente: ")
      
      disparo = int(disparo_x),int(disparo_y)

      #print(disparo)

      while validar_disparo(disparo,todos_los_disparos):

        disparos_repetidos += 1

        print("\n<<<<< DISPARO YA REALIZADO >>>>>\t \n")
        disparo_x = input("Ingrese la coordenada x (No repetida): ")
        disparo_y = input("Ingrese la coordenada y (No repetida): ")

        while not disparo_x.isdigit() or int(disparo_x) < 1 or int(disparo_x) > 10 or not disparo_y.isdigit() or int(disparo_y) < 1 or int(disparo_y) > 10:

          print("\n <<<<< HA OCURRIDO UN ERROR >>>>>\t \n")
          disparo_x = input("Ingrese la coordenada x de su disparo correctamente: ")
          disparo_y = input("ingrese la coordenada y de su disparo correctamente: ")
        
        disparo = int(disparo_x),int(disparo_y)

        validar_disparo(disparo,todos_los_disparos)

      else:

        todos_los_disparos.append(disparo)

        if comprobar_acierto(disparo,flota):

          partida.disparos += 1
          partida.puntos += 10
          partida.aciertos += 1

          print("<<<<< DISPARO EXITOSO >>>>>\t \n")

          #print(disparo)
    
        else:

          partida.disparos +=1

          if partida.puntos > 1:
            partida.puntos -= 2
          else:
            partida.puntos = 0
            
          partida.no_aciertos += 1

          print("<<<<< DISPARO ERRADO >>>>>\t \n")

      naves_destruidas = evaluar_flota(flota,todos_los_disparos)
  
    else:
      #todavia tengo las posiciones de los barcos de los aciertos y desaciertos

      submarino.estado = "DESTRUIDO"
      buque2.estado = "DESTRUIDO"
      buque3.estado = "DESTRUIDO"

      submarino.mostrar_info()
      buque2.mostrar_info()
      buque3.mostrar_info()

      if partida.disparos == 9:
        print("\t ¿Eres un Robot? lo que acabas de hacer es poco probable ….\n")
      elif partida.disparos < 45:
        print("\t Excelente Estrategia \n")
      elif partida.disparos >= 45 and partida.puntos <= 70:
        print("\t Buena Estrategia; pero hay que mejorar \n")
      elif partida.disparos > 70:
        print("\t Considérese Perdedor, tiene que mejorar notablemente \n")

      print("""

      USERNAME: {}
      CANTIDAD DE DISPAROS: {}
      DISPAROS REPETIDOS: {}
      PUNTOS TOTALES: {}
      \n
      """.format(objeto.username,partida.disparos,partida.disparos_repetidos,partida.puntos))

      mostrar_ultima_matriz(todos_los_disparos,flota,partida,tablero)

      option = (input("""
      HA SIDO MUY DIVERTIDO! 

      ¿DESEAS SEGUIR JUGANDO? 

        [1] --> Si
        [2] --> No
      """))

      while not option.isdigit() or int(option) < 1 or int(option) > 2:
        option = input('Ingrese su opción correctamente: ')
      
      if option == "1":

        partida.registrar_datos_partida()

        objeto.puntos_totales = partida.puntos

        objeto.registrar_base_datos()

        play_juego(objeto)

      elif option == "2":

        partida.registrar_datos_partida()

        objeto.registrar_base_datos()

        main()

def main():

  """
  FUNCIÓN DE CONTROL PRINCIPAL.

  MUESTRA EL MENU DE INICIO
  """

  inicio = True 

  while inicio:

    menu = input("""

    \t<<<<<<<<<<<-- ♦ SAMAN GAMES ♦ -->>>>>>>>>>>

           Batalla 🚢  Naval

          [+] INICIAR NUEVO JUEGO

          [x] CARGAR USUARIO

          [a] EDITAR DATOS

          [e] MOSTRAR ESTADÍSTICAS
    """)

    if menu == "+":

      jugador = crear_new_usuario()

      print("\t ¡REGISTRO EXITOSO! A JUGAR! 🚢 \n")

      play_juego(jugador)

    elif menu.lower() == "x":

      username = input("Ingrese su nombre de jugador: ")

      while len(username) > 30 or " " in username or not username.islower():
        username = input("Ingrese su nombre de jugador correctamente: ")

      if verificar_usuario(username):

        jugador = buscar_jugador(username)

        play_juego(jugador)

      else:

        print("Este usuario no existe! ")
        main() 
      
    elif menu.lower() == "a":

      mostrar_usuarios()

      option = input("Selecciona el usuario a modificar (1/2/3/4...): ")

      while not option.isdigit() or int(option) < 1:
        option = input('Ingrese su opción correctamente: ')

      actualizar_info(int(option))
    
    elif menu.lower() == "e":

      rango_edad = usuarios_jugadores()
      puntos_genero = puntosPorGenero()
      promedio_disparos = promedio_disparos_ganar()

      estadisticas = Estadistica(rango_edad,puntos_genero,promedio_disparos)

      estadisticas.mostrar_estadisticas()

    else:
      main()

main()