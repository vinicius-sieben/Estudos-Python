# Métodos úteis:
# add, update, clear, discard

# Operadores úteis:
# união | união (union) - Une
# interseccção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

s1 = {1, 2, 3}
s2 = {2, 3, 4}

s3 = s1 | s2
s3 = s1 & s2
s3 = s2 - s1
s3 = s2 ^ s2

print(s3) 