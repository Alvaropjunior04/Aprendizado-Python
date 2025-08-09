real = float(input('Quanto dinheiro você tem na carteira? R$ '))
b = real / 5.43
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, b))