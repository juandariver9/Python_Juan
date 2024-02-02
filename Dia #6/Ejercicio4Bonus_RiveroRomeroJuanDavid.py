import math

def Colision(bola1, bola2):
    x1, y1 ,r1 = bola1
    x2, y2,r2 = bola2

    distance_euclides = math.sqrt((x2 - x1)**2 + (y2 - y1)**2) 
    print(distance_euclides)

    return distance_euclides <= r1 + r2

bola1 = (2, 6 , 2)
bola2 = (2, 2, 2)

print(Colision(bola1, bola2))

#Desarrollado por Juan David Rivero Romero 1096701639
#Ayudantes: Daniel Latorre, Joel Santiago, Kenia Hernandez, Andres daza, Paulita y Nekotina(bot de musica)
# :DDDD