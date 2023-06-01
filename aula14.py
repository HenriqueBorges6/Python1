import os

lista = []

while True:
    print("Selecione uma opção")
    escolha = input("[i]inserir ; [a]apagar ; [l]istar ")
    if escolha == "i":
        os.system("cls")
        item = input("Digite o que deseja inserir: ")
        lista.append(item)

    elif escolha == "a":
        os.system("cls")
        apagar = input("Qual item deseja apagar? ")
        try:
            item_pra_apagar = int(apagar)
            del lista[item_pra_apagar]
        except IndexError :
            print("Não foi possível apagar esse indice")
        except ValueError :
            print("Digite um número inteiro")
    elif escolha == "l":
        os.system("cls")
        if len(lista) == 0:
            print("não tem nada para listar")
        for indice, escolha in enumerate(lista):
            print(indice, escolha)

    else:
        print("Escreva apensa a letra em colchetes")