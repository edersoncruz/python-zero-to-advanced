# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

# def duplica(num):
#     return num * 2

# def triplica(num):
#     return num * 3

# def quadruplica(num):
#     return num * 4

# print(duplica(5))
# print(triplica(5))
# print(quadruplica(5))


def criar_multiplicador(multiplicador):
    print(f"criar_multiplicador chamado com multiplicador = {multiplicador}")

    def multiplicar(numero):
        print(f"multiplicar chamado com numero = {numero} e multiplicador = {multiplicador}")
        return numero * multiplicador

    return multiplicar 


# Criando funções duplicar, triplicar e quadruplicar
duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

# Chamando as funções e imprimindo os resultados
print(duplicar(2))  # Chama multiplicar(2) com multiplicador fixado como 2
print(triplicar(2))  # Chama multiplicar(2) com multiplicador fixado como 3
print(quadruplicar(2))  # Chama multiplicar(2) com multiplicador fixado como 4
