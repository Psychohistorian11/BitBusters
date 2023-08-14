import time



class Program:
    def __init__(self):
        self.matriz = []
    def llenar_matriz(self,filas,columnas):
        self.matriz = [[ 0 for _ in range(columnas)] for _ in range(filas)]
        contador = 0
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz[0])):
                contador += 1
                self.matriz[i][j] = contador


    def obtenerNumeroFilas(self):
        return len(self.matriz)

    def obtenerNumeroColumnas(self):
        return len(self.matriz[0])

    def recorrerMatrizEspiral(self, fila=0, columna=0, contador=0, n=0,fase_horizontal=1,fase_vertical = 1,valor=[]):
        numerofilasMatriz = self.obtenerNumeroFilas()
        if numerofilasMatriz <=0:
            raise Exception("Debes ingresar un matriz al menos con una cantidad de filas  mayor o igual  a cero.")
        numerocolumnasMatriz = self.obtenerNumeroColumnas()
        if numerocolumnasMatriz <= 0 :
            raise Exception("Debes ingresar un matriz al menos con una cantidad de columnas  mayor o igual  a cero.")
        if contador == (self.obtenerNumeroFilas() *self.obtenerNumeroColumnas()):
            self.llenar_matriz(self.obtenerNumeroFilas(),self.obtenerNumeroColumnas())
            return valor
        elif columna != self.obtenerNumeroColumnas()-n and fase_horizontal == 1 and fase_vertical ==1:
            valor.append(self.matriz[fila][columna])
            self.matriz[fila][columna] = "🐌"
            contador += 1
            columna += 1
            print("Recorriendo matriz en forma de caracol 🐌... \n")
            for i in self.matriz:
                print(i)
            print("\n")
            time.sleep(2)
            return self.recorrerMatrizEspiral(fila,columna,contador,n,fase_horizontal,fase_vertical,valor)
        elif fila != self.obtenerNumeroFilas()-1-n and fase_vertical == 1:
            fila += 1
            valor.append(self.matriz[fila][columna - 1])
            self.matriz[fila][columna-1] = "🐌"
            contador += 1
            print("Recorriendo matriz en forma de caracol 🐌... \n")
            for i in self.matriz:
                print(i)
            print("\n")
            time.sleep(2)

            return self.recorrerMatrizEspiral(fila, columna, contador, n,2,fase_vertical,valor)
        elif columna != 1+n and fase_horizontal == 2:
            columna -= 1
            valor.append(self.matriz[fila][columna - 1])
            self.matriz[fila][columna-1] = "🐌"
            contador += 1
            print("Recorriendo matriz en forma de caracol 🐌... \n")
            for i in self.matriz:
                print(i)
            print("\n")
            time.sleep(2)

            return self.recorrerMatrizEspiral(fila, columna, contador, n,fase_horizontal,2,valor)
        elif fila != 1+n and fase_vertical == 2 :
            fila -= 1
            valor.append(self.matriz[fila][columna - 1])
            self.matriz[fila][columna - 1] = "🐌"
            contador += 1
            print("Recorriendo matriz en forma de caracol 🐌... \n")
            for i in self.matriz:
                print(i)
            print("\n")
            time.sleep(2)

            return self.recorrerMatrizEspiral(fila,columna,contador,n,1,fase_vertical,valor)
        else:
            n +=1
            return self.recorrerMatrizEspiral(fila,columna,contador,n,1,1,valor)

    def recorrerMatrizEspiral_Analisis(self, fila, columna, contador=1, n=0, fase_horizontal=1, fase_vertical=1, valor=[]):
        numerofilasMatriz = self.obtenerNumeroFilas()
        if numerofilasMatriz <= 0:
            raise Exception("Debes ingresar un matriz al menos con una cantidad de filas  mayor o igual  a cero.")
        numerocolumnasMatriz = self.obtenerNumeroColumnas()
        if numerocolumnasMatriz <= 0:
            raise Exception("Debes ingresar un matriz al menos con una cantidad de columnas  mayor o igual  a cero.")
        if contador == (self.obtenerNumeroFilas() * self.obtenerNumeroColumnas())+1 :
            self.llenar_matriz(self.obtenerNumeroFilas(), self.obtenerNumeroColumnas())
            return valor
        elif columna != -1 + n and fase_horizontal == 1 and fase_vertical == 1:
            valor.append(self.matriz[fila][columna])
            self.matriz[fila][columna] = "🐌"
            contador += 1
            columna -= 1
            print("Recorriendo matriz en forma de caracol 🐌... \n")
            for i in self.matriz:
                print(i)
            print("\n")
            time.sleep(2)
            return self.recorrerMatrizEspiral_Analisis(fila, columna, contador, n, fase_horizontal, fase_vertical, valor)
        elif fila != (self.obtenerNumeroFilas()-1)-n and fase_vertical == 1:
            fila += 1
            valor.append(self.matriz[fila][columna+1])
            self.matriz[fila][columna+1] = "🐌"
            contador += 1
            print("Recorriendo matriz en forma de caracol 🐌... \n")
            for i in self.matriz:
                print(i)
            print("\n")
            time.sleep(2)
            return self.recorrerMatrizEspiral_Analisis(fila, columna, contador, n, 2, fase_vertical,
                                                       valor)
        elif columna+2 != self.obtenerNumeroColumnas()-n and fase_horizontal == 2:
            columna += 1
            contador +=1
            valor.append(self.matriz[fila][columna+1])
            self.matriz[fila][columna+1] = "🐌"
            print("Recorriendo matriz en forma de caracol 🐌... \n")
            for i in self.matriz:
                print(i)
            print("\n")
            time.sleep(2)
            return self.recorrerMatrizEspiral_Analisis(fila, columna, contador, n, fase_horizontal, 2,
                                                       valor)
        elif fila != 1+n and fase_vertical ==2:
            fila -= 1
            contador +=1
            valor.append(self.matriz[fila][columna+1])
            self.matriz[fila][columna + 1] = "🐌"
            print("Recorriendo matriz en forma de caracol 🐌... \n")
            for i in self.matriz:
                print(i)
            print("\n")
            time.sleep(2)
            return self.recorrerMatrizEspiral_Analisis(fila, columna, contador, n, 2, fase_vertical,
                                                       valor)
        else:
            n +=1
            return self.recorrerMatrizEspiral_Analisis(fila, columna, contador, n, 1, 1,
                                                       valor)
    def revertir_arreglo(self,arreglo):
        a = Program()
        a.llenar_matriz(4, 4)
        list_resultado = []
        for i in range(len(arreglo) - 1, -1, -1):
            list_resultado.append(arreglo[i])

        return list_resultado






















