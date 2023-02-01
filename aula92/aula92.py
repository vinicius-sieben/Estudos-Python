"""
split e join com list e str
split - divide uma string
join - une uma string
"""
frase = 'Olha só que coisa interessante'
lista_frases_cruas = frase.split(',')

lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())

print(lista_frases)

# .strip() -> tira os espaços do começo e fim da string
# .rstrip() -> tira os espaços da direita
# .lstrip() -> tira os espaços da esquerda

