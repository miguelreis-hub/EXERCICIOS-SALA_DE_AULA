import os
os.system("cls")
from dataclasses import dataclass

@dataclass

class Conta:
    titular:str
    conta:str
    saldo:float

    def mostrar(self):
        print("")
        print("Mostrando Dados")
        print("")
        print(f"Titular = {self.titular} ")
        print(f"Conta = {self.conta}")
        print(f"Saldo = {self.saldo:.2f}R$")
        print("")


lista_de_contas_clientes = []


while True:
    print("")

    cliente = Conta(
        titular = input("Digite o nome do titular = ").strip().lower(),
        conta = input("Digite a conta do cliente = ").strip().lower(),
        saldo = float(input("Digite o saldo do cliente = "))
    )
    print("")

    lista_de_contas_clientes.append(cliente)

    opaco = input("Deseja cadastrar mais contas (S|N) = ").strip().lower()

    if opaco == "n":
        break

salvando_arquivo = input("Deseja salvar esses dados em arquivos (S|N) = ").strip().lower()


if salvando_arquivo == "s":

    with open("Contas.txt","a") as arquivo_contas:
        for conta in lista_de_contas_clientes:
            arquivo_contas.write(f"Titular = {conta.titular} | Conta = {conta.conta} | Saldo = {conta.saldo:.2f}R$\n")


for conta in lista_de_contas_clientes:

    conta.mostrar()