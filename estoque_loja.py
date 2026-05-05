import os
os.system("cls")
from dataclasses import dataclass

@dataclass

class Produto:
    nome:str
    preco:float
    quantidade:int

    def mostrar(self):
        print("")
        print("Mostrando - Dados")
        print("")
        print(f"Nome Produto = {self.nome}")
        print(f"Preco Produto = {self.preco}")
        print(f"Quantidade = {self.quantidade}")
        print("")



lista_de_produtos = []


while True:
    print("")

    produtos = Produto(

        nome = input("Digite o nome do produto = ").strip().lower(),

        preco = float(input("Digite o valor do produto = ")),

        quantidade = int(input("Digite á quantidade de produtos no estoque = "))
    )

    lista_de_produtos.append(produtos)

    opcao = input("Deseja cadastrar mais produtos (S|N) = ").strip().lower()

    if opcao == "n":
        break


salvar_arquivo = input("Deseja salvar em um arquivo (S|N) = ").strip().lower()

if salvar_arquivo == "s":

    with open("Produtos.txt","a") as arquivo_produtos:

        for produto in lista_de_produtos:

            arquivo_produtos.write(f"Nome Produto = {produto.nome} Preco Produto = {produto.preco}R$ Quantidade = {produto.quantidade}\n")


exbir = input("Deseja exibir os dados (S|N) = ").strip().lower()

if exbir == "s":

    for produto in lista_de_produtos:

        produto.mostrar()