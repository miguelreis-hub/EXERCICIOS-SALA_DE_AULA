import os 
os.system("cls")


vetor_numeros_positivos = []

qtd_negativo = 0


for i in range(1,6,1):
    
    numero = int(input("Digite um numero = "))
    
    
    
    if numero < 0:
        
        qtd_negativo +=1
    else:
        
        vetor_numeros_positivos.append(numero)


soma_dos_positivos = sum(vetor_numeros_positivos)


print(f"O vetor com numeros positivos preenchidos = {vetor_numeros_positivos}")

print(f"A quantidade de numeros negativos = {qtd_negativo}")

print(f"A soma dos numeros positivos é = {soma_dos_positivos}")






