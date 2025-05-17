"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

cpf_cru = '04119599051'

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

digitos_1 = cpf_cru[9:11]
digitos_2 = str(primeiro_digito) + str(segundo_digito)

if digitos_1 == digitos_2:
     print("Seu CPF é valido!")
else:
     print("Seu CPF é inválido!")








