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
import copy
d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2],
}

# d2 = d1  # Compartilham o mesmo dicionário
d2 = d1.copy()  # Cria uma cópia rasa (shallow copy) (não copia valores mutáveis, apenas "linka" eles)

d2['c1'] = 1000

# Alterando no dicionário 2 mas também altera no dicionário 1 pois estão linkadas devido a serem listas.
d2['l1'][1] = 9999

print(d1) 
print(d2)

d2 = copy.deepcopy(d1)  # Cria uma cópia profunda (deep copy)

d2['c1'] = 1000

# Alterando no dicionário 2 mas também altera no dicionário 1 pois estão linkadas devido a serem listas.
d2['l1'][1] = 9999

print(d1)
print(d2)
