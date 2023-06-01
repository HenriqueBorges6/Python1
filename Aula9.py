nome = "Henrique Borges"
ind = 0
new = ''
while ind < len(nome):
    letra = nome[ind]
    new += f'*{letra}'
    ind += 1
new += '*'
print(new)


