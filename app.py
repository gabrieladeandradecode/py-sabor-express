# Python usa snake_case: variável, funções e métodos

import os

restaurantes = [{'nome': 'Pizza', 'categoria': 'Italiana', 'ativo': False},
                {'nome': 'Hamburguer', 'categoria': 'Americana', 'ativo': True},
                {'nome': 'Doces da Suíça', 'categoria': 'Suíça', 'ativo': True}
            ]

def exibir_nome_programa():
    '''
        Apresenta o nome do programa sendo a primeira função usada ao iniciar a aplicação .
    '''
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
          """)

def exibir_opcoes():
    '''
        Exibe menu de opções para usuário selecionar e executar as ações da aplicação.
    '''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar estado do restaurante')
    print('4. Sair')

def finalizar_app():
    '''
        Interface com mensagem que sinaliza o usuário o encerramento da aplicação.
    '''
    exibir_subtitulo('Finalizando aplicativo\n')

def voltar_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal ')
    main()

def opcao_invalida():
    '''
        Caso o usuário digite uma tecla diferente das apresentadas, essa função serve para avisá-lo que o dígito foi inválido e por isso a aplicação retornará ao menu principal.
    '''
    print('Opção inválida! ')
    voltar_menu_principal()

def exibir_subtitulo(texto):
    '''
        Argumento: str
        Retorna: str -> texto digitado como título 
        Função utilizada em outras funções para colocar título. 
    '''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)

def cadastrar_restaurante():
    '''Essa função é responsável por cadastrar novos restaurantes
    
    Inputs:
    - Nome do restaurante
    - Categoria do restaurante

    Output:
    - Novo restaurante adicionado à lista
    
    '''
    os.system('cls')
    exibir_subtitulo('Cadastro de novos restaurantes')
    
    novo_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')

    categoria = input(f'Digite a categoria do restaurante {novo_restaurante}: ')

    dados_do_restaurante = {'nome': novo_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)

    print(f'\nO restaraunte {novo_restaurante} foi cadastrado com sucesso!\n')
    voltar_menu_principal()

def listar_restaurantes():
    '''
        Essa função é responsável por retornar a lista de restaurantes cadastrados na aplicação.

        Output: list
        - Nome
        - Categoria
        - Status
    '''
    exibir_subtitulo('Listando restaurantes...\n')
    print(f'{'Nome do restaurante'.ljust(23)} | {'Categoria'.ljust(20)} | {'Status'}')

    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativo_restaurante = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f' - {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {ativo_restaurante}')
    voltar_menu_principal()    
    
def alternar_estado_restaurante():
    '''
        Essa função oferece input para usuário ativar ou desativar um restaurante, alterando seu estado ao digitar o nome do restaurante.

        Input: nome do restaurante

        Output: alternância de estado para ativado ou desativado.
    '''
    exibir_subtitulo('Alternando estados dos restaurantes...\n')

    restaurante_encontrado = False
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso.' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso.'
            print(mensagem)
    if not restaurante_encontrado:
        print(f'O restaurante {nome_restaurante} não foi encontrado.')
    
    voltar_menu_principal()

def escolher_opcao():
    '''
        Função com input para usuário escolher uma opção do menu.
        Input: int -> 1 ao 4

        Output: function 
    '''
    try: 
        opcao_escolhida = int(input('Escolha uma opção: '))
        
        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida() 
    except:
        opcao_invalida()


def main():
    '''
        Função principal e importante responsável por criar o fluxo da aplicação. 
        Ela abrange outras três funções:
        Apresentação do nome;
        Menu de opções;
        Input para escolha de opção, a qual inclui também a opção de finalizar a aplicação.
    '''
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
