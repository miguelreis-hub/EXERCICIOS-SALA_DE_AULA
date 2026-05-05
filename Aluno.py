import os
os.system("cls")
from dataclasses import dataclass

@dataclass

class Aluno:
    nome:str
    matricula:str
    curso:str

    def mostrar(self):

        print("")
        print("Mostrando - Dados")
        print("")
        print(f"Nome Aluno = {self.nome}")
        print(f"Matricula = {self.matricula}")
        print(f"Curso = {self.curso}")
        print("")



lista_de_alunos = []


while True:
    print("")

    aluno = Aluno(
        nome = input("Digite o nome do aluno = ").strip().lower(),
        matricula = int(input("Digite á sua matricula = ")),
        curso = input("Digite seu curso = ").strip().lower()
    )

    print("")
    lista_de_alunos.append(aluno)

    opcao = input("Deseja cadastrar mais aluno (S|N) = ").strip().lower()

    if opcao == "n":
        break


salvar_arquivo = input("Deseja salvar esses dados em um arquivo (S|N) = ").strip().lower()

if salvar_arquivo == "s":

    with open("Alunos.txt", "a") as arquivos_alunos:

        for aluno in lista_de_alunos:

            arquivos_alunos.write(f"Nome Aluno = {aluno.nome} | Matricula = {aluno.matricula} | Curso = {aluno.curso}\n")


exibir = input("Deseja mostrar os dados da lista (S|N) = ").strip().lower()


if exibir == "s":

    for aluno in lista_de_alunos:

        aluno.mostrar()