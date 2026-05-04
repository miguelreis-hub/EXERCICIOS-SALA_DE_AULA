import os 
os.system("cls")

from dataclasses import dataclass


@dataclass

class Pet:
    nome:str
    idade:int
    raca:str

    def exibir_dados(self):

        print("")
        print("")
        print(f"Nome = {self.nome}")
        print(f"Idade = {self.idade}")
        print(f"Raça = {self.raca}")
        print("")

lista_de_pets = []

while True:
    print("")
    print("")

    animal = Pet(

        nome = input("Digite o nome do Pet = ").strip().lower(),
        idade = int(input("Digite a idade do Pet = ")),
        raca = input("Digite á raça do Pet = ")
    )

    lista_de_pets.append(animal)

    print("")

    opcao = input("Deseja cadastrar mais Pet? S|N = ").strip().lower()

    if opcao == "n":

        break

    if opcao == "s":

        for i in range(2):

            animal = Pet(

            nome = input("Digite o nome do Pet = ").strip().lower(),
            idade = int(input("Digite a idade do Pet = ")),
            raca = input("Digite á raça do Pet = ")

            )

            lista_de_pets.append(animal)

            print("")
            print("Cadastro Concluido!")

        break


with open("Dados_Pets.txt", "a") as arquivo_pets:

    for pet in lista_de_pets:

        arquivo_pets.write(f"{pet.nome},{pet.idade},{pet.raca}\n")



## Exibindo lista de pets cadastrados

for pet in lista_de_pets:

    pet.exibir_dados()


