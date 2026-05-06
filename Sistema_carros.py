import os
from dataclasses import dataclass

@dataclass
class Carro:
    nome_do_dono: str
    carro: str
    fabricante: str
    preco: float

    def mostrar_dados(self):
        print(f'Nome: {self.nome_do_dono}')
        print(f'carro: {self.carro}')
        print(f'fabricante: {self.fabricante}')
        print(f'Preço: {self.preco}')


NOME_DO_ARQUIVO = 'catalogo_carros.csv'

# Função para salvar em arquivo.
def salvar_no_arquivo(carro: Carro):
    with open(NOME_DO_ARQUIVO, 'a', encoding='utf-8') as arquivo:
        arquivo.write(f'{carro.nome_do_dono},{carro.carro},{carro.fabricante},{carro.preco}\n')
    print('Carro salvo com sucesso!')

# Função para ler dados em arquivo.
def ler_arquivo():
    # Tratamento de exceção.
    try:
        print('\n- LISTA DE CARROS -')
        lista_carro = []
        with open(NOME_DO_ARQUIVO, 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                nome_do_dono, carro, fabricante, preco = linha.strip().split(',')
                lista_carro.append(Carro(nome_do_dono, carro, fabricante, preco))

        for carro in lista_carro:
            carro.mostrar_dados()
            print('-'*20)
    except FileNotFoundError:
        print('Arquivo não encontrado...')


while True:
    os.system('cls')
    print('''--- SISTEMA DE CADASTRO ---
    1 - Adicionar carro
    2 - Listar carro
    3 - Sair
          ''')
    opcao = int(input('Digite a opção desejada: '))

    match opcao:
        case 1:
            os.system('cls')
            print('- Cadastrar carro -')
            novo_carro = Carro(
                nome_do_dono= input('Nome: '),
                carro=input('carro:  '),
                fabricante=input('marca: '),
                preco=float(input('Preço: '))
            )
            salvar_no_arquivo(novo_carro)
        case 2:
            os.system('cls')
            ler_arquivo()
            input('Pressione Enter para voltar ao menu...')
            os.system('cls')
        case 3:
            print('Saindo do programa...')
            break
        case _:
            print('\nOpção inválida. Tente novamente.\n')