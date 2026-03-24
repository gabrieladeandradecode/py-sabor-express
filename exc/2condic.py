num = int(input('Digite um número: '))

if num % 2 == 0:
    print(f'O número {num} é par')
else: 
    print(f'O número {num} é ímpar')

idade = int(input('Digite sua idade: '))

if 0 < idade <= 12:
    print('Criança')
elif idade <=18:
    print('Adolescente')
else:
    print('Adulto')


nome = input('Digite seu nome de usuário: ')
senha = input('Digite sua senha: ')

if nome == 'gabi' and senha == '123':
    print('Bem vindo(a)!')
else:
    print('Login inválido.')


coord_x = int(input('Digite o valor da coordenada x: '))
coord_y = int(input('Digite o valor da coordenada y: '))

if coord_x > 0 and coord_y > 0:
    print('1° Quadrante')
elif coord_x < 0 and coord_y > 0:
    print('2° Quadrante')
elif coord_x < 0 and coord_y < 0:
    print('3° Quadrante')
elif coord_x > 0 and coord_y < 0:
    print('4° Quadrante')
else:
    print('Ponto está no eixo / origem.')
