import LIbComp as lc
import math


def sumamatrix(A, B):
    m = len(A)
    n = len(A[0])
    print(m)
    print(n)
    fila = [(0,0)] * n
    suma = [fila]* m
    for j in range(m):
        fila = [(0,0)] * n
        suma[j] = fila
        for k in range(n):
            suma[j][k] = lc.sumaComp(A[j][k],B[j][k])
    return suma

def transpuesta(m):
    f =  len(m)
    c = len(m[0])
    fila = [(0,0)] * c
    transpuesta = [fila] * f
    for j in range(f):
        fila = [(0,0)] * c
        transpuesta[j] = fila
        for k in range(c):
            transpuesta[j][k] = m[k][j]
    return transpuesta  


def inversoMat(m):
    f =  len(m)
    c = len(m[0])
    fila = [(0,0)] * c
    inver = [fila] * f
    for j in range(f):
        fila = [(0,0)] * c
        inver[j] = fila
        for k in range(c):
            inver[j][k] = lc.producComp((-1,0),m[j][k])
    return inver  

def conjugada(m):
    f =  len(m)
    c = len(m[0])
    fila = [(0,0)] * c
    conjugada = [fila] * f
    for j in range(f):
        fila = [(0,0)] * c
        conjugada[j] = fila
        for k in range(c):
            conjugada[j][k] = lc.conjComp(m[j][k])
    return conjugada  

def adjuntaMat(m):
    f =  len(m)
    c = len(m[0])
    fila = [(0,0)] * c
    adjunta = [fila] * f
    m = conjugada(transpuesta(m))
    for j in range(f):
        fila = [(0,0)] * c
        adjunta[j] = fila
        for k in range(c):
            adjunta[j][k] = m[j][k]
    return adjunta  


def multEscMat(m):
    e = int(input("dijite el escalar a multiplicar: "))
    f =  len(m)
    c = len(m[0])
    fila = [(0,0)] * c
    multiE = [fila] * f
    for j in range(f):
        fila = [(0,0)] * c
        multiE[j] = fila
        for k in range(c):
            multiE[j][k] = lc.producComp((e,0),m[j][k])
    return multiE   

      

def producMat(m,w):
    f =  len(m)
    c = len(w)
    a = [[(0,0) for i in range (c)] for i in range (f)]  
    for i   in range (f):
        for j in range(c):
            for k in range(f):
                a[i][j] = lc.sumaComp(a[i][j],lc.producComp(m[i][k],w[k][j]))
    return  a

def inversoVec(v):
    num = len(v)
    s = [(0,0)] * num
    for i in range (num):
        s[i] = lc.producComp((-1,0),v[i])
    return (s)
    
def multEscVec(v):
    f = int(input("escalar a multiplicar: "))
    num = len(v)
    s = [(0,0)] * num 
    for i in range (num):
        s[i] = lc.producComp((f,0),v[i])
    return (s)

def producIntVec(v,u):
    num = len(v)
    x = (0,0)
    s = [(0,0)] * num 
    for i in range (num):
        s[i] = lc.producComp(lc.conjComp(v[i]),u[i]) 
        x = lc.sumaComp(s[i],x)
    return (x)

def normaVec(v):
    num = len(v)
    s = (0,0)
    for i in range (num):
        s = lc.sumaComp(lc.producComp(v[i],v[i]),s) 
    s = lc.modComp(s)
    print(s)

def  tensorVecPro(a,b):
    na = len(a)
    nb = len(b)
    nr = na * nb

def distanciaVec(v,w):
    num = len(v)
    s = 0
    for i in range (num):
        s = s + (lc.modComp(lc.restaCom(v[i],w[i])))**2
    s = s**(1/2)
    return s

def matUnit (w):
    f = len(w)
    a = [[(0,0) for i in range (f)] for i in range (f)] 
    p = [[(0,0) for i in range (f)] for i in range (f)] 
    for i in range (f):
        a = producMat(adjuntaMat(w),w)
    for i in range (f):
        p[i][i] = (1,0)
    x = a == p
    return  x


def matHer (w):
    f = len(w)
    a = [[(0,0) for i in range (f)] for i in range (f)] 
    a = adjuntaMat(w)
    x = a == w
    return  x

def accionMacVec(m,v):
    f =  len(m)
    a = [(0,0)] * f
    for j in range(f):
        for k in range(f):   
            a[j] = lc.sumaComp(a[j],lc.producComp(m[j][k],v[k]))
    return  a

if __name__ == '__main__':
    v = [(-8,0),(10,0)]
    u = [[(1,2),(3,4)],
         [(5,6),(7,8)]]
    w = [[(2,4),(6,8)],
         [(10,12),(14,16)]]
    print(producMat([[(1,2),(4,5)],[(6,7),(8,9)]],[[(2,4),(6,8)],[(10,2),(14,16)]]))
