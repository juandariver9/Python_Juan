num1 = int(input("menor "))
num2 = int(input("mayor "))
menor = num1
mayor = num2


MCD = 1
MCM = 1

for i in range(2, menor + 1,1):
    while num1%i==0 and num2%i==0:
        MCD = MCD*i
        num1 = num1/i
        num2 = num2/i
MCM = (mayor*menor)/MCD

print(f"el maximo común divisor de {mayor} y {menor} es {MCD}")