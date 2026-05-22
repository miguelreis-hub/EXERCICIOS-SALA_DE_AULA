import os 
os.system("cls")
from dataclasses import dataclass

@dataclass

class Reserva:
    nome_passageiro:str
    numero_aviao:int




vetor_avioes = []
vetor_assentos =[]
vetor_reservas = []
reserva_global = 0





while True:
    print("")

    print("""
1: Registrar o número de cada avião
2: Registrar o quantitativo de assentos disponíveis em cada avião
3: Reservar passagem aérea
4: Realizar consulta por avião
5: Realizar consulta por passageiro
6: Encerrar sistema

""")
    print("")

    opcao = int(input("Digite á opção desejada = "))

    match opcao:
        case 1:
            print("")
            print("Registro-Aviões")
            print("")

            for i in range(4):

                identificador_aviao = int(input(f"Registre o avião {i+1} =  "))
                vetor_avioes.append(identificador_aviao)
            
            print("")
            print("Aviões registrado com sucesso!")
        
        case 2:
            print("")
            print("Registrador de Assentos")
            print("")

            for i in range(4):

                assentos_avioes = int(input(f"Registre á quantidade de assentos disponiveis no avião {vetor_avioes[i]} =  "))
                vetor_assentos.append(assentos_avioes)
            
            print("")
            print("Registro de assentos realizado com sucesso!")

        
        case 3:
            print("")
            print("Resevar passagem aerea")
            print("")


            if reserva_global == 20:
                print("")
                print("Reserva alcançou limite maximo!")
                continue
            
            else:

                aviao_encontrado = False ## Ate agora aviao não encontrado

                identificador_aviao = int(input("Digite o numero do avião para reserva = "))
                print("")

                for indice, aviao in enumerate(vetor_avioes): ## vai devolver o indice do aviao encontrado

                    if aviao == identificador_aviao:

                        print("")

                        aviao_encontrado = True

                        print(f"Este avião existe! {vetor_avioes[indice]} ")

                        print("")

                        print("Verificando vaga!")

                        if vetor_assentos[indice] > 0:
                            print("")
                            print(f"Vaga disponiveis! = {vetor_assentos[indice]}")
                            print("")

                            reserva = Reserva(
                                nome_passageiro = input("Digite o nome do passageiro = ").strip().lower(),
                                numero_aviao = vetor_avioes[indice]
                            )

                            vetor_reservas.append(reserva)

                            vetor_assentos[indice]-=1

                            print("")
                            print("Reserva realizada com sucesso!")
                            reserva_global+=1
                    
                        else:
                            print("")
                            print("Vaga alcançou limite maximo!")
            
                if aviao_encontrado == False:
                    print("")
                    print("Avião não econtrado tente novamente!")
                    continue


        case 4:
            print("")
            print("Consulta - avião!")
            print("")

            encontrou_aviao = False ## aviao não encontrado
            reserva_encontrada = False ## Reserva não encontrada

            identificador_aviao = int(input("Digite o numero do avião para á consulta = "))

            for indice, aviao in enumerate(vetor_avioes):

                if aviao == identificador_aviao:
                    print("")
                    print(f"Avião encontrado! - {vetor_avioes[indice]}")

                    encontrou_aviao = True

                    for i, reserva in enumerate(vetor_reservas):
                        
                        if reserva.numero_aviao == identificador_aviao:
                            print("")
                            print("Reservas presentes!")
                            reserva_encontrada = True
                            print("")
                            print(f"Numero avião: {reserva.numero_aviao}")
                            print(f"Nome:{reserva.nome_passageiro}")
                            print("")
                        
                    if reserva_encontrada == False:
                        print("")
                        print("Reserva não encontrada!")
                        continue
                        

            if encontrou_aviao == False:
                print("")
                print("Aviao não encontrado!")
                continue

        case 5:
            print("")
            print("Resevar - Passageiro")
            print("")

            encontrou_passageiro = False ## Passageiro não encontrado!

            passageiro = input("Digite o nome do passageiro = ").strip().lower()

            for i, reserva in  enumerate(vetor_reservas):

                if reserva.nome_passageiro == passageiro:
                    encontrou_passageiro = True
                    print("")
                    print(" Passageiro encontrado - Exibindo - reserva!")
                    print("")
                    print(f"Nome:{reserva.nome_passageiro}")
                    print(f"Aviao:{reserva.numero_aviao}")
                    print("")
            
            if encontrou_passageiro == False:
                print("")
                print("Passageiro não encontrado !")
                continue

            


        
        case 6:
            print("")
            print("Encerrando Sistema......")
            break

        case _:
            print("")
            print("Dado invalido tente novamente!")