from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, agencia, numero_conta, saldo):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.saldo = saldo        

    def deposito(self, valor):
        self.valor = valor
    
    @abstractmethod
    def sacar(self, valor):
        ...

class  ContaCorrente(Conta):
    def __init__(self, agencia, numero_conta, saldo):
        super().__init__(agencia, numero_conta, saldo)
    
    def sacar(self, valor):
        self.valor = valor

        if (self.saldo - valor) < -500:
            return print("Saldo Insuficiente")
        
        self.saldo -= valor
        


class  ContaPoupanca(Conta):
    def __init__(self, agencia, numero_conta, saldo):
        super().__init__(agencia, numero_conta, saldo)
    
    def sacar(self, valor):
        if (self.saldo - valor) < 0:
            return print("Saldo Insuficiente")
        
        self.saldo -= valor

conta1 = ContaCorrente(123, 123, 500)
conta2 = ContaPoupanca(123, 123, 500)

print(conta1.saldo)
print(conta2.saldo)

conta1.sacar(5000)
conta2.sacar(40000)

print(conta1.saldo)
print(conta2.saldo)
