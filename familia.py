import os 
os.system("cls")

total_de_familia = 0

soma_dos_salarios = 0

soma_dos_filhos = 0

total_filhos = 0

maior_salario = 0

menor_salario = 0

quantidade_filhos = 0

c = 0

while True:

    print("""
    === MENU ===
    codigo | Descrição
       1   | Adicionar familia
       2   | Sair e  exibir resultados
        """)
    opcao = int(input("Digite uma das opções = "))

    match opcao:

        case 1:

            salario = float(input("Digite o salario da familia = "))
            filhos = int(input("Digite a quantidade de filhos = "))


            total_de_familia += 1
            soma_dos_salarios += salario
            soma_dos_filhos += filhos
            quantidade_filhos += 1
            c += 1


            if c == 1:

                maior_salario = salario
                menor_salario = salario
            
            if salario > maior_salario:

                maior_salario = salario
            
            if salario < menor_salario:

                menor_salario = salario
        
        case 2:

            os.system("cls")
            media_salario_familias = soma_dos_salarios / total_de_familia
            media_dos_numeros_filhos = soma_dos_filhos / quantidade_filhos

            print(f"O numero total de familias que responderam a pesquisa foi = {total_de_familia}")
            print(f"A media salarial da população foi de = {media_salario_familias:.2f}")
            print(f"A media de numeros de filho foi de = {media_dos_numeros_filhos:.1f}")
            print(f"O maior salario foi de = {maior_salario:.2f}")
            print(f"O menor salario foi de = {menor_salario:.2f}")

            break