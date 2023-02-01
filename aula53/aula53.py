"""
Faça um programa que peça ao usuário para digitar um número inteiro, informe se este número é par ou ímpar.
Caso o usuário não digite um número inteiro, informe que não é um número inteiro.

Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a saudação apropriada.
Ex. Bom dia 0-11, Boa tarde 12-17, Boa noite 18-23.

Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos escreva "Seu nome é curto"; se
tiver entre 5 e 6 letras, escreva "Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""

print("Exercício 1.")
print("")
num = input("Digite um número inteiro: ")

if num.isdigit():
    num = int(num)
    if num % 2 == 0:
        print(f"O número {num} é par.")
    else:
        print(f"O número {num} é ímpar.")
else:
    print("O valor inserido não é um número inteiro.")

print("")
print("Exercício 2.")
print("")

horario = input("Insira o horário: ")

if horario.isdigit():
    horario = int(horario)
    if horario >= 0 and horario <= 11:
        print("Bom dia!")
    if horario >= 12 and horario <= 17:
        print("Boa tarde!")
    if horario >= 18 and horario <= 23:
        print("Boa noite!")
else:
    print("Valor inserido inválido.")

print("")
print("Exercício 3.")
print("")

nome = input("Insira seu primeiro nome: ")
if len(nome) <= 4:
    print("Seu nome é curto.")
if len(nome) == 5 or len(nome) == 6:
    print("Seu nome é normal.")
if len(nome) > 6:
    print("Seu nome é muito grande.")
