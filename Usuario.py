class Usuario:

  def __init__(self,username,nombre,edad,genero,puntos_totales,partidas_jugadas):

    self.username = username
    self.nombre = nombre
    self.edad = edad
    self.genero = genero
    self.puntos_totales = puntos_totales
    self.partidas_jugadas = partidas_jugadas

  def mostra_info(self):
    print("""
    <<<<<<<<<<--♦ BATALLA NAVAL ♦-->>>>>>>>>>

    Player: {}
    Nombre: {}
    Edad: {}
    Genero: {}
    Puntos Totales: {}
    Partidas Jugadas: {}
    """.format(self.username,self.nombre,self.edad,self.genero,self.puntos_totales,self.partidas_jugadas))

  def registrar_base_datos(self):

    with open("Base_Datos.txt", "a+") as jugador: 
      jugador.write("{},{},{},{},{},{}\n".format(self.username,self.nombre,self.edad,self.genero,self.puntos_totales,self.partidas_jugadas))