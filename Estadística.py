class Estadistica:

    def __init__(self,rango_edad,puntos_genero,promedio_disparos):
        
        self.rango_edad = rango_edad
        self.puntos_genero = puntos_genero
        self.promedio_disparos = promedio_disparos

    def mostrar_estadisticas(self):

        print("""
        <<<<<<<<<<-♦ ESTADÍSTICAS ♦->>>>>>>>>

        -♦ RANGO DE EDAD DE CLIENTES FRECUENTES: {}
        -♦ CANTIDAD TOTAL DE PUNTOS POR GÉNERO (M,F): {}
        -♦ PROMEDIO DE DISPAROS PARA GANAR: {}

        """.format(self.rango_edad,self.puntos_genero,self.promedio_disparos))

    def mostrar_top10(self,top10):

        for i,jugador in enumerate(top10):
            print("*"*5+ i+1 + jugador +"*"*5)
