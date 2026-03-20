import os 
os.system("cls")

nome_pessoa_velha = ""

mulher_mais_jovem = ""

maior_idade = 0
menor_idade = 999

qtd_de_pessoas = 0

qtd_de_homems_30 = 0 

qtd_de_mulhere_menos_18 = 0

soma_das_idades_totais = 0

qtd_mulheres = 0
qtd_homems = 0


while True:

    nome_da_pessoa = input("Digite seu nome = ").strip().lower()
    idade = int(input("Digite sua idade = "))
    sexo = input("Digite seu sexo = ").strip().lower()

    soma_das_idades_totais += idade

    qtd_de_pessoas += 1

    if idade > maior_idade:
        maior_idade = idade
        nome_pessoa_velha = nome_da_pessoa
    
    if sexo == "f":

        qtd_mulheres +=1

        if idade < menor_idade:
            menor_idade = idade
            mulher_mais_jovem = nome_da_pessoa
        
        if idade < 18:
            qtd_de_mulhere_menos_18 += 1
    
    if sexo == "m":

        qtd_homems += 1

        if idade > 30:
            qtd_de_homems_30 += 1

    opcao = input("Voçe deseja continuar =").strip().lower()

    if opcao == "n":
        break
    else:
        continue


if qtd_homems == 0:

    qtd_de_homems_30 = 0

if qtd_mulheres == 0:

    mulher_mais_jovem = 0
    
    qtd_de_mulhere_menos_18 = 0


media_total = soma_das_idades_totais / qtd_de_pessoas

print(f"O nome da pessoa mais velha é = {nome_pessoa_velha}")
print(f"O nome da mulher mais jovem é = {mulher_mais_jovem}")
print(f"A media d idade do grupo é = {media_total:.1f}")
print(f"A quantidade de homems que tem mais de 30 anos é = {qtd_de_homems_30}")
print(f"A quantidade de mulheres com menos de 18 é = {qtd_de_mulhere_menos_18}")



