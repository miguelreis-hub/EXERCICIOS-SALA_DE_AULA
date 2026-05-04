import os
os.system("cls")

from dataclasses import dataclass

@dataclass

class Funcionario:
    nome:str
    email:str
    telefone:str

    def exibir_dados(self):

        print("")
        print("Exibindo - Dados")
        print("")
        print(f"Nome = {self.nome}")
        print(f"Email = {self.email}")
        print(f"Telefone = {self.telefone}")
        print("")
        print("Dados Encerrados")
        print("")


lista_de_funcionarios_novos = []

while True:

    print("")
    print("")

    novo_funcionario = Funcionario(
        nome = input("Digite seu nome = ").strip().lower(),
        email = input("Digite seu email = ").strip().lower(),
        telefone = input("Digite seu telefone = ").strip()
    )

    print("")

    lista_de_funcionarios_novos.append(novo_funcionario)

    opcao = input("Deseja cadastrar mais funcionarios? S|N = ").strip().lower()

    if opcao == "n":
        break


## Para cada funcionario na lista faça alguma coisa
for funcionario in lista_de_funcionarios_novos:

    funcionario.exibir_dados()