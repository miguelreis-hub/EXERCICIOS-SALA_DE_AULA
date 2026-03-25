import os 

os.system("cls")

vetor_numero = []


for i in range (1,6,1):
    
    numero = int(input("Digite numeros = "))
    
    vetor_numero.append(numero)


maior_nota = max(vetor_numero)
menor_nota = min(vetor_numero)


for i in range(len(vetor_numero)): ## exibir na tela os valores digitados pelo usuario
    
    print(f"OS valores digitados pelo usuario são = {vetor_numero[i]}")

print(f"A maior nota presente no vetor é = {maior_nota}")
print(f"A menor nota presente no vetor é = {menor_nota}")


    
    