
def mostrarIndices(filas, columnas):
  for i in range(filas-1, -1, -1): 
    if i % 2 == 0:
      for j in range(columnas-1, -1, -1): 
        print(f"fila = [{i}], columna =[{j}]")
    else:
      for j in range(columnas): 
        print(f"fila = [{i}], columna =[{j}]")

mostrarIndices(3,3)
