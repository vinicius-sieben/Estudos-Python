"""
Exercícios
Crie funções que duplicam, triplicam e quadruplicam o número recebido como parâmetro.
"""

# Capacidade de perceber o seu "entorno"... Tem consciência do local onde ela foi escrita.
# Além do escopo interno, ela percebe o que está ao seu redor.

# Closure: Consiste em retornar uma função que use internamente variáveis (ou nomes) da função que a define.


def calcular(x):
    def calculo(y):
        return x * y
    return calculo


dobro = calcular(2)
triplo = calcular(3)
quadruplo = calcular(4)

print(dobro(2))
print(triplo(2))
print(quadruplo(2))
