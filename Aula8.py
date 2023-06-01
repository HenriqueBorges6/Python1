time = input('Digite a hora em números inteiros: ')

try:
    hora = int(time)
    if 0 <= hora <=11 :
        print(f"Bom dia ! São {hora} da manhã ")
    elif 12 <= hora <=17 :
        print(f"Boa tarde ! São {hora} da tarde ")
    elif 18 <= hora <= 23 :
        print(f"Boa noite ! São {hora} da noite")
    else:
        print('Não conheço essa hora')
except:
    print('Digite apenas numeros inteiros')