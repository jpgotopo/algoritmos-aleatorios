#congruencial lineal 2
from statistics import mean, variance #Importamos la librería relacionada con estadisticas

#introduciendo el rango de x
x1 = int(input('Introduzca el menor valor de x: '))
x2 = int(input('Introduzca el mayor valor de x: '))
#introduciendo el rango de m
m1 = int(input('Introduce el menor valor de m: '))
m2 = int(input('Introduce el mayor valor de m: '))
k = int(input('Introduce el  valor de k: '))
c = int(input("Introduce el valor de la constante aditiva: "))

a = 1 + (4*k) #Calculando el valor de a usando el valor de k
res = [0,0,0] #Declarando el arreglo donde se almacemará el mayor valor de x, mayor valor de m, y mayor valor de r
cont = 0 #Declarando el contador
arr = [] #Declarando el arreglo donde iremos almacenando los valores de r, para luego calcular media y varianza

#Definimos la funcion llamada congruencial la cual hace el calculo según la fórmula para el Algoritmo Congruencial Lineal
def congruencial(x0, a, b, m):
    return (a * x0 + b) % m;
#El primer for hará un recorrido por todos los valores de x
for i in range(x1, x2+1):
    #El segundo for hará un recorrido por los valores de m
    for j in range(m1, m2+1):

        x = congruencial(i, a, c, j); #Aplicamos la funcion congruencial a cada valor de x
        r = x / (j - 1) #calculamos r con el valor de x
        arr.append(r) #agregamos en cada casilla el valor de r, el numero de casillas del arreglo, aumenta conforme va corriendo el ciclo
        print('x = ' + str(i) + '  m = ' + str(j) + '  r = ' + str(r)) #Imprimimos cada valor de x, de m y de r
        if r > res[2]: #Este condicional me ayuda a almacenar el mayor valor de r (solicitado por el problema)
            # y al mismo tiempo me esta dando el valor de m y de x correspondientes con el valor r, solo si el valor de r es mayor que el anterior
            res[0] = i #valor de la x almacenado en primer indice, da
            res[1] = j #valor de la m almacenado en segundo indice
            res[2] = r #valor de la r almacenado en tercer indice

        cont += 1 #sumando al contador (está contando la cantidad de cálculos realizados

media = mean(arr) #este es un método de la libreria statistics que calcula la media, en este caso, la media de todas las r almacenadas en el arreglo arr
varianza = variance(arr) #este es un método de la libreria statistics que calcula la media, en este caso, la varianza de todas las r almacenadas en el arreglo arr
print("contador", cont) #Imprimiendo contador
#Imprimiendo todos los valores calculados de x m y r
print('El mayor valor de x es: ' + str(res[0]) + ' y el mayor valor de m es: ' + str(res[1]) + ' y el mayor valor de r es: ' + str(res[2]))
#Imprimiendo la media y la Variianza
print('La media es: ' + str(media) + ' y la varianza es: ' + str(varianza))