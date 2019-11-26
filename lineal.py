#congruencial lineal
def congruencial(x0, a, b, m):
    return (a * x0 + b) % m;

x = int(input("Introduce el valor de la semilla: "))
res = [0,0] #Primer elemento valor de r, segundo elemento valor de X
c = int(input("Introduce el valor de la constante aditiva: "))
m = int(input("Introduce el valor de m: "))
a= int(input("Introduce el valor de a: "))


ini = x
cont = 0
repetir = True
while repetir:
    x = congruencial(x, a, c, m);
    r = x/(m-1)

    print('X es ' +str(x) + ' r= ' + str(r))
    if r > res[0]:
        res[0]=r
        res[1]=x
    if ini != x:
        cont += 1
    else:
        repetir = False

print("contador", cont)
print('El mayor valor de r es: ' + str(res[0]) + ' y el mayor valor de x es: ' + str(res[1]))