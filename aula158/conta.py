from abc import ABC, abstractmethod
from banco import Banco
from pessoa import Cliente


class Conta(ABC):
    def __init__(self, agencia, numero_conta, saldo):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.saldo = saldo

    def depositar(self, valor):
        self.valor = valor
        self.saldo += valor

    @abstractmethod
    def sacar(self, valor):
        ...


class ContaCorrente(Conta):
    def __init__(self, agencia, numero_conta, saldo):
        super().__init__(agencia, numero_conta, saldo)

    def sacar(self, valor, banco, cliente):
        if banco.autenticar(cliente, self):
            if (self.saldo - valor) < -500:
                print("Saldo Insuficiente")
                return
            self.saldo -= valor


class ContaPoupanca(Conta):
    def __init__(self, agencia, numero_conta, saldo):
        super().__init__(agencia, numero_conta, saldo)

    def sacar(self, valor, banco, cliente):
        if banco.autenticar(cliente, self):
            if (self.saldo - valor) < 0:
                print("Saldo Insuficiente")
                return
            self.saldo -= valor


if __name__ == '__main__':

    conta1 = ContaCorrente(123, 123, 500)
    conta2 = ContaPoupanca(456, 456, 1000)

    cliente1 = Cliente('Ederson', 26, conta1)
    cliente2 = Cliente('Joao', 35, conta2)

    banco1 = Banco([conta1.agencia], [conta1], [cliente1])
    banco2 = Banco([conta2.agencia], [conta2], [cliente2])

    print()
    print(vars(banco1))
    print(vars(banco2))
    print()

    conta1.depositar(100)
    conta2.depositar(200)

    print()
    print(conta1.saldo)
    print(conta2.saldo)
    print()

    conta1.sacar(500, banco1, cliente1)
    conta2.sacar(500, banco2, cliente2)

    print(conta1.saldo)
    print(conta2.saldo)
    print()
