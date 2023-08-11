from program import *
class InterfazConsola:
    def __init__(self,programa: Program):
      self.programa = programa
      print("Bienvenido al programa para recorrer una matriz en forma de caracol 🐌")
    def mostrar_menu(self):
        print("""
        🎮 Menú Principal 🎮

1. ➕ Definir dimensiones de la matriz
2. ✏️ Recorrer Matriz en forma de caracol
3. 🚪 Salir
""")
    def crear_matriz(self,filas,columnas):
        if filas > 0 and columnas> 0:

            self.programa.llenar_matriz(filas,columnas)
            print("➕Resultado de la creación de la matriz:\n")
            for i in self.programa.matriz:
                print(i)
        else:
            print("Ingresa filas y columnas mayores que 0 -_-")
    def elegir(self):
        answer = int(input("Ingrese una opción:"))
        if answer == 1:
           return 0
        elif answer == 2:
            return 1
        elif answer == 3:
            return 2

    def correr(self):
        while True:
            self.mostrar_menu()
            opcion = self.elegir()
            if opcion == 0:
                filas = int(input("\nIngrese numero de filas: "))
                columnas = int(input("Ingrese numero de columnas:"))
                print("\n")
                self.crear_matriz(filas,columnas)
            elif opcion ==1:
                self.programa.recorrerMatrizEspiral()
            elif opcion ==2:
                break
            else:
                print("Ingresa una opción valida")


