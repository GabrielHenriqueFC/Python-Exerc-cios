valor = float(input('Digite quantas maçãs foram compradas: '))

if valor >= 12:
    print('O valor de',valor,'maçãs custam R$',valor)
else:
    preco = valor * 1.30
    print('O valor de',valor,'maçãs custam R$',preco)