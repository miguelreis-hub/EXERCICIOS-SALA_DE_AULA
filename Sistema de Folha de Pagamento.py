import os 
os.system("cls")

def exibir_intrucoes():
    
    print("""
1. Informe a matrícula e a senha do funcionário para acessar o sistema

2. Digite o valor do salário base do funcionário

3. O funcionário deseja receber vale-transporte? (S/N)

4. Informe o valor do vale-refeição fornecido pela empresa

5. Digite a quantidade de dependentes do funcionário

6. Calculando descontos e benefícios da folha de pagamento

7. Exibindo o salário líquido após descontos e acréscimos

""")

def calcular_vale_transporte(salario_base):

    salario_transporte = 0

    salario_transporte = salario_base * 0.06

    return  salario_transporte


def calcular_vale_reifeicao(vale_refeicao):

    vale_almoco = vale_refeicao * 0.2

    return vale_almoco


def calcular_INSS(salario_base):

    if salario_base <=1518:

        salario_base_desconto_final = (salario_base * 0.075)

    elif salario_base > 1518 and salario_base <= 2793.88:

        salario_base_desconto_final= (salario_base * 0.09)

    elif salario_base > 2793.89 and salario_base <= 4190.83:

        salario_base_desconto_final= (salario_base * 0.12)

    elif salario_base > 4190.84 and salario_base <= 8157.41:

        salario_base_desconto_final=(salario_base * 0.14)

    elif salario_base > 8157.41:

        salario_base_desconto_final=951.62

    return salario_base_desconto_final


def calcular_imposto(salario_base_imposto,inns):

    base_do_imposto= salario_base_imposto - inns

    base_do_imposto_final = 0

    if base_do_imposto <= 2428.80:

        base_do_imposto_final = 0

    elif base_do_imposto > 2428.81 and base_do_imposto <= 2826.65:

        base_do_imposto_final = base_do_imposto - (base_do_imposto * 0.075)

    elif base_do_imposto > 2826.66 and base_do_imposto <= 3751.05:

        base_do_imposto_final = base_do_imposto - (base_do_imposto * 0.15)

    elif base_do_imposto > 3751.06 and base_do_imposto <= 4664.68:

        base_do_imposto_final= base_do_imposto - (base_do_imposto * 0.225)

    elif base_do_imposto > 4664.68:

        base_do_imposto_final = base_do_imposto - (base_do_imposto * 0.275)

    return base_do_imposto_final




matricula_dos_funcionarios = 0

senhas_dos_funcionarios = 0

salario_base_dos_funcionarios = 0

vale_transporte = 0

vale_reifeicao = 0

dependentes_final = 0

salario_final_bruto = 0

inns = 0

imposto_de_renda = 0

while True:

    

    exibir_intrucoes()

    opcao = int(input("Digite a opção desejada = "))

    match opcao:

        case 1:

            print("\n=== ACESSO AO SISTEMA ===")

            matriculas = int(input("Digite sua matricula = "))
            senhas = int(input("Digite sua senha = "))

            

        
        case 2:

            print("\n=== SALÁRIO BASE ===")

            salario_base_dos_funcionarios = float(input("Digite seu salario base = "))
            


        
        case 3:
            print("\n=== VALE-TRANSPORTE ===")

            vale_transporte = input("Deseja receber o vale transporte? = S | N = ").strip().lower()

            if vale_transporte == "s":

                vale_transporte = calcular_vale_transporte(salario_base_dos_funcionarios)

        case 4:

            print("\n=== VALE-REFEIÇÃO ===")

            print("VALE - REFEIÇÂO - EMPRESA = 500R$")

            vale_reifeicao = calcular_vale_reifeicao(500)

        
        case 5:

            print("\n=== DEPENDENTES ===")

            dependentes = int(input("Digite a quantidade de dependentes = "))

            dependentes_final = dependentes * 150

            
        
        case 6:

            inns=calcular_INSS(salario_base_dos_funcionarios)

            imposto_de_renda=calcular_imposto(salario_base_dos_funcionarios,inns)

            vr_vt = vale_reifeicao + vale_transporte

            imposto_total = inns + imposto_de_renda + dependentes_final

            salario_final_bruto = salario_base_dos_funcionarios -  (vr_vt + imposto_total)

            print("\n=== CÁLCULO DA FOLHA ===")
            print("\n=== IMPOSTO DE RENDA ===")
            print(f" {imposto_de_renda}R$")
            print("\n======== INSS ==========")
            print(f" {inns}R$")
            print("\n=== VALE REFEIÇÃO ======")
            print(f"{vale_reifeicao}R$")
            print("\n=== VALE-TRANSPORTE ===")
            print(f"{vale_transporte}")

            # inns=calcular_INSS(salario_base_dos_funcionarios)

            # imposto_de_renda=calcular_imposto(salario_base_dos_funcionarios,inns)

            # vr_vt = vale_reifeicao + vale_transporte

            # imposto_total = inns + imposto_de_renda + dependentes_final

            # salario_final_bruto = salario_base_dos_funcionarios -  (vr_vt + imposto_total)

        
        case 7:

            print("\n=== RESULTADO FINAL ===")
            print("\n Exibindo salário líquido...")
            print(f"Sálario base = {salario_base_dos_funcionarios}R$ \nDependentes = {dependentes_final}R$ \nVale-transporte = {vale_transporte}R$ \nVale-Reifeição = {vale_reifeicao}R$ \nSalário Liquido = {salario_final_bruto}R$                      ")
        
        case _:

            print("\nOpção inválida! - Tente novamente")


                        

















