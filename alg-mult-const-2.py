# Algoritmo Multiplicador Constante Version 2

X = int(input('Ingrese el valor (cuatro dígitos)  de la Semilla: '))
a = int(input('Ingrese el valor de la constante (cuatro dígitos): '))
m = int(input('Ingrese el valor de m: '))

ini = X


def multiConstante(X, a, m):
    D = ""
    r = 0
    cont = 0
    loop = True
    while loop:
        X = (X*a)
        Y = str(X)
        D = (Y[2:6])
        r = int(D) % m
        print(D)
        print(X)
        if ini != X:
            cont = cont + 1
        else:
            loop = False

multiConstante(X, a, m)
print("El periodo de vida máximo es " + str(cont))
