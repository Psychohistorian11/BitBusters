import pygame
import random
import math
import time
pygame.init()

class InformacionDibujo:
    NEGRO = 0, 0, 0
    BLANCO = 255, 255, 255
    VERDE = 0, 255, 0
    ROJO = 255, 0, 0
    COLOR_FONDO = BLANCO

    GRADIENTES = [
        (128, 128, 128),
        (160, 160, 160),
        (192, 192, 192)
    ]

    FUENTE = pygame.font.SysFont('candara', 18)
    FUENTE_GRANDE = pygame.font.SysFont('candara', 24)

    MARGEN_LATERAL = 100
    MARGEN_SUPERIOR = 150

    def __init__(self, ancho, alto, lista):
        self.ancho = ancho
        self.alto = alto

        self.ventana = pygame.display.set_mode((ancho, alto))
        pygame.display.set_caption("Visualización de Algoritmos de Ordenamiento")
        self.establecer_lista(lista)

    def establecer_lista(self, lista):
        self.lista = lista
        self.valor_min = min(lista)
        self.valor_max = max(lista)

        self.ancho_bloque = round((self.ancho - self.MARGEN_LATERAL) / len(lista))
        self.alto_bloque = math.floor((self.alto - self.MARGEN_SUPERIOR) / (self.valor_max - self.valor_min))
        self.inicio_x = self.MARGEN_LATERAL // 2


def dibujar(info_dibujo, nombre_algo):
    info_dibujo.ventana.fill(info_dibujo.COLOR_FONDO)

    titulo = info_dibujo.FUENTE_GRANDE.render(f"{nombre_algo}", 1, info_dibujo.ROJO)
    info_dibujo.ventana.blit(titulo, (info_dibujo.ancho/2 - titulo.get_width()/2 , 5))

    controles = info_dibujo.FUENTE.render("R - Reiniciar | ESPACIO - Iniciar Ordenamiento | B - Burbuja |L - Burbuja Bidireccional | I - Inserción | M - Mezcla | C - Conteo |Q - Rapido | X - Radix | K -Casilleros", 1, info_dibujo.NEGRO)
    info_dibujo.ventana.blit(controles, (info_dibujo.ancho/2 - controles.get_width()/2 , 45))

    dibujar_lista(info_dibujo)
    pygame.display.update()


def dibujar_lista(info_dibujo, posiciones_color={}, borrar_fondo=False):
    lista = info_dibujo.lista

    if borrar_fondo:
        rectangulo_limpiar = (info_dibujo.MARGEN_LATERAL//2, info_dibujo.MARGEN_SUPERIOR,
                        info_dibujo.ancho - info_dibujo.MARGEN_LATERAL, info_dibujo.alto - info_dibujo.MARGEN_SUPERIOR)
        pygame.draw.rect(info_dibujo.ventana, info_dibujo.COLOR_FONDO, rectangulo_limpiar)

    for i, val in enumerate(lista):
        x = info_dibujo.inicio_x + i * info_dibujo.ancho_bloque
        y = info_dibujo.alto - (val - info_dibujo.valor_min) * info_dibujo.alto_bloque

        color = info_dibujo.GRADIENTES[i % 3]

        if i in posiciones_color:
            color = posiciones_color[i]

        pygame.draw.rect(info_dibujo.ventana, color, (x, y, info_dibujo.ancho_bloque, info_dibujo.alto))

    if borrar_fondo:
        pygame.display.update()


def generar_lista_inicial(n, valor_min, valor_max):
    lista = []

    for _ in range(n):
        val = random.randint(valor_min, valor_max)
        lista.append(val)

    return lista


def bubble_sort(info_dibujo):
    lista = info_dibujo.lista

    for i in range(len(lista) - 1):
        dibujar_lista(info_dibujo, {i - 1: info_dibujo.VERDE, i: info_dibujo.ROJO}, True)
        for j in range(len(lista) - 1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                dibujar_lista(info_dibujo, {j: info_dibujo.NEGRO, j + 1: info_dibujo.ROJO}, True)

    return lista


def insertion_sort(info_dibujo):
    lista = info_dibujo.lista

    for i in range(1, len(lista)):
        actual = lista[i]
        dibujar_lista(info_dibujo, {i - 1: info_dibujo.VERDE, i: info_dibujo.ROJO}, True)

        while i > 0 and lista[i - 1] > actual:
            lista[i] = lista[i - 1]
            i = i - 1
            lista[i] = actual
            dibujar_lista(info_dibujo, {i - 1: info_dibujo.VERDE, i: info_dibujo.ROJO}, True)

    return lista
def counting_sort(info_dibujo):
    lista = info_dibujo.lista
    n = len(lista)

    max_valor = max(lista)
    min_valor = min(lista)
    rango = max_valor - min_valor + 1

    cuenta = [0] * rango
    resultado = [0] * n

    for i in range(n):
        cuenta[lista[i] - min_valor] += 1
        dibujar_lista(info_dibujo, {i: info_dibujo.NEGRO, i - 1: info_dibujo.VERDE}, True)

    for i in range(1, len(cuenta)):
        cuenta[i] += cuenta[i - 1]
        dibujar_lista(info_dibujo, {i: info_dibujo.NEGRO, i - 1: info_dibujo.VERDE}, True)

    for i in range(n - 1, -1, -1):
        resultado[cuenta[lista[i] - min_valor] - 1] = lista[i]
        cuenta[lista[i] - min_valor] -= 1
        dibujar_lista(info_dibujo, {i: info_dibujo.NEGRO, i - 1: info_dibujo.VERDE}, True)

    for i in range(n):
        lista[i] = resultado[i]
        dibujar_lista(info_dibujo, {i: info_dibujo.NEGRO, i - 1: info_dibujo.VERDE}, True)

    return lista

def quicksort(info_dibujo):
    lista = info_dibujo.lista

    def particion(bajo, alto):
        pivote = lista[alto]
        i = bajo - 1

        for j in range(bajo, alto):
            if lista[j] <= pivote:
                i += 1
                lista[i], lista[j] = lista[j], lista[i]
                dibujar_lista(info_dibujo, {i: info_dibujo.VERDE, j: info_dibujo.ROJO}, True)

        lista[i + 1], lista[alto] = lista[alto], lista[i + 1]
        dibujar_lista(info_dibujo, {i + 1: info_dibujo.VERDE, alto: info_dibujo.ROJO}, True)
        return i + 1

    def quicksort_rec(bajo, alto):
        if bajo < alto:
            indice_pivote = particion(bajo, alto)
            quicksort_rec(bajo, indice_pivote - 1)
            quicksort_rec(indice_pivote + 1, alto)

    quicksort_rec(0, len(lista) - 1)
    return lista


def merge_sort(info_dibujo):
    def merge(lista, izquierda, medio, derecha):
        izq = lista[izquierda:medio + 1]
        der = lista[medio + 1:derecha + 1]

        i = j = 0
        k = izquierda

        while i < len(izq) and j < len(der):
            if izq[i] <= der[j]:
                lista[k] = izq[i]
                i += 1
            else:
                lista[k] = der[j]
                j += 1
            dibujar_lista(info_dibujo, {k: info_dibujo.VERDE}, True)
            k += 1

        while i < len(izq):
            lista[k] = izq[i]
            dibujar_lista(info_dibujo, {k: info_dibujo.VERDE}, True)
            i += 1
            k += 1

        while j < len(der):
            lista[k] = der[j]
            dibujar_lista(info_dibujo, {k: info_dibujo.VERDE}, True)
            j += 1
            k += 1

    def merge_sort_rec(lista, izquierda, derecha):
        if izquierda < derecha:
            medio = (izquierda + derecha) // 2
            merge_sort_rec(lista, izquierda, medio)
            merge_sort_rec(lista, medio + 1, derecha)
            merge(lista, izquierda, medio, derecha)

    lista = info_dibujo.lista
    merge_sort_rec(lista, 0, len(lista) - 1)
    return lista

def counting_sort_for_radix(lista, exp, info_dibujo):
    n = len(lista)
    cuenta = [0] * 10
    resultado = [0] * n

    for i in range(n):
        index = lista[i] // exp
        cuenta[index % 10] += 1

    for i in range(1, 10):
        cuenta[i] += cuenta[i - 1]

    i = n - 1
    while i >= 0:
        index = lista[i] // exp
        resultado[cuenta[index % 10] - 1] = lista[i]
        cuenta[index % 10] -= 1
        i -= 1

    for i in range(n):
        lista[i] = resultado[i]
        dibujar_lista(info_dibujo, {i: info_dibujo.VERDE}, True)

def radix_sort(info_dibujo):
    lista = info_dibujo.lista
    max_valor = max(lista)
    exp = 1

    while max_valor // exp > 0:
        counting_sort_for_radix(lista, exp, info_dibujo)
        exp *= 10

def cocktail(info_dibujo):
    lista = info_dibujo.lista
    n = len(lista)
    empezar_en = 0

    while True:
        intercambiado = False

        for i in range(empezar_en, n - 1):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                intercambiado = True
                dibujar_lista(info_dibujo, {i: info_dibujo.NEGRO, i + 1: info_dibujo.ROJO}, True)


        if not intercambiado:
            break

        intercambiado = False
        n -= 1

        for i in range(n - 1, empezar_en, -1):
            if lista[i] < lista[i - 1]:
                lista[i], lista[i - 1] = lista[i - 1], lista[i]
                intercambiado = True
                dibujar_lista(info_dibujo, {i: info_dibujo.NEGRO, i -1: info_dibujo.VERDE}, True)

        if not intercambiado:
            break

        empezar_en += 1

    return lista
def bucket_sort(info_dibujo):
    lista = info_dibujo.lista
    max_lista = max(lista)
    min_lista = min(lista)

    rango = (max_lista - min_lista) / len(lista)

    buckets = [[] for _ in range(len(lista))]

    for i in lista:
        index = int((i - min_lista) / rango)
        if index == len(lista):
            index -= 1
        buckets[index].append(i)

    resultado = []
    for bucket in buckets:
        bucket.sort()  # Ordena el bucket directamente sin asignarlo
        resultado.extend(bucket)
        info_dibujo.lista= resultado
        dibujar_lista(info_dibujo, {i: info_dibujo.VERDE}, True)

    info_dibujo.lista = resultado  # Actualiza la lista en el info_dibujo con la lista ordenada


    return resultado


def main():
    ejecutar = True
    reloj = pygame.time.Clock()

    n = 500
    valor_min = 0
    valor_max = 100

    lista = generar_lista_inicial(n, valor_min, valor_max)
    info_dibujo = InformacionDibujo(1280, 720, lista)
    ordenando = False

    algoritmo_ordenamiento = bubble_sort
    nombre_algoritmo = "Burbuja"


    while ejecutar:
        reloj.tick(60)

        if ordenando:
            algoritmo_ordenamiento(info_dibujo)
            ordenando = False
        else:
            dibujar(info_dibujo, nombre_algoritmo)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutar = False

            if evento.type != pygame.KEYDOWN:
                continue

            if evento.key == pygame.K_r:
                lista = generar_lista_inicial(n, valor_min, valor_max)
                info_dibujo.establecer_lista(lista)
                ordenando = False
            elif evento.key == pygame.K_SPACE and not ordenando:
                ordenando = True
            elif evento.key == pygame.K_b and not ordenando:
                algoritmo_ordenamiento = bubble_sort
                nombre_algoritmo = "Burbuja"
            elif evento.key == pygame.K_i and not ordenando:
                algoritmo_ordenamiento = insertion_sort
                nombre_algoritmo = "Inserción"
            elif evento.key == pygame.K_m and not ordenando:
                algoritmo_ordenamiento = merge_sort
                nombre_algoritmo = "Mezcla"
            elif evento.key == pygame.K_c and not ordenando:
                algoritmo_ordenamiento = counting_sort
                nombre_algoritmo = "Conteo"
            elif evento.key == pygame.K_q and not ordenando:
                algoritmo_ordenamiento = quicksort
                nombre_algoritmo = "Rapido"
            elif evento.key == pygame.K_x and not ordenando:
                algoritmo_ordenamiento = radix_sort
                nombre_algoritmo = "Radix"
            elif evento.key == pygame.K_k and not ordenando:
                algoritmo_ordenamiento = bucket_sort
                nombre_algoritmo = "Casilleros"
            elif evento.key == pygame.K_l and not ordenando:
                algoritmo_ordenamiento = cocktail
                nombre_algoritmo = "Burbuja Bidireccional"



main()
