import os 
os.system("cls")

from dataclasses import dataclass

@dataclass

class Jogo:
    nome:str
    valor:float
    quantidade:int

    # def mostrar(self):
    #     print("")
    #     print("Exibindo - Dados")
    #     print("")
    #     print(f"Nome:{self.nome}")
    #     print(f"Tipo:{self.tipo}")
    #     print(f"Valor:{self.valor:.2f}R$")
    #     print(f"Quantidade:{self.quantidade}")
    


def exibir_dados(lista_de_jogos,nome_do_jogo):

    for jogo in lista_de_jogos:

        if jogo.nome == nome_do_jogo:
            print("")
            print(f"Exibindo dados - {jogo.nome} ")
            print(f"valor:{jogo.valor:.2f}R$")
            print(f"Quantidade restante:{jogo.quantidade}")
            print("")
            print("Jogo listado com sucesso!")

            return
        
    
    else:
            print("")
            print("Jogo não encontrado - tente novamente!")
            print("")



def remover_unidade_jogo(lista_de_jogos, nome_do_jogo, quantidade):

    for jogo in lista_de_jogos:

        if jogo.nome == nome_do_jogo:

            if quantidade > jogo.quantidade:
                print("")
                print("Não foi possível remover, valor maior que o estoque!")
                print("")

            else:
                jogo.quantidade -= quantidade
                print("")
                print("Unidade do jogo removida com sucesso!")

            return  # ← fora dos ifs internos, dentro do for

    # ← fora do for, só roda se não achou nenhum jogo
    print("")
    print("Jogo não encontrado! - tente novamente")


def adicinando_unidade(lista_de_jogos,nome_do_jogo,quantidade):

    for jogo in lista_de_jogos:

        if jogo.nome == nome_do_jogo:

            jogo.quantidade += quantidade

            print("")
            print("Adicinado unidades com sucesso!")
            print("")

            return
        

    print("")
    print("jogo não encontrado - tente novamente")
    print("")


lista_de_jogo_organizado = []
lista_de_jogos = []

while True:
    print("")

    print("""
1-Adicionar - jogo - Sistema
2-Remover - jogo
3-Listar - jogo
4-Adicinar - unidade - jogo
5-Salvar - Arquivo
6-Sair
          """)
    print("")
    
    opcao = int(input("Digite á opção desejada = "))

    match opcao:

        case 1:
            print("")
            print("Adicionar - jogo")
            print("")

            while True:
                print("")

                jogo = Jogo(
                    nome = input("Digite o nome do jogo = ").strip().lower(),
                    valor = float(input("Digite o valor do jogo = ")),
                    quantidade = int(input("Digite á quantidade de unidades disponiveis do jogo = "))
                 )
        

                print("")

                lista_de_jogos.append(jogo)

                print("Jogo cadastrado!")
                print("")

                opcao = input("Deseja cadastrar mais jogos (S|N) = ").strip().lower()

                print("")

                if opcao == "n":
                    break
        
        case 2:
            print("")
            print("Removendo - unidade")
            print("")

            while True:

                nome_jogo = input("Digite o nome do jogo para remover do estoque = ").strip().lower()
                quantidade = int(input("Digite á quantidade que deseja remover = "))

                if quantidade < 0:
                    print("")
                    print("Quantidade invalida - tente novamente")
                    continue


                remover_unidade_jogo(lista_de_jogos,nome_jogo,quantidade)

                print("")

                opcao = input("Deseja remover unidade de outro jogo (S|N) = ").strip().lower()

                if opcao == "n":
                    break
        
        case 3:
            print("")
            print("Listando - jogo")
            print("")

            while True:
                print("")


                nome_do_jogo = input("Digite o nome do jogo = ").strip().lower()

                exibir_dados(lista_de_jogos,nome_do_jogo)

                print("")

                opcao = input("Deseja lista outro jogo (S|N) = ").strip().lower()

                if opcao == "n":
                    break

        
        case 4:
            print("")
            print("Adicinando unidade jogo")
            print("")

            while True:
                print("")

                nome_do_jogo = input("Digite o jogo á ser adiciondo no estoque = ").strip().lower()
                unidade = int(input("Digite á quantidade á ser adicionado ao estoque = "))

                if unidade < 0:
                    print("")
                    print("Valor invalido - tente novamente")
                    continue


                print("")

                adicinando_unidade(lista_de_jogos,nome_do_jogo,unidade)

                print("")

                opaco = input("Deseja adicinar mais unidades de jogos no estoque (S|N) = ").strip().lower()

                if opaco == "n":
                    break
        
        case 5:
            print("")
            print("Salvando arquivo!")

            with open("Jogos.txt","a",encoding="utf-8") as arquivo_jogos:
                for jogo in lista_de_jogos:
                    arquivo_jogos.write(f"Nome: {jogo.nome}, valor: {jogo.valor:.2f}, quantidade = {jogo.quantidade}\n")
            
        case 6:
            print("")

            # with open("jogos.txt","r",encoding="utf-8") as arquivo_jogos:
            #     for linha in lista_de_jogos:
            #         nome,valor,quantidade = linha.split(",")
            #         lista_de_jogo_organizado.append(Jogo(
            #             nome=nome,
            #             valor=valor,
            #             quantidade=quantidade
            #         ))
            print("Encerrando - programa")


        case _:
            print("")
            print("Dado invalido - Tente - novamente")


        

