numero_conta = int(input('Digite o número da sua conta: '))
saldo = float(input('Digite o saldo da sua conta: '))
debito = float(input('Digite o debito da sua conta: '))
credito = float(input('Digite o credito da sua conta: '))
saldo_atual = saldo - debito + credito

if saldo_atual >= 0:
    print('Saldo positivo: R$', saldo_atual)
else :
    print('Saldo negativo: R$', saldo_atual)