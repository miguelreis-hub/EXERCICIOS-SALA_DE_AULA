import os
os.system("cls")


vetor_numeros = []

qtd_de_pares = 0
qtd_de_impares = 0

for i in range(1,7,1):
    
    numero = int(input("Digite os numeros = "))
    
    vetor_numeros.append(numero)
    
    if numero % 2 == 0:
        
        qtd_de_pares +=1
        
    else:
        
        qtd_de_impares +=1



for i in range(len(vetor_numeros)):
    
    print(f"Os numeros citados foram = {vetor_numeros[i]}")


print(f"A quantidade de numeros pares são = {qtd_de_pares}")
print(f"A quantidade de numeros impares são = {qtd_de_impares}")
        
    