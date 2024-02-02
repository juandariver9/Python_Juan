import math

def Colision(bola1, bola2):
    x1, y1, z1 ,r1 = bola1
    x2, y2, z2 ,r2 = bola2

    distance_euclides = math.sqrt((x2 - x1)**2 + (y2 - y1)**2) + (z2 - z1)**2
    print(distance_euclides)

    return distance_euclides <= r1 + r2

bola1 = (6.5, 2, 4 , 2)
bola2 = (6.5, 2, 2, 2)

print(Colision(bola1, bola2))

#Ayudantes: Daniel Latorre, Joel Santiago, Kenia Hernandez, Andres daza, Paulita, Juan David y Nekotina(bot de musica)
# :DDDD