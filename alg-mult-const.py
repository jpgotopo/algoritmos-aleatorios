# Algoritmo Multiplicador Constante
n = int(input('Ingrese la cantidad de números a generar: '))
X = int(input('Ingrese el valor (cuatro dígitos)  de la Semilla: '))
a = int(input('Ingrese el valor de la constante (cuatro dígitos): '))
m = int(input('Ingrese el valor de m: '))


def multiConstante(n, X, a, m):
    D = ""
    r = 0
    for i in range(n):
        X = (X*a)
        Y = str(X)
        D = (Y[2:6])
        r = int(D)%m
        print (D)
        print (X)



multiConstante(n, X, a, m)