nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2

if media >= 6:
    print('O aluno teve média',media,' => APROVADO')
else:
    print('O aluno teve média',media,' => REPROVADO')