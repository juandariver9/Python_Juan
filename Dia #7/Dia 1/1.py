#--------------------- Funciones def <nombre>(): ----------------
#Sin parametros y sin retorno
def SinSin():
    print("Hola Mundo!")
SinSin()
#Sin parametros y con retorno
def SinCon():
    c = 3 + 5
    return c
print(SinCon())
#Con Parametors y sin retorno
def ConSin(a, b):
    c = a + b
    print("La suma es: ", c)
ConSin(10,20)
#Con Parametros y Con retorno
def ConCon(x,y):
    n = x / y
    return round(n,2) #round es pa redondear dahh, y el 2 es para cuantos decimales se dejan