import os

# Função sem retorno.
def logoSenai():
    os.system("cls || clear")
    print("=== SENAI === ")


def calculando_imc(peso,altura):

    imc = peso / (altura * altura)

    return imc


def situacao(imc_do_usuario):

    if imc_do_usuario < 18.5:

       return "Abaixo do peso"
       
    
    if imc_do_usuario >=18.5 and imc_do_usuario <=24.9:
        
        return "Peso normal"
    
    if imc_do_usuario >= 25 and imc_do_usuario <= 29.9:
        
        return "Sobrepeso"
    
    if imc_do_usuario >=30 and imc_do_usuario <=34.9:
        
        return "Obesidade grau 1"
    
    if imc_do_usuario >= 35 and imc_do_usuario <= 39.9:
        
        return "Obesidade grau 2"
    
    if imc_do_usuario >= 40:
        
        return "Obesidade grau 3"
    


nomes = []
idades = []
alturas = []
pesos = []
vetor_imc_do_usuario = []

# Solicitando os dados dos usuários em um loop
while True:
    logoSenai()
    nome = input("Digite o nome do usuário (ou digite 'sair' para encerrar): ")
    
    # Verificando se o usuário quer sair
    if nome.lower() == 'sair':
        break
    
    idade = int(input("Digite a idade do usuário: "))
    altura = float(input("Digite a altura do usuário (em metros): "))
    peso = float(input("Digite o peso do usuário (em quilogramas): "))
    
    # Adicionando os dados às listas
    nomes.append(nome)
    idades.append(idade)
    alturas.append(altura)
    pesos.append(peso)

    imc = calculando_imc(peso,altura)

    vetor_imc_do_usuario.append(imc)

# Exibindo os dados armazenados
logoSenai()
print("\nDados dos usuários:")
for i in range(len(nomes)):
    print(f"Usuário {i+1}:")
    print("Nome:", nomes[i])
    print("Idade:", idades[i])
    print("Altura:", alturas[i], "metros")
    print("Peso:", pesos[i], "quilogramas")
    print(f"Imc = {vetor_imc_do_usuario[i]:.0f} - Situação = {situacao(vetor_imc_do_usuario[i])}")