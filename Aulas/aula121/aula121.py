# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    # 'idade': 900,
}
pessoa.setdefault('idade', 0)
print(pessoa['idade'])
print(len(pessoa))  # Retorna quantas chaves existem no dicionário
print(list(pessoa.keys()))  # Retorna uma lista com as chaves do dicionário
print(list(pessoa.values()))  # Retorna uma lista com os valores do dicionário
print(list(pessoa.items()))  # Retorna uma lista com as chaves e valores do dicionário

for chave in pessoa:  # Quando eu chamo um iterador ele retorna chaves
    print(chave)

for valores in pessoa.values():
    print(valores)

for chave, valor in pessoa.items():
    print(chave, valor)
