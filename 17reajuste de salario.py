salario = float(input('Qual é o salario desse funcionário? R$'))
novo = salario + (salario * 15 / 100)
print('O seu salario era de R${} e agora com aumento de 15% foi para R${}'.format(salario, novo))