# Fazer um algoritmo para ler um número inteiro entre 1 e 12 e mostrar o mês correspondente.
# Caso o valor digitado não estiver no intervalo solicitado, mostrar uma mensagem. 

numero = int(input('Digite um numero do mes: '))

if (numero > 12) and (numero < 1):
    if numero == 1: print('Janeiro')
    elif numero == 2: print('Fevereiro')
    elif numero == 3: print('Março')
    elif numero == 4: print('Abril')
    elif numero == 5: print('Maio')
    elif numero == 6: print('Junho')
    elif numero == 7: print('Julho')
    elif numero == 8: print('Agosto')
    elif numero == 9: print('Setembro')
    elif numero == 10: print('Outubro')
    elif numero == 11: print('Novembro')
    elif numero == 12: print('Dezembro')
else:
    print('Numero invalido')
    