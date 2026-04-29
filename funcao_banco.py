import os
os.system("cls")




def exibir_menu_banco(): ## função para exibir o menu

    print("""

===== BANCO DO BRASIL =====
  
      1 = Cadastro do usuario 
      2 = Depositar
      3 = Sacar
      4 = Exibir Saldo
      5 = Transferencia
      6 = Sair
                         
          """)


def encontrando_indice(usuario,cadastro_usuario): ## função para encontrar o indice, fica melhor para entender quem ta fazendo login e o que quer , porque os vetorees usuario e senha e saldo estao paralelo entre si entao usuario 1 sua senha vai ser no indice 1 e saldo tbm

    indice = cadastro_usuario.index(usuario)

    return indice

   

cadastro_usuario = [] ## Vetor para armazenar nome dos usuarios que da acesso a conta
senha_do_usuario = [] ## Vetor para armazenar senha do usuario
saldo_do_usuario = [] ## Vetor para armazenar saldo da conta de cada usuario


while True:

    exibir_menu_banco()

    opcao = int(input("Digite a opção desejada = "))

    match opcao:

        case 1:
            print("")
            print("===== CADASTRO DO USUARIO =====")
            print("")

            nome_do_usuario = input("Digite seu nome = ").strip().lower()
            print("")
            usuario_senha = input("Crie sua senha | max 3 caractere = ")

            if len(usuario_senha) > 3:

                print("")

                print("Senha invalida - no maximo 3 caractere")

                continue

            else:
                cadastro_usuario.append(nome_do_usuario)

                senha_do_usuario.append(usuario_senha)

                saldo_do_usuario.append(0)

                print("")
                print("Cadastro realizado com sucesso!")
        
        case 2:
            print("")
            print("===== DEPOSITO =====")
            print("")

            usuario = input("Digite seu usuario = ")

            if usuario in cadastro_usuario:
                print("")

                print("Usuario correto")

                print("")

                indice = encontrando_indice(usuario,cadastro_usuario)

                senha = input("Digite sua senha = ")

                if senha == senha_do_usuario[indice]:

                    print("")
                    print(f"Acesso permitido {cadastro_usuario[indice]}! ")
                    print("")

                    saldo_do_usuario[indice] = float(input("Digite o valor para o deposito = "))

                    print("")

                    print("Deposito realizado com sucesso!")
                
                else:

                    print("")

                    print("Usuario correto, porem senha incorreta tente novamente!")

                    continue
        
        case 3:
            print("")
            print("===== Sacar =====")
            print("")

            usuario = input("Digite seu usuario = ")

            if usuario in cadastro_usuario:
                print("")

                print("Valido!")

                print("")

                indice = encontrando_indice(usuario,cadastro_usuario)

                senha = input("Digite sua senha = ")

                if senha == senha_do_usuario[indice]:

                    print("")
                    print(f"Acesso permitido - Bem vindo {cadastro_usuario[indice]} ")
                    print("")

                    valor_do_saque = float(input("Digite o valor do saque = "))

                    if valor_do_saque > saldo_do_usuario[indice]:

                        print("")
                        print("Saque invalido! - Valor maior que o saldo da conta - Tente novamente!")
                        print("")

                        continue
                    
                    else:


                        saldo_do_usuario[indice] -= valor_do_saque
                        print("")
                        print(f"Saque Realizado com sucesso {cadastro_usuario[indice]}! ")

                    
                
                else:

                    print("")

                    print("Usuario correto, porem senha incorreta tente novamente!")

                    continue
        
        case 4:
            print("")
            print("===== SALDO ====")
            print("")

            usuario = input("Digite seu usuario = ")

            if usuario in cadastro_usuario:
                print("")

                print("Valido!")

                print("")

                indice = encontrando_indice(usuario,cadastro_usuario)

                senha = input("Digite sua senha = ")

                if senha == senha_do_usuario[indice]:

                    print("")
                    print(f"Acesso permitido - {cadastro_usuario[indice]} seus saldo atual é = {saldo_do_usuario[indice]:.2f}R$")
                    print("")
                
                else:

                    print("")

                    print("Senha invalida - tente novamente!")

                    continue
            
            else:

                print("")
                print("Usuario invalido! - tente novamente")

                continue
    
        case 5:

            print("")
            print("===== TRANSFERENCIA =====")
            print("")

            usuario = input("Digite seu usuario = ")

            if usuario in cadastro_usuario:
                print("")

                print("Valido!")

                print("")

                indice = encontrando_indice(usuario,cadastro_usuario)

                senha = input("Digite sua senha = ")

                if senha == senha_do_usuario[indice]:

                
                    print("")
                    print(f"Acesso permitido - {cadastro_usuario[indice]}")

                    nome_transferencia = input("Digite o nome para realizar transferencia = ").strip().lower()

                    if nome_transferencia in cadastro_usuario:

                        print("Usuario encontrado!")

                        indice_usuario_transferencia = encontrando_indice(nome_transferencia,cadastro_usuario)
                        print("")

                        opcao = input(f"Deseja fazer transferencia para {cadastro_usuario[indice_usuario_transferencia]} S|N ").strip().lower()

                        if opcao == "s":

                            valo_da_transferencia = float(input(f"Digite o valor da transferencia {cadastro_usuario[indice]} =  "))
                            
                            if valo_da_transferencia > saldo_do_usuario[indice]:

                                print("")
                                print("Transferencia invalida")
                                continue

                            else:

                                saldo_do_usuario[indice] -= valo_da_transferencia
                                saldo_do_usuario[indice_usuario_transferencia] += valo_da_transferencia

                                print("")
                                print("Transferencia realizada com sucesso!")
                        
                        else:

                            continue
                    
                    else:

                        print("")
                        print("Usuario não encontrado !")
                        continue
                
                else:
                    print("")
                    print("Senha invalida!")
                    continue
            
            else:

                print("")
                print("Usuario não encontrado!")
                continue

        case 6:

            break







            
          


        







            
        
        



