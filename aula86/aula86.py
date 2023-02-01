"""
Introdução ao desempacotamento
"""
# Para empacotarmos usa-se * (asterisco) + var
# Por convenção, variáveis com o nome "_" significam que existem porém não serão usadas.


nome1, *_ = ['Maria', 'Helena', 'Luiz']
print(nome1, _)
