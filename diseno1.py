def point(arreglo1, arreglo2):
  if len(arreglo1) == 0:
    return 0
  else:
    return (arreglo1.pop() * arreglo2.pop(0)) + point(arreglo1, arreglo2)
def bubbleSort(arr):
  n = len(arr)
  for i in range(n - 1):
    for j in range(0, n - i - 1):
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
  return arr
arregloej = [3,1,1]
arregloej2= [6,5,4]
a3 = [6,1,9,5,4]
a4 = [3,4,8,2,4]
arregloejordenado = bubbleSort(arregloej)
arregloej2ordenado = bubbleSort(arregloej2)
a3ordenado = bubbleSort(a3)
a4ordenado= bubbleSort(a4)
num = point(arregloejordenado,arregloej2ordenado)
num2= point(a3ordenado,a4ordenado)

print("primero",num,num2)

# 2do ------------
def optimo(n, contador=1, operacion=1):
  if operacion == n:
    return contador
  if operacion > n:
    return float('inf')
  izquierda = optimo(n, contador + 1, operacion + 1)
  derecha = optimo(n, contador + 1, operacion * 2)
  if izquierda is None:
    return derecha
  if derecha is None:
    return izquierda
  return min(izquierda, derecha)


print("segundo",optimo(10))
