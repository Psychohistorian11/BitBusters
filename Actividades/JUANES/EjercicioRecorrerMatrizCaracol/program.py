import time


class Program:
    def __init__(self):
        self.matriz = []
    def llenar_matriz(self,filas,columnas):
        self.matriz = [[0 for _ in range(columnas)] for _ in range(filas)]

    def obtenerNumeroFilas(self):
        return len(self.matriz)

    def obtenerNumeroColumnas(self):
        return len(self.matriz[0])

    def recorrerMatrizEspiral(self, fila=0, columna=0, contador=1, n=0,fase_horizontal=1,fase_vertical = 1):
        numerofilasMatriz = self.obtenerNumeroFilas()
        if numerofilasMatriz <=0:
            raise Exception("Debes ingresar un matriz al menos con una cantidad de filas  mayor o igual  a cero.")
        numerocolumnasMatriz = self.obtenerNumeroColumnas()
        if numerocolumnasMatriz <= 0 :
            raise Exception("Debes ingresar un matriz al menos con una cantidad de columnas  mayor o igual  a cero.")
        if contador == (self.obtenerNumeroFilas() *self.obtenerNumeroColumnas())+1:
            return self.matriz
        elif columna != self.obtenerNumeroColumnas()-n and fase_horizontal == 1 and fase_vertical ==1:
            self.matriz[fila][columna] = contador
            contador += 1
            columna += 1
            print("Recorriendo matriz en forma de caracol 🐌... \n")
            for i in self.matriz:
                print(i)
            print("\n")
            time.sleep(2)
            return self.recorrerMatrizEspiral(fila,columna,contador,n)
        elif fila != self.obtenerNumeroFilas()-1-n and fase_vertical == 1:
            fila += 1
            self.matriz[fila][columna-1] = contador
            contador += 1
            print("Recorriendo matriz en forma de caracol 🐌... \n")
            for i in self.matriz:
                print(i)
            print("\n")
            time.sleep(2)

            return self.recorrerMatrizEspiral(fila, columna, contador, n,2)
        elif columna != 1+n and fase_horizontal == 2:
            columna -= 1
            self.matriz[fila][columna-1] = contador
            contador += 1
            print("Recorriendo matriz en forma de caracol 🐌... \n")
            for i in self.matriz:
                print(i)
            print("\n")
            time.sleep(2)

            return self.recorrerMatrizEspiral(fila, columna, contador, n,fase_horizontal,2)
        elif fila != 1+n and fase_vertical == 2 :
            fila -= 1
            self.matriz[fila][columna - 1] = contador
            contador += 1
            print("Recorriendo matriz en forma de caracol 🐌... \n")
            for i in self.matriz:
                print(i)
            print("\n")
            time.sleep(2)

            return self.recorrerMatrizEspiral(fila,columna,contador,n,1,fase_vertical)
        else:
            n +=1
            return self.recorrerMatrizEspiral(fila,columna,contador,n,1,1)




