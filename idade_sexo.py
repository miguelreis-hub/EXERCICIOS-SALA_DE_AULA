import os
os.system("cls")

maior_idade = 0
qtd_de_homems = 0

soma_das_idades_homems = 0

menor_idade_mulher = 999

qtd_de_mulher = 0


while True:

    sexo = input("Digite seu sexo = ").strip().lower()
    idade = int(input("Digite sua idade = "))

    if idade > maior_idade:
        maior_idade = idade

    if sexo == "f":
        
        qtd_de_mulher += 1
        if idade < menor_idade_mulher:
            
            menor_idade_mulher = idade
    
    if sexo == "m":
        qtd_de_homems += 1
        soma_das_idades_homems += idade

    opcao = input("Deseje continuar = ").strip().lower()

    if opcao == "n":
        break


if qtd_de_mulher == 0:
    menor_idade_mulher = 0

if qtd_de_homems > 0:
    
    media_idade_dos_homems = soma_das_idades_homems / qtd_de_homems
else:
    media_idade_dos_homems = 0
    



print(f"A maior idade lida é = {maior_idade}")
print(f"A quantidade de homems cadastrados foram = {qtd_de_homems}")
print(f"A idade da mulher mais jovem é = {menor_idade_mulher}")
print(f"A media de idade entre os homems é = {media_idade_dos_homems}")

