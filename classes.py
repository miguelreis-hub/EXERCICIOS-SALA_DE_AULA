import os
from dataclasses import dataclass
os.system("cls")

@dataclass

class Pessoa:
    nome:str
    idade:int

@dataclass
class Pet:
    nome:str
    idade:int

#Usando classe
Pessoa1 = Pessoa("Miguel",19)
Pessoa2 = Pessoa("Junior",19)

pet1 = Pet("Toto",15)
pet2 = Pet("Negão",15)

print(f"Nome:{Pessoa1.nome}\nidade{Pessoa1.idade}")
print(f"Nome:{Pessoa2.nome}\nidade:{Pessoa2.idade}")

print(f"Nome_pet:{pet1.nome} idade_pet:{pet1.idade}")
print(f"Nome_pet2:{pet2.nome} idade_pet2:{pet2.idade}")







