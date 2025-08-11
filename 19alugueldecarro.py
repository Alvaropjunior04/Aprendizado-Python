Km = float(input('Quantos Km pecorridos?'))
dias = float(input('Quantos dias alugado?'))
carro = dias * 60
preço = Km * 0.15
final = carro + preço
print('O valor total a se pagar do carro é ? R${}'.format(final))
