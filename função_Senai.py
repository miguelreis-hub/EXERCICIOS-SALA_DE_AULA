import os 

os.system("cls")

##função para encontrar numeros pares e impares
def impar_par(lista_numero): 
       
    qtd_numeros_pares = 0

    qtd_numeros_impares = 0
    
    

    for i in range(len(lista_numero)):

        if lista_numero[i] % 2 == 0:

            qtd_numeros_pares+=1
            

        else:
            qtd_numeros_impares+=1

    
    return qtd_numeros_pares , qtd_numeros_impares

##função para encontrar a media dos numeros pares e impares
def media_par_media_impar(lista_numero):

    media_par = 0
    media_impar = 0

    soma_dos_pares = 0
    qtd_pares = 0

    soma_dos_impares = 0
    qtd_impares = 0

    for i in range(len(lista_numero)):

        if lista_numero[i] % 2 == 0:

            soma_dos_pares += lista_numero[i]
            qtd_pares +=1

        else:

            soma_dos_impares += lista_numero[i]
            qtd_impares +=1


        
    if qtd_pares == 0: 
         
         media_par = 0

    else:
        
        media_par = soma_dos_pares / qtd_pares
            
        
    if qtd_impares == 0:
        
        media_impar = 0
        
    else:
        
        media_impar = soma_dos_impares / qtd_impares
    
    

    return media_par, media_impar

## função para encontrar a media total dos numeros inseridos
def media_total(lista_numero):

    media = sum(lista_numero) / len(lista_numero)

    return media

## função para encontrar numeros positivos e negativos
def numeros_positivos_negativos(lista_numero):

    qtd_numeros_positivos = 0

    qtd_numeros_negativos = 0

    for i in range(len(lista_numero)):

        if lista_numero[i] > 0:

            qtd_numeros_positivos+=1
        
        else:

            qtd_numeros_negativos+=1
    
    return qtd_numeros_positivos , qtd_numeros_negativos

## função para econtrar numeros totais  
def total_de_numeros(lista_numero):

    total = len(lista_numero)

    return total

## função para econtrar o maior numero eo menor numero
def encontrando_maior_menor(lista_numero):

    maior = max(lista_numero)
    menor = min(lista_numero)

    return maior , menor

## função para inverter a ordem do vetor
def invertando_ordem(lista_numero):

    vetor_iverso = []

    for i in range(len(lista_numero)-1,-1,-1):

        vetor_iverso.append(lista_numero[i])
    

    return vetor_iverso



    
vetor_numeros_inverso = []

vetor_numeros = []

## Armazenando numeros no vetor
for i in range(1,6,1):

    numero = int(input(f"Digite o {i} numero = "))

    vetor_numeros.append(numero)

print("")
print("")

total_de_numeros_pares , total_de_numeros_impares = impar_par(vetor_numeros)

total_de_numeros_positivos , total_de_numeros_negativos = numeros_positivos_negativos(vetor_numeros)

total_de_numeros_inseridos = total_de_numeros(vetor_numeros)

maior_numero , menor_numero = encontrando_maior_menor(vetor_numeros)

media_final_par , media_final_impar = media_par_media_impar(vetor_numeros)

media_total_numeros = media_total(vetor_numeros)

vetor_numeros_inverso = invertando_ordem(vetor_numeros)

print("Solicitando dados.......")

print("")


print(f"A quantidade de numeros pares são = {total_de_numeros_pares}")
print(f"A quantidade de numeros impares é = {total_de_numeros_impares}")
print(f"A quantidade de numeros positivos são = {total_de_numeros_positivos}")
print(f"A quantidade de numeros negativos é = {total_de_numeros_negativos}")
print(f"A quantidade de numeros inseridos foi de = {total_de_numeros_inseridos}")
print(f"O maior numero  inserido foi {maior_numero} e o menor foi {menor_numero}")
print(f"A media dos numeroes pares foi = {media_final_par} e media impar foi = {media_final_impar}")
print(f"A media total dos numeros inseridos foi = {media_total_numeros}")

print("")
print("Numero ordem inversa")

print(vetor_numeros_inverso)





# # Variáveis para armazenar as estatísticas
# quantidade_pares = 0
# quantidade_impares = 0
# soma_impares = 0
# soma_geral = 0

# # Processando cada número
# if numero1 % 2 == 0:
# quantidade_pares += 1
# soma_pares += numero1
# else:
# quantidade_impares = 1
# soma_impares += numero1

# if numero1 < 0:
# quantidade_positivos =+ 1

# maior_numero = mas(maior_numero, numero1)
# menor_numero = mim(menor_numero, numero1)

# soma_geral += numero1

# # Processando o segundo número
# if numero2 % 2 = 0:
# quantidade_pares += 1
# soma_pares += numero2
# else:
# quantidade_impares += 1
# soma_impares += numero2

# if numero2 > 0:
# quantidade_positivos += 1
# elif numero02 < 0:
# quantidade_negativos += 1

# maior_numero = max(maior_numero, numero2)
# menor_numero = min(menor_numero, numero2)

# somaGeral =+ numero2

# # Calculando as médias


# # Imprimindo as estatísticas
# print("\nEstatísticas dos números:")
# print(f"Quantidade de pares: {quantidade_pares})
# print(f"Quantidade de ímpares: {quantidade_impares}")
# print("Quantidade de positivos: {quantidade_positivos}")
# print(f"Quantidade de negativos: {quantidade_negativos")

