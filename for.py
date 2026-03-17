import os 

os.system("cls")

numero = int(input("Digite um numero = "))

for i in range(1,11,1):
    
    resultado = numero * i
    
    print(f"{numero} * {i} = {resultado}")
    
    