while True:
    number1 = input('Digite um numero: ')
    number2 = input('Digite um numero: ')
    operador = input('Digite um operador (+-/*): ')
    números_válidos = None
    nun1 = 0
    nun2 = 0
    try:
        nun1 = float(number1)
        nun2 = float(number2)
        números_válidos = True
    except:
        números_válidos = None
    if números_válidos is None:
        print('Algum dos números não são válidos')
        continue
    
    operadores_válidos = '+-/*'

    if operador not in operadores_válidos:
        print('Não temos esse operador')
        continue
    
    if len(operador) > 1:
        print('digite apenas um operador')
        continue
    
    print('Realizando sua conta')
    if operador == '+':
        print(nun1 + nun2)
    if operador == '-':
        print(nun1 - nun2)
    if operador == '/':
        print(nun1 / nun2)
    if operador == '*':
        print(nun1 * nun2)

    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break