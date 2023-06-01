nome = input('digite seu nome: ')
if 0 > len(nome) <= 1:
    print('Digite um nome maior')
elif 1 < len(nome) <= 4:
    print('seu nome é curto')
elif 5>=len(nome)>4 :
    print('Seu nome é normal')
elif len(nome)>5:
    print('Seu nome é grande')
else :
    print("Digite algo")