import os
os.system("cls")

vetor_notas = []

for i in range(1,5,1):
    
    nota = int(input(f"Digite sua nota {i}= "))
    
    vetor_notas.append(nota)


for i in range(len(vetor_notas)):
    
    print(f"Nota {i+1} = {vetor_notas[i]}")

media = sum(vetor_notas) / len(vetor_notas)


if media >= 7:
    
    print("APROVADO")

if media >=5:
    
    print(f"RECUPERAÇÂO")

if media <= 5:
    
    print(f"Reprovado")
    
    
    