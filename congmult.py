#congruencial multiplicativo
def multiplicador(x0, a, m):
    return (a * x0) % m;
n = int(input('Ingrese la cantidad de números a generar: '))
x = int(input("Introduce el valor de la semilla: "))
g = int(input("Introduce el valor del periodo: "))
a = 1 + (4*g)
m = 2**g
ini = x
cont = 0
for i in range(n):
    x = multiplicador(x, a, m);
    print   (x)
    if ini != x:
        cont += 1

print("contador", cont)
if m == cont:
    print("es completo")
else:
    print("es incompleto")