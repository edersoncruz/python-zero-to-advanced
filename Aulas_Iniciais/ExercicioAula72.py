# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplicar(*args):
    total = 1
    for num in args:
        total *= num
    return total

resultado = multiplicar(1,3,3,5)
print(resultado)

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def verificar_par_impar(numero):
    if not isinstance(numero,int):
        return ("Erro: por favor, insira um número inteiro.")
                
    return f"Seu número {numero} é {'par' if numero % 2 == 0 else 'ímpar'}"

print (verificar_par_impar(resultado))
print (verificar_par_impar(3))
