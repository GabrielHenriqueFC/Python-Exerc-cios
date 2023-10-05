atual = int(input('Digite a quantidade atual em estoque: '))
maxima = int(input('Digite a quantidade maxima: '))
minima = int(input('Digite a quantidade minima: '))
media = (maxima + minima) / 2

if atual >= media :
    print('Não efetuar compra')
else:
    print('Efetuar compra')