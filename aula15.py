cpf = '01988661609'
nove_digitos = cpf[:9]
contador_regressivo = 10
resultado = 0

for digito_1 in nove_digitos:
    resultado += int(digito_1)* contador_regressivo
    contador_regressivo -= 1

digito_1 = (10*resultado) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

dez_digitos = nove_digitos + str(digito_1)
contador_regressivo_2 = 11
resultado2 = 0

for digito_2 in dez_digitos:
    resultado2 += int(digito_2) * contador_regressivo_2
    contador_regressivo_2 -=1

digito_2 = (10*resultado2)%11
digito_2 = digito_2 if digito_2 <= 9 else 0

novo_cpf = f"{nove_digitos}{digito_1}{digito_2}"
print(novo_cpf if cpf == novo_cpf else "cpf falso")
