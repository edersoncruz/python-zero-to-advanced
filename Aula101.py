# Exercício - Adiando execução de funções
def soma(x, y):
    return x + y


def multiplica(x, y):
    return x * y

def somar_tudo_com_5 (*args):
    return sum(args)

def criar_funcao(funcao, *args_fixos):
    def interna(*args_novos):
        return funcao(*args_fixos ,*args_novos)
    return interna


soma_com_cinco = criar_funcao(soma, 5,)
multiplica_por_dez = criar_funcao(multiplica, 10)
somar_tudo_com_5 = criar_funcao(somar_tudo_com_5, 5)

teste1 = multiplica_por_dez(10)
teste2 = soma_com_cinco(10)
teste3 = somar_tudo_com_5(10,10,10,10,10)

print(teste1)
print(teste2)
print(teste3)
