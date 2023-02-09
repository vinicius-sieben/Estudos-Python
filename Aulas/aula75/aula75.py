"""
EXERCÍCIO - JOGO DA PALAVRA SECRETA

Faça um jogo para o usuário adivinhar qual a palavra secreta.

- Você vai propor uma palavra secrteta qualquer e vai dar a possibilidade para o usuário digitar apenas uma letra.
- Qual o usuário digitar uma letra, você vai conferir se a letra digitada está na palavra secreta.
- Se a letra digitada estiver na palavra secreta; exiba a letra;
- Se a letra digitada não estiver na palavra secreta; exiba *.

Faça a contagem de tentativas do seu usuário.
"""
palavra_secreta = 'perfume'
letras_acertadas = ''
numero_tentativas = 0


while True:
    letra_digitada = input('Informe uma letra: ')
    numero_tentativas += 1

    # Checking if the user typed more than once letter.
    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print(f'Palavra formada: {palavra_formada}')

    if palavra_formada == palavra_secreta:
        print('VOCÊ GANHOU! PARABÉNS!')
        print(f'Tentativas: {numero_tentativas}')
        print(f'A palavra era {palavra_secreta}')
        letras_acertadas = ''
        numero_tentativas = 0
        palavra_formada = ''
