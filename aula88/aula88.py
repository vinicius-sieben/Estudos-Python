"""
Enumerate - enumera iteráveis (indíces)
"""
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

lista_enumerada = list(enumerate(lista))

for indice, nome in lista_enumerada:
    print(indice, nome)
