import os 
from dataclasses import dataclass
os.system("cls")


@dataclass

class Endereco: ## classe para armazenar informações endereço

    logadouro:str ## equivalente á rua
    numero:str


@dataclass

class Cliente: ## classe para obter informações do cliente
    nome:str
    idade:str
    endereco:Endereco # Realcionamento com a classe Endereço

    def mostrar_dados(self): ##função para exibir dados (self serve para quando não souber que variavel vai ficar la como 0 ai quando a função for chamado numa variavel automaticamente esa variavel vai entrar no lugar do self
        
        print("")
        print("===== Solicitando Dados =====")
        print("")
        print(f"Nome:{self.nome}")
        print(f"Idade:{self.idade}")
        print(f"Endereco:{self.endereco.logadouro}")
        print(f"Numero:{self.endereco.numero}")
        print("")
        print("===== Encerrando Programa =====")



cliente = Cliente(

    nome=input("Digite seu nome = ").strip(),
    idade=input("Digite sua idade = ").strip(),
    endereco=Endereco(
        logadouro=input("Digite seu endereco = ").strip(),
        numero=input("Digite o numero = ").strip()
    )
)

cliente.mostrar_dados()