pessoa = {'nome': 'Gabi', 'idade': 20, 'cidade': 'RJ'}

print('INFORMACOES da pessoa')
print(pessoa)

pessoa['idade']= 21

# usando lista é append:
# pessoa.append({'profissao': 'Cientista da Computacao'})
pessoa['profissao'] = 'Cientista da Computacao'

pessoa.pop('cidade')
# del pessoa['cidade']

print('\nIdade, Profissao e sem cidade')
print(pessoa)

lista_de_mercado = {'comida': 'carne', 'bebida': 'suco', 'sobremesa': 'bolinho'}
if 'bebida' in lista_de_mercado:
    print('\nA bebida existe na lista.')
else:
    print('\nA bebida nao existe na lista.')

if 'fruta' in lista_de_mercado:
    print('\nA fruta existe na lista.')
else:
    print('\nA fruta nao existe na lista.')

print()
frase = 'estudo de Python requer muito estudo'
palavras = frase.split()
print(palavras)
frequencias_de_palavras = {}
for palavra in palavras:
    frequencias_de_palavras[palavra] = frequencias_de_palavras.get(palavra, 0) + 1
print(frequencias_de_palavras)
