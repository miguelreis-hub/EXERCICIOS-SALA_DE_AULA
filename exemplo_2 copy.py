import os 
from dataclasses import dataclass
os.system("cls")

@dataclass

class Fornecedor:
    nome:str
    email:str
    telefone:str

    def exibir_dados(self):

        print("")
        print("===== Solicitando Dados =====")
        print("")
        print(f"Nome:{self.nome}")
        print(f"Email:{self.email}")
        print(f"Telefone:{self.telefone}")
        print("")
        print("===== Encerrando Programa =====")
        


forcedor = Fornecedor(
    nome=input("Digite seu nome = ").strip().lower(),
    email=input("Digite seu email = ").strip(),
    telefone=input("Digite seu telefone = ").strip(),

)

forcedor.exibir_dados()