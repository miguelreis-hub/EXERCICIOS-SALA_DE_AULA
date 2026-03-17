import os

os.system("cls")


soma_das_notas = 0

nome = 4
for i in range(1,nome+1):
    
    notas = float(input(f"Digite sua nota {i} = "))
    
    soma_das_notas += notas

media = soma_das_notas / 4

print(f"A soma das notas é = {soma_das_notas}")
print(f"A media final do aluno é = {media:.1f}")
    
    