Xi = int(input('Introduce el valor de la semilla: '))
m = int(input('Ingrese el valor del módulo: '))
ri = 0
cont = 0
def blum(m, ri, Xi, cont):

    while(cont!= m):

        cont += 1
        # la formula generando los números
        Xi = (Xi**2)%m
        # Generando las r
        ri = (Xi/(m-1))
        #imprime los r

        print('X' + str(cont) + ' es ' + str(Xi))
        print('r' + str(cont) + ' es ' + str(ri))


blum(m, ri, Xi, cont)