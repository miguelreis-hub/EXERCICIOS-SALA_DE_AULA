import os 
os.system("cls")

valor_total = 0

prato_escolhido = []
valor_do_prato_escolhido = []

while True:

    print("""
    === MENU ===
    1   Picanha          R$ 25,00
    2   Lasanha          R$ 20,00
    3   Strogonoff       R$ 18,00
    4   Bife acebolado   R$ 15,00
    5   Pão com ovo      R$ 15,00
        """)
    
    opcao = int(input("Escolha o prato desejado = "))

    match opcao:

        case 1:

            prato_escolhido.append("Picanha")
            valor_do_prato_escolhido.append(25.0)

            valor_total += 25

            continuar = input("Deseja continuar = ").strip().lower()

            if continuar == "n":
                break
        
        case 2:

            prato_escolhido.append("Lasanha")
            valor_do_prato_escolhido.append(20.0)

            valor_total += 20

            continuar = input("Deseja continuar = ").strip().lower()

            if continuar == "n":
                break
        
        case 3:

            prato_escolhido.append("Strogonoff")
            valor_do_prato_escolhido.append(18.0)

            valor_total += 18

            continuar = input("Deseja continuar = ").strip().lower()

            if continuar == "n":
                break
        
        case 4:

            prato_escolhido.append("Bife acebolado")
            valor_do_prato_escolhido.append(15.0)

            valor_total += 15

            continuar = input("Deseja continuar = ").strip().lower()

            if continuar == "n":
                break
        
        case 5:

            prato_escolhido.append("Pão com ovo ")
            valor_do_prato_escolhido.append(15.0)

            valor_total += 15

            continuar = input("Deseja continuar = ").strip().lower()

            if continuar == "n":
                break
        
        case _:

            print("Dado invalido tente novamente")
    


for i in range(len(prato_escolhido)):

    print(f"{prato_escolhido[i]} - {valor_do_prato_escolhido[i]}")



print("")
print("")

print(f"O valor total á pagar é = {valor_total}R$")


dinheiro_do_usuario = float(input("Insira o valor á pagar = "))

troco = valor_total - dinheiro_do_usuario

print(f"O troco é = {troco*-1}R$")

print("Até a proxima ")
