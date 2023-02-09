"""
Closure e funções que retornam outras funções

Closure: Consiste em retornar uma função que use internamente variáveis (ou nomes) da função que a define.

# Capacidade de perceber o seu "entorno"... Tem consciência do local onde ela foi escrita.
# Além do escopo interno, ela percebe o que está ao seu redor.
"""


def criar_saudacao(saudacao, nome):
    def saudar():
        return f'{saudacao}, {nome}!'
    return saudar()


s1 = criar_saudacao('Bom dia', 'Luiz')
s2 = criar_saudacao('Boa noite', 'Luiz')
print(s1)
print(s2)
