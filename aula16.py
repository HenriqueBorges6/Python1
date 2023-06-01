#Função de produto de números
def produtorio(*args):
    vezes = 1
    for numero in args:
        vezes *= numero
    return vezes

multiplicação = produtorio(1,2,3,4,5,6)
print(multiplicação)

#Função que responde a paridade de um número
def paridade(numero):
    if numero % 2 == 0:
        return f"{numero} é par"
    return f"{numero} é impar"

number = paridade(122)
print(number)