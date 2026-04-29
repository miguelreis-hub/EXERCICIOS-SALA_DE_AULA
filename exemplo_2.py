import os 
from dataclasses import dataclass
os.system("cls")

@dataclass

class Fornecedor:
    nome:str
    email:str
    telefone:str
    endereco:str


forcedor = Fornecedor(
    nome=input("Digite seu nome = ").strip().lower(),
    email=input("Digite seu email = ").strip(),
    telefone=input("Digite seu telefone = ").strip(),
    endereco=input("Digite seu endereço = ")
)

print("")
print("===== Solicitando Dados =====")
print("")
print(f"Nome:{forcedor.nome}")
print(f"Email:{forcedor.email}")
print(f"Telefone:{forcedor.telefone}")
print(f"Endereço:{forcedor.endereco}")
print("")
print("===== Encerrando Programa =====")