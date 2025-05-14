"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""


numero_inteiro = input("Digite um número inteiro: ")

if numero_inteiro.isdigit():
    numero_inteiro_int = int(numero_inteiro)

    if (numero_inteiro_int % 2) == 0:
        print("Seu número é par")
    else:
        print("Seu número é impar")
else:
    print("Você não digitou um inteiro!")