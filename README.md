# algoritmos-aleatorios

Algoritmos Generadores de Números Pseudoaleatorios


<b>ALGORITMOS GENERADORES NO CONGRUENCIALES</b>

<b>Algoritmo de Cuadrados Medios</b>

Este algoritmo no congruencial fue propuesto en la década de los cuarenta del siglo XX, por Von Neuman y Metropolis. Para generar números aleatorios de cuadrados medios se siguen los siguientes pasos:

Seleccionar una semilla (Xo) con D dígitos (D>3).
Sea Xo = resultado de elevar Xo al cuadraado; sea X1 = los D dígitos del centro y sea ri = 0.D dígitos del centro.
Sea Yi = resultado de elevar Xi al cuadrado; sea Xi+1 =los D dígitos del centro y sea ri =  0.D dígitos del centro para toda i = 1,2,3…n.
Repetir el paso anterior hasta obtener los n números ri deseados.
Si no es posible obtener los D dígitos del centro del número Yi , agregue ceros a la izquierda del número Yi
EJEMPLO

Generar los primeros 4 números ri a partir de una semilla Xo = 5735 de donde se puede observar que D = 4 dígitos

<i>SOLUCIÓN</i>

Y0 = (5735)2 = 32890225   X1 = 8902   r1 = 0.8902
Y1 = (8902)2 = 79245604   X2 = 2456   r2 = 0. 2456
Y2 = (2456)2 = 06031936   X3 = 0319   r3 = 0. 0319
Y3 = (0319)2 = 101761       X4 = 0176       r4 = 0. 0176

<b>Algoritmos de Productos Medios</b>

La diferencia radica en que el algoritmo de productos medios requiere dos semillas ambas con D dígitos además en lugar de elevarlas al cuadrado, las semillas se multiplican y del producto se seleccionan los D dígitos del centro, los cuales formarán el primer número pseudo aleatorio ri =  0.D dígitos. Después se elimina una semilla y la otra se multiplica por el primer número de D dígitos para luego seleccionar del producto de los D dígitos que conformarán un segundo número ri .Entonces se elimina la segunda semilla y se multiplican el primer número de D dígitos por el segundo número de D dígitos del producto se obtiene el tercer número ri. .Siempre se irá eliminando el número más antiguo y el procedimiento se repetirá hasta generar los n números pseudo aleatorios.

Los pasos a seguir son los siguientes:

Seleccionar una semilla (Xo) con D dígitos (D>3).
Seleccionar una semilla (X1) con D dígitos (D>3).Sea Yo = Xo * X1 ;sea X2 los D dígitos del centro y sea ri = 0.D dígitos del centro.
Sea Yi = Xi * X1+1 ;sea Xi+2 los D dígitos del centro y sea ri +1= 0.D dígitos del centro para toda i = 1,2,3…n.
Repetir el paso anterior hasta obtener los n números ri deseados.
Si no es posible obtener los D dígitos del centro del número Yi , agregue ceros a la izquierda del número Yi
Algoritmo Multiplicador Constante

Los pasos para desarrolar este algoritmo son los siguientes:

Seleccionar una semilla (Xo) con D dígitos (D>3).
Seleccionar una semilla (X1) con D dígitos (D>3).
Sea Yo = Xo * X1 ;sea X2 los D dígitos del centro y sea ri = 0.D dígitos del centro.
Sea Yi = Xi * X1+1 ;sea Xi+2 los D dígitos del centro y sea ri +1= 0.D dígitos del centro para toda i = 1,2,3…n.
Repetir el paso anterior hasta obtener los n números ri deseados.
Si no es posible obtener los D dígitos del centro del número Yi , agregue ceros a la izquierda del número Yi
Algoritmo Congruencial Multiplicativo

La ecuación recursiva es:
X i+1 = (aXi)mod(m)         i=0,1,2,3,…,n
Las condiciones para el alcance de su máximo periodo es:
m = 2g
a = 3+8k   o    5+8k
k = 0,1,2,3,…
X0 debe ser un número impar
g debe ser entero

<b>Algoritmo Congruencial Aditivo</b>

La ecuación recursiva es:
X i = (Xi-1 + Xi-n)mod(m)        i=n+1,n+2,n+3,…,N

Los números ri pueden ser generados mediante la ecuación:
ri = xi / (m-1)

<b>Algoritmo Congruencial no Lineales</b>

La ecuación recursiva es:
X i+1 = (aX2i + bXi +c)mod(m)            i=0,1,2,3,…,N

Las condiciones para el alcance de su máximo periodo es:
m = 2g
a debe ser un numero par
c debe ser un numero impar
g debe ser entero
(b – 1) mod 4 = 1
