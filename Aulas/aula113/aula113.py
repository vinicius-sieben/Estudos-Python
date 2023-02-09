# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

# Crie uma função que fala se um número é par ou ímpar
# Retorne se o número é par ou ímpar


# Função que multiplica todos os argumentos não nomeados recebidos
def multiplicador(*args):
    total = 1
    for numero in args:
        total *= numero
    return total


resultado = multiplicador(1, 2, 4, 5)
print(resultado)


# Função que fala se um número é par ou ímpar
def parouimpar(inteiro):
    if inteiro % 2 == 0: 
        return f'O número {inteiro} é par.'
    return f'O número {inteiro} é ímpar.'


parouimpar(3)
parouimpar(21)
parouimpar(6456)
parouimpar(9293)
