import random

cpf_nove_digitos = [random.randint(0, 9) for _ in range(9)]  # Gera 9 números entre 0 e 10
# cpf_nove_digitos = [6,1,1,0,3,8,3,6,9]


# Primeiro Digito

valor_1 = 0
indice_reverso_1 = 10

for numero in cpf_nove_digitos:
        numero_int = int(numero)
        valor_1 += numero_int * indice_reverso_1
        indice_reverso_1 -= 1 

resultado_1 = (valor_1 * 10) % 11

if resultado_1 > 9:
    primeiro_digito = 0
else:
    primeiro_digito = resultado_1

# print(f'O seu primeiro dígito é: {primeiro_digito}')

#Segundo Dígito

cpf_nove_digitos.append(primeiro_digito)
cpf_dez_digitos = cpf_nove_digitos

valor_2 = 0
indice_reverso_2 = 11

for numero in cpf_dez_digitos:
        numero_int = int(numero)
        valor_2 += numero_int * indice_reverso_2
        indice_reverso_2 -= 1 

resultado_2 = (valor_2 * 10) % 11

if resultado_2 > 9:
    segundo_digito = 0
else:
    segundo_digito = resultado_2


# Juntar CPF + Digitos

cpf_dez_digitos.append(segundo_digito)
cpf_onze_digitos = "".join(map(str, cpf_dez_digitos))


print(f'CPF Válido: {cpf_onze_digitos}')

###TESTE



