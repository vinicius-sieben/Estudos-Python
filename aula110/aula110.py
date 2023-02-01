"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""
# Lemre-te de desempacotamento
x, y, *resto = 1, 2, 3, 4
print(x, y, resto)


# def soma(x, y):
#    return x + y

def soma(*args):
    for numero in args:
        print(numero)
 

soma(1, 2, 3, 4, 5, 6)
