#multiplicador constante
n=int(input('Ingrese la cantidad de números a generar: '))
i=0
X=list()
Y=list()
r=list()
X.insert(i,int(input('Ingrese una semilla con cuatro dígitos: ')))
X.insert(i+1,int(input('Ingrese una constante: ')))
D=(len(str(X[i]))+len(str(X[i])))//2

if D>3:
    ok=0
    while i<n and ok==0:
        Y.insert(i,str(X[i]*X[i+1]))
        dY=len(Y[i])
        if(dY%2 or dY<D):
            Y.insert(i,'0'+Y[i])
            dY+=1
        di=dY//2-2
        X.insert(i+1,int(Y[i][di:di+D]))
        numA=X[i+1]/10**D
        if not numA in r:
            r.insert(i,numA)
            i+=1
        else:
            ok=1
        print('X' + str(i) + ' tiene r'+str(i)+ ' = ' + str(numA))
    print('Se generaron ',i,'números aleatorios')

else:
    print('Debe ingresar semilla con más de tres dígitos')