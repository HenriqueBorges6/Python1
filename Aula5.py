number = input("digite um número inteiro: ")
if number .isdigit():
    if int(number)% 2 > 0:
        print("O número é ímpar")
    else:
        print("o número é par")
else:
    print("Esse número não é inteiro")