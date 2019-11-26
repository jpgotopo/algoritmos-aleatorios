Xi = int(input('Introduce el valor de la semilla: '))
m = int(input('Ingrese el valor del módulo: '))
ri = 0
cont = 0
def cuadratico(m, ri, Xi, cont):


    a = int(input('Ingrese el valor de a: '))
    b = int(input('Ingrese el valor de b: '))
    c = int(input('Ingrese el valor de c: '))
a
    while(cont != m):
        i = 0
        cont += 1
        # la formula generando los números
        Xi = ((a*(Xi**2))+b*Xi+c)%m
        # Generando las r
        ri = (Xi/(m-1))
        #imprime los r


        print(ri)


cuadratico(m, ri, Xi, cont)