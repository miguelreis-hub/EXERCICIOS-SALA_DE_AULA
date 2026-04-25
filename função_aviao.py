import os 
os.system("cls")

def exibir_menu():

    print("""
          
 1: Registrar o número de cada avião.
 2: Registrar o quantitativo de assentos disponíveis em cada avião.
 3: Reservar passagem aérea.
 4: Realizar consulta por avião.
 5: Realizar consulta por passageiro.
 6: Encerrar sistema.          
    """)




vetor_avioes = []
vetor_assentos = []
nome_do_passageiro = []
numero_aviao_reserva = []

reservar_passagem = 0

while True:


    exibir_menu()

    opcao = int(input("Digite a opção desejada = "))

    match opcao:

        case 1:
            print("")
            print("")

            for i in range(4):

                numero_do_aviao = int(input(f"Digite o numero do aviao {i + 1} = "))

                vetor_avioes.append(numero_do_aviao)


            print("")
            print("Cadastro de aviões concluido")
        
        case 2:
            print("")
            print("")

            for i in range(4):

                assento_disponivel = int(input(f"Digite a quantidade de assentos disponivel no avião {vetor_avioes[i]} = "))

                vetor_assentos.append(assento_disponivel)

            print("")
            print("Cadastro de assentos concluidos")
        
        case 3:

            print("")
            print("")

            if reservar_passagem == 20:
                print("Limite de reserva atingido")
                break


            aviao_existente = int(input("informe o numero do avião = "))

            if aviao_existente == vetor_avioes[0]:

                if vetor_assentos[0] <= 0:

                    print(f"Não há assentos disponíveis para este avião {vetor_avioes[0]} assento disponiveis = {vetor_assentos[0]}")
                
                else:

                    nome = input("Digite o seu nome = ").strip().lower()
                    nome_do_passageiro.append(nome)

                    numero_aviao_reserva.append(vetor_avioes[0])

                    reservar_passagem+=1

                    print(f"Reserva realizada no aviao {vetor_avioes[0]} com sucesso!")
                    
                    vetor_assentos[0] -=1

                    print(f"No avião {vetor_avioes[0]} possui {vetor_assentos[0]} vagas ")





                
            
            elif aviao_existente == vetor_avioes[1]:

                if vetor_assentos[1] <= 0:

                    print(f"Não há assentos disponíveis para este avião {vetor_avioes[1]} assento disponiveis = {vetor_assentos[1]}")
                
                else:

                    nome = input("Digite o seu nome = ").strip().lower()
                    nome_do_passageiro.append(nome)
                    reservar_passagem+=1
                    numero_aviao_reserva.append(vetor_avioes[1])

                    print(f"Reserva realizada no aviao {vetor_avioes[1]} com sucesso!")
                    
                    vetor_assentos[1] -=1

                    print(f"No avião {vetor_avioes[1]} possui {vetor_assentos[1]} vagas ")



                
            
            elif aviao_existente == vetor_avioes[2]:

                if vetor_assentos[2] <= 0:

                    print(f"Não há assentos disponíveis para este avião {vetor_avioes[2]} assento disponiveis = {vetor_assentos[2]}")
                
                else:

                    nome = input("Digite o seu nome = ").strip().lower()
                    nome_do_passageiro.append(nome)
                    reservar_passagem+=1
                    numero_aviao_reserva.append(vetor_avioes[2])

                    print(f"Reserva realizada no aviao {vetor_avioes[2]} com sucesso!")
                    
                    vetor_assentos[2] -=1

                    print(f"No avião {vetor_avioes[2]} possui {vetor_assentos[2]} vagas ")

                print("")
            
            elif aviao_existente == vetor_avioes[3]:

                if vetor_assentos[3] <= 0:

                    print(f"Não há assentos disponíveis para este avião {vetor_avioes[3]} assento disponiveis = {vetor_assentos[3]}")
                
                else:

                    nome = input("Digite o seu nome = ").strip().lower()
                    nome_do_passageiro.append(nome)
                    reservar_passagem+=1
                    numero_aviao_reserva.append(vetor_avioes[3])

                    print(f"Reserva realizada no aviao {vetor_avioes[3]} com sucesso!")
                    
                    vetor_assentos[3] -=1

                    print(f"No avião {vetor_avioes[3]} possui {vetor_assentos[3]} vagas ")

            
            
            else:

                print("")

                print("Este avião não existe!")
                continue

        
        case 4:

            print("")
            print("Consultas e Relatórios")

            aviao_existe = int(input("Digite o numero do avião para consulta = "))

            if aviao_existe == vetor_avioes[0]:

                for i in range(len(numero_aviao_reserva)):

                    if numero_aviao_reserva[i] == vetor_avioes[0]:
                        print(f"Passageiro:{nome_do_passageiro[i]}")

            
            if  aviao_existe == vetor_avioes[1]:

                for i in range(len(numero_aviao_reserva)):

                    if numero_aviao_reserva[i] == vetor_avioes[1]:
                        print(f"Passageiro:{nome_do_passageiro[i]}")
            
            if aviao_existe == vetor_avioes[2]:

                for i in range(len(numero_aviao_reserva)):

                    if numero_aviao_reserva[i] == vetor_avioes[2]:
                        print(f"Passageiro:{nome_do_passageiro[i]}")
            
            if aviao_existe == vetor_avioes[3]:

                for i in range(len(numero_aviao_reserva)):

                    if numero_aviao_reserva[i] == vetor_avioes[3]:
                        print(f"Passageiro:{nome_do_passageiro[i]}")
            
            else:

                print("Não há reservas realizadas para este avião!")
        
        case 5:

            print("")
        

        case 6:

            break
            
            
            
            


           

                    


            

