import random

numeros_aleatorios = [random.randint(0, 10) for _ in range(9)]  # Gera 9 números entre 0 e 10
print(numeros_aleatorios)


cpf_cru = numeros_aleatorios

##Primeiro Digito

cpf_nove_primeiros = cpf_cru[:9]
valor_1 = 0
indice_reverso_1 = 10

for numero in cpf_nove_primeiros:
        numero_int = int(numero)
        valor_1 += numero_int * indice_reverso_1
        indice_reverso_1 -= 1 

resultado = (valor_1 * 10) % 11

if resultado > 9:
    primeiro_digito = 0
else:
    primeiro_digito = resultado

print(f'O seu primeiro dígito é: {primeiro_digito}')

##Segundo Dígito

cpf_dez_primeiros = cpf_cru[:10]
valor_2 = 0
indice_reverso_2 = 11

for numero in cpf_dez_primeiros:
        numero_int = int(numero)
        valor_2 += numero_int * indice_reverso_2
        indice_reverso_2 -= 1 

resultado = (valor_2 * 10) % 11

if resultado > 9:
    segundo_digito = 0
else:
    segundo_digito = resultado

print(f'O seu segundo dígito é: {segundo_digito}')

#Validar CPF

cpf_digitos = str(cpf_cru) + str(primeiro_digito) + str(segundo_digito)
print (f"Seu CPF: {cpf_digitos}")
