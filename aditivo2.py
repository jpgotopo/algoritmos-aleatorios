n = int(input('Ingrese la cantidad de números a ingresar: '))
p = int(input('Ingrese la cantidad de números a generar: '))
m = int(input('Ingrese el valor del módulo: '))
i = 0
d = 0
X = list()
Y = list()
for d in range(n):
    X.insert(d, int(input('Ingrese una dato: ')))

def aditivo(n, p, m, X):
    ri = 0
    for i in range(p):
        X.append((X[n-1]+X[i])%m)
        ri = X[n]/(m-1)
        print ('X'+str(n+1) + ' = ' + str(X[n]) + ' r' + str(i) + ' = ' + str(ri))
        n += 1

aditivo(n, p, m, X)