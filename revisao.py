import os

def exibir_nome_programa():
    print("""
    PROGRAMA PYTHON
          """)
    

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair')

def finalizar_app():
    os.system('cls')
    print('Finalizando app\n')

def voltar_menu_principal():
    print('Digite uma tecla para voltar ao menu principal\n')
    main()

def opcao_invalida():
    print('Opção inválida!')
    voltar_menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            print('1. Cadastrar restaurante')
        elif opcao_escolhida == 2:
            print('2. Listar restaurante')
        elif opcao_escolhida == 3:
            print('3. Ativar restaurante')
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()


def main():
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()