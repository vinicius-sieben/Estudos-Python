# Manipulando chaves e valores em dicionários
# CRUD = Create, Read, Update, Delete

pessoa = {}

chave = 'nome'

pessoa[chave] = 'Luiz Otávio'
pessoa['sobrenome'] = 'Miranda'

print(pessoa[chave])

pessoa[chave] = 'Maria'

# del pessoa['sobrenome']

print(pessoa)
print(pessoa['nome'])

print(pessoa.get('sobrenome', None))

if pessoa.get('sobrenome') is None:
    print('Não existe')
else:
    print(pessoa['sobrenome'])

# print('Isso não vai')
