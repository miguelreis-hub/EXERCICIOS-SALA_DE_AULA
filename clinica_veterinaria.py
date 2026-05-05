import os
os.system("cls")

from dataclasses import dataclass

@dataclass

class Pet:
    nome:str
    idade:int
    raca:str

    def mostrar_dados(self):
        print("")
        print("Exibindo - Dados")
        print("")
        print(f"Nome = {self.nome}")
        print(f"Idade = {self.idade}")
        print(f"Raça = {self.raca}")
        print("")




lista_de_pets = []


while True:
    print("")

    animal = Pet(

        nome = input("Digite o nome do pet = ").strip().lower(),
        idade = int(input("Digite á idade do pet = ")),
        raca = input("Digite o nome da raça = ")

    )
    print("")

    lista_de_pets.append(animal)

    opcao = input("Deseja cadastrar mais pet (S|N) =  ").strip().lower()

    if opcao == "n":
        break

print("")

arquivo = input("Deseja salvar em um arquivo (S|N) = ").strip().lower()

if arquivo == "s":

    with open("Arquivo_pet.txt","a") as arquivo_pet:

        for pet in lista_de_pets:

            arquivo_pet.write(f"Nome Pet = {pet.nome}, Idade Pet = {pet.idade}, Raça Pet = {pet.raca}\n")


mostrar = input("Deseja exibir dados da lista (S|N) = ").strip().lower()

if mostrar == "s":

    for animal in lista_de_pets:

        animal.mostrar_dados()



