import os
from dataclasses import dataclass
os.system("cls")
@dataclass

class Paciente:
    nome:str
    idade:int
    peso:float
    altura:float

    def exibir_dados(self):

        print("")
        print("===== Solicitando Dados =====")
        print("")
        print(f"Nome:{self.nome}")
        print(f"Idade:{self.idade}")
        print(f"Peso:{self.peso}")
        print(f"Altura:{self.altura:.2f}")
        print("")
        print("===== Encerrando Programa =====")


paciente = Paciente(
    nome=input("Digite seu nome = ").strip().lower(),
    idade=int(input("Digite sua idade = ")),
    peso=float(input("Digite seu peso = ")),
    altura=float(input("Digite sua altura = ")),
)

paciente.exibir_dados()