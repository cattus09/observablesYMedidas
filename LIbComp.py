import math

def sumaComp(a, b):
    real = a[0] + b[0]
    imaginario = a[1] + b[1]
    return (real, imaginario)

def restaCom(a, b):
    real = a[0] - b[0]
    imaginario = a[1] - b[1]
    return (real, imaginario)

def producComp(a, b):
    real = a[0]*b[0] - a[1]*b[1]
    imaginario = a[0]*b[1] + a[1]*b[0]
    return (real, imaginario)

def divComp(a,b):
    real = (a[0]*b[0] + a[1]*b[1])/(b[0]**2 + b[1]**2)
    imaginario = (a[1]*b[0] - a[0]*b[1])/(b[0]**2 + b[1]**2)
    return (real, imaginario)

def modComp(a):
    modA = (a[0]**2 + a[1]**2)**(1/2)
    return (modA)

def conjComp(a):
    real = a[0]
    imaginario = -a[1]
    return (real, imaginario)

def polComp(a):
    modulo = (a[0]**2 + a[1]**2)**(1/2)
    fase = math.atan(a[1]/a[0])
    return (modulo, fase)

def faseComp(a):
    fase = math.atan(a[1] / a[0])
    return (fase)

if __name__ == '__main__':
    a = (2.5, 4.7)
    b = (4.76, 5.48)
    print(sumaComp(a,b))
    print(restaCom(a,b))
    print(producComp(a,b))
    print(divComp(a,b))
    print(modComp(a))
    print(conjComp(a))
    print(polComp(a))
    print(faseComp(a))


