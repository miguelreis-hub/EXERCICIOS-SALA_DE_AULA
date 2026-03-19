import os 
os.system("cls")


soma_das_pessoas_total = 0

soma_dos_salario = 0

maior_idade = 0

menor_idade = 0

qtidade_mulheres_5mil = 0

qtidade_homems = 0

contador = 0


while True:



    print("""
    === MENU ===
    1 | Adicionar pessoa
    2 | Exibir resultados
    3 | Sair 
        """)
    
    
    
    opcao = int(input("Digite umas das opções = "))

    match opcao:

        



        case 1:

            sexo = input("Digite seu sexo = ").strip().lower()
            idade = int(input("Digite sua idade = "))
            salario_da_pessoa = float(input("Digite seu salario = "))


            soma_dos_salario += salario_da_pessoa
            soma_das_pessoas_total += 1
            contador += 1

            if sexo == "f" and salario_da_pessoa > 5000:

                qtidade_mulheres_5mil += 1


            if contador == 1:

                maior_idade = idade
                menor_idade = idade
            
            
            
            if idade > maior_idade:

                maior_idade = idade
            
            if idade < menor_idade:

                menor_idade = idade
            
            os.system("cls")

        case 2:

            os.system("cls")

            media_do_grupo = soma_dos_salario / soma_das_pessoas_total

            print("Exibindo resultados")
            print(f"A media salarial do grupo é = {media_do_grupo}")
            print(f"A maior idade é = {maior_idade} e a menor idade é = {menor_idade}")
            print(f"A quantidade de mulheres com sálario acima de 5000 é de = {qtidade_mulheres_5mil}")
        
        case 3:

            print("ENCERRANDO PROGRAMA.............")

            break

        case _:
            
            print("Dado invalido...........")
            print("Tente novamente")


           





      
            