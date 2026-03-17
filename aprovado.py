import os 

os.system("cls")

soma_das_notas = 0
for i in range(1,4,1):
    
    nota_aluno = float(input(f"Digite sua nota {i} = "))
    
    soma_das_notas += nota_aluno
    
media_do_aluno = soma_das_notas / 3

if media_do_aluno >= 7:
    print(f"Sua media = {media_do_aluno:.1f}")
    print(" ARPOVADO")
    
if media_do_aluno < 7 and media_do_aluno > 4:
    
    print(f"Sua media = {media_do_aluno:.1f}")
    
    print("RECUPERAÇÃO")
    
if media_do_aluno < 4:
    
    print(f"Sua media = {media_do_aluno:.1f}")
    
    print("REPROVADO")