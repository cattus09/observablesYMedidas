import math
import numpy as np
from numpy import linalg as LA
import LIbComp as lc
import LIbEspVect as lE

#primer sistema cuantico de la sección 4.1
#reto de programación del capitulo 4, reto uno
#1) probabilidad de una posición en particular
def posicionDeProbab(numPosiciones,v):
    tamaño =  len(v)
    s = 0
    for j in range(tamaño):
        s = s + (lc.modComp(v[j]))**2
    s = s**(1/2) 
    proba = (lc.modComp(v[numPosiciones])**2)/s**2
    return  proba

#2) probabilidad de transitar de un vector (v) a (w) 
def probaTransitar(v,w):
    tamaño = len(v) 
    bra = [(0,0)] * tamaño
    for j in range (tamaño):
        bra[j] = lc.conjComp(w[j])
    amplitudT = (0,0)
    for i in range(tamaño):
        amplitudT = lc.sumaComp(amplitudT , lc.producComp(v[i],bra[i]))
    return amplitudT

#segundo reto de programación
def mediaVarianza(matriz,y):
    tamaño = len(y)
    
    matrizMedia = [[(0,0) for i in range (tamaño)] for i in range (tamaño)]
    varianza = (0,0)
    q = [[(0,0) for i in range (tamaño)] for i in range (tamaño)]
    w = [(0,0)]*tamaño
    bra = [(0,0)] * tamaño
    x = [(0,0)] * tamaño
    for i in range (tamaño):
        x[i] = y[i]
    media = (0,0)
    if lE.matHer(matriz) == False:
        return "no es hermitanea"
    else:
        w = lE.accionMacVec(matriz,y)
        for j in range (tamaño):
            bra[j] = lc.conjComp(w[j])
        for i in range(tamaño):
            media = lc.sumaComp(media , lc.producComp(bra[i],y[i]))
        matrizMedia = lE.multEscMat(lE.diagonal(tamaño),media)
        q = lE.restamatrix(matriz,matrizMedia)
        q = lE.producMat(q,q)
        for i in range (tamaño):
            y[i] = lc.conjComp(y[i])
        y = lE.accionMacVec(lE.transpuesta(q),y)
        for i in range(tamaño):
            varianza = lc.sumaComp(varianza , lc.producComp(y[i],x[i]))
    return varianza

#tercer reto de programación
def valPropiVecPropi(matriz,psi):
    tamaño =len(matriz)
    psiC = [(0,0)] * tamaño
    m = [[(0,0) for i in range (tamaño)] for i in range (tamaño)]
    z = [[(0,0) for i in range (tamaño)] for i in range (tamaño)]
    for i in range (tamaño):
        psiC[i] = lc.conjComp(psi[i])
    for i in range (tamaño):
        psiC[i] = lc.imaginarioJ(psiC[i])
    for i in range (tamaño):
        for j in range (tamaño):
            m[i][j] = lc.imaginarioJ(matriz[i][j])
    mat = np.array(m)
    valoresPropios, vectoresPropios = np.linalg.eig(mat)   
    for i in range (tamaño):
        for j in range (tamaño):
            z[j][i] = (psiC[i]*vectoresPropios[i])
    for i in range (tamaño):
        print((LA.norm(z[i])**2))
    return valoresPropios

#curto reto, estado final 
def estados(m,v,clk):
    for i in range (clk):
        v = lE.accionMacVec(m,v)
    return v

#problemas 
#4.4.1/verificar si ambas son unitarias y si su producto da una matriz unitaria
def cuatroUno(v,w):
    tamaño = len(v)
    z = [[(0,0) for i in range (tamaño)] for i in range (tamaño)]
    if lE.matUnit(v) and lE.matUnit(w) == False:
        print("no son unitarias")
    else:
        z = lE.producMat(lE.transpuesta(v),w)
        if lE.matUnit(z):
            print("el producton es unitario")
        else:
            print("el producto no es unitario")

#4.4.2 determine el estado del sistema de billar despues de 3 puntos
def cuatroDos(w,clk,v):
    tamaño = len(w)
    matrizFut = [[(0,0) for i in range (tamaño)] for i in range (tamaño)]
    matrizFut = w
    for i in range (clk-1):
        matrizFut = lE.producMat(matrizFut,w)
    vecProb = lE.accionMacVec(matrizFut,v)
    print(vecProb)

#4.5.2 determinar si es separable o no 
def cincoDos(v,w):
    tamañox = len(v)
    tamañoy = len(w)
    k = 0
    tamañoComp = tamañox * tamañoy
    psi = [(0,0)] * tamañoComp
    for i in range (tamañox):
        for j in range (tamañoy):
            psi[k] = lE.producMat(v[i],w[j])
            k =+ 1
    print(psi) #cada casilla representara el valor complejo que compaña a |xi> x|yi>


#4.5.3 determinar si el sistema es sepaarable 
#el vector a entregar es el vector de las constantes C 
def cincoTres(v):
    c0 = 1
    cx0 = 1
    c1 = 1
    cx1 = 1
    if v[0] == 0:
        c0 = 0
        cx0 = 0
    if v[1] == 0:
        c0 = 0
        cx1 = 0
    if v[2] == 0:
        c1 = 0
        cx0 = 0
    if v[3] == 0:
        c1 = 0
        cx1 = 0
    if c0 == 1 or cx0 == 1 or c1 == 1 or cx1 == 1:
        print("es separable")
    else:
        print("no es separable")
    

if __name__ == '__main__':
        #punto 4.4.1
    x = [[(0,0),(1,0)],
         [(1,0),(0,0)]]
    z = [[((2**(1/2)/2),0),((2**(1/2)/2),0)],
         [((2**(1/2)/2),0),(-(2**(1/2)/2),0)]]
    #cuatroUno(x,z)

        #punto 4.4.2
    x = [[(0,0),(1/(2**(1/2)),0),(1/(2**(1/2)),0),(0,0)],
         [(1/(2**(1/2)),0),(0,0),(0,0),(1/(2**(1/2)),0)],
         [(1/(2**(1/2)),0),(0,0),(0,0),(1/(2**(1/2)),0)],
         [(0,0),(1/(2**(1/2)),0),(-1/(2**(1/2)),0),(0,0)]]
    v = [(1,0),(0,0),(0,0),(0,0)]
    #cuatroDos(x,3,v)

        #punto 4.5.2
    #cincoDos()

        #punto 4.5.3
    v = (0,1,0,1)
    cincoTres(v)
