n, t = map(int, input("Enter n and t: ").split())
tipoMoneda = []
me2=[]
for i in range(n):
    tipoMoneda.append(int(input()))
for i in range(t):
    me2.append(int(input()))


print("monedas:", tipoMoneda)
print("mesas:", me2)

mayor = max(tipoMoneda)

print(mayor)

x = mayor
import math


for i in range(t):
    T_n = me2[0]
    me2[0]+1
    if x <= T_n:
        x = mayor + mayor
        

print(x)


for i in range(t):
    T_n = me2[0]
    me2[0]+1
    if x >= T_n:
        y = mayor + mayor

print(y)