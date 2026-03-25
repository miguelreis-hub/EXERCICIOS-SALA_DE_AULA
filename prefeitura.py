import os 
os.system("cls")

qtd_de_familia = 0

soma_total_de_familia = 0

maior_salario = 0

menor_salario = 0

soma_dos_fihlos = 0

soma_dos_salarios = 0

i = 0

while True:
    
    print("""
Código|  Descrição
    1 |   Adicionar família
    2 |   Sair e exibir resultados
""")
    
    opcao = int(input("Digite a opção desejada = "))
    
    i += 1
    
    match opcao:
        
        case 1:
            
            salario = float(input("Digite o salario da familia = "))
            filhos = int(input("Digite a quantidade de filhos existente = "))
            
            soma_dos_salarios += salario
            soma_dos_fihlos += filhos
            qtd_de_familia +=1
            
            
            
            if i == 1:
                
                maior_salario = salario
                
                menor_salario  = salario
                
            else:
                
                if salario > maior_salario:
                    
                    maior_salario = salario
                
                if  salario < menor_salario:
                    
                    menor_salario = salario
        
        case 2:
            print("Exibindo resultados................")
            
            if soma_dos_salarios == 0 or qtd_de_familia == 0:
                
                media_de_salario = 0
                
            else:
                
             media_de_salario = soma_dos_salarios / qtd_de_familia
            
            if soma_dos_fihlos == 0 or qtd_de_familia == 0 :
                
                media_de_filho = 0
                
            else:
                
             media_de_filho = soma_dos_fihlos / qtd_de_familia
            
            print(f"O total de familias que responderam foram = {qtd_de_familia} familias")
            print(f"A media de salario da população foi de = {media_de_salario:.1f}R$")
            print(f"A media de filhos por familia é de = {media_de_filho} filhos")
            print(f"O maior salario é = {maior_salario:.1f}R$")
            print(f"O menor salario é = {menor_salario:.1f}R$") 
            
            break
        
        case _:
            
            print("Opção invalida, tente novamente...............")               