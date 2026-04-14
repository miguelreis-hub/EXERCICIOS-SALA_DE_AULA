import os 

os.system("cls")

def calcular_IMC(peso,altura):
    
    imc = peso / (altura * altura)
    
    return imc



def situacao_do_peso_usuario(peso_imc):
    
    if peso_imc < 18.5:
        print(f"Abaixo do peso")
        print(f"")
        print(f"Recomendação")
        print(f"")
        print(f"Consulte um nutricionista")
    
    if peso_imc >=18.5 and peso_imc <=24.9:
        
        print(f"Peso normal")
        print(f"")
        print(f"Matenha hábitos saudaveis")
    
    if peso_imc >= 25 and peso_imc <= 29.9:
        
        print(f"Sobre - peso")
        print(f"")
        print(f"Considere uma dieta balançada")
    
    if peso_imc >=30 and peso_imc <=34.9:
        
        print(f"Obesidade grau 1")
        print(f"")
        print(f"Procure orientação médica")
    
    if peso_imc >= 35 and peso_imc <= 39.9:
        
        print(f"Obesidade grau 2")
        print("")
        print("Consulte um médico para avaliação e orientação")
    
    if peso_imc >= 40:
        
        print(f"Obesidade grau 3")
        print("")
        print(f"Busque assistencia médica imediatamente")






peso_do_usuario = float(input("Digite seu peso = "))

altura_do_usuario = float(input("Digite sua altura = "))
print("")
print("")

imc_do_usuario = calcular_IMC(peso_do_usuario,altura_do_usuario)

situacao_do_peso_usuario(imc_do_usuario)