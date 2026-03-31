import os 
os.system("cls")


valor_total_pagar = 0

preco_do_prato = []

prato_escolhido = []



while True:
    
    print("""
    === MENU ===
    1   Picanha          R$ 25,00
    2   Lasanha          R$ 20,00
    3   Strogonoff       R$ 18,00
    4   Bife acebolado   R$ 15,00
    5   Pão com ovo      R$ 15,00
        """)
    
    opcao = int(input("Digite o prato desejado = "))
    
    match opcao:
        
        case 1:
            
            prato_escolhido.append("Picanha")
            
            preco_do_prato.append(25)
            
            valor_total_pagar += 25
            
            parar = input("Deseja continuar = ").strip().lower()
            
            if parar == "n":
                break
        
        case 2:
            
            prato_escolhido.append("Lasanha")
            
            preco_do_prato.append(20)
            
            valor_total_pagar += 20
            
            parar = input("Deseja continuar = ").strip().lower()
            
            if parar == "n":
                break
        
        case 3:
            
            prato_escolhido.append("Strogonoff")
            
            preco_do_prato.append(18)  
                      
            valor_total_pagar += 18
            
            parar = input("Deseja continuar = ").strip().lower()
            
            if parar == "n":
                break
        
        case 4:
            
            prato_escolhido.append("Bife acebolado")
            
            preco_do_prato.append(15)
            
            valor_total_pagar += 15
            
            parar = input("Deseja continuar = ").strip().lower()
            
            if parar == "n":
                break
        
        case 5:
            
            prato_escolhido.append("Pão com ovo")
            
            preco_do_prato.append(15)
            
            valor_total_pagar += 15
            
            parar = input("Deseja continuar = ").strip().lower()
            
            if parar == "n":
                break
        
        case _:
            
            print("Dado invalido - Tente novamente")


print("")
print("")


for i in range(len(prato_escolhido)):
    
    print(f"{prato_escolhido[i]} - {preco_do_prato[i]}R$")
    
print("")
print("")

print(f"O valor total á pagar é = {valor_total_pagar}R$")
            
            