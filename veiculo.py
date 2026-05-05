import os
os.system("cls")
from dataclasses import dataclass

@dataclass

class Carro:
    veiculo:str
    placa:str
    cor:str

    def mostrar(self):
        print("")
        print("Exibindo - Dados")
        print("")
        print(f"veiculo = {self.veiculo}")
        print(f"placa = {self.placa}")
        print(f"cor = {self.cor}")
        print("")



lista_de_carros = []

while True:
    print("")

    veiculo = Carro(
        veiculo = input("Digite o veiculo = ").strip().lower(),
        placa = input("Digite á placa = ").strip().lower(),
        cor = input("Digite á cor do carro = ").strip().lower()
    )

    print("")

    lista_de_carros.append(veiculo)

    opcao = input("Deseja cadastrar mais veiculos (S|N) = ").strip().lower()

    if opcao == "n":
        break

salvar_arquivo = input("Deseja salvar os dados no arquivo = (S|N) = ").strip().lower()

if salvar_arquivo == "s":
    with open("Carros.txt","a") as arquivo_carro:
        for veiculo in lista_de_carros:
            arquivo_carro.write(f"Veiculo = {veiculo.veiculo} | Placa = {veiculo.placa} | Cor = {veiculo.cor}\n")


for veiculo in lista_de_carros:
    veiculo.mostrar()