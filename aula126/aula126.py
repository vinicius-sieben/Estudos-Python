# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas tipos imutáveis como valor interno.

# Criando um set
# set(iteravel) ou {1, 2, 3}
# s1 = set() # vazio
s1 = {'Luiz', 1, 2, 3}  # com dados
print(s1)

# Sets são eficientes para remover valores duplicados de iteráveis.
# - eles não tem índexes;
# - eles não garantem ordem;
# - eles são iteráveis (for, in, not in)

# Métodos úteis:
# add, update, clear, discard
