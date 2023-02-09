"""
Iterável -> str, range, etc (___iter___)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador

"""
#  for letra in texto:
texto = 'Luiz'
iterador = iter(texto)

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break

# Isso acima é basicamente o que o FOR faz por baixo dos panos.
for letra in texto:
    print(letra)
