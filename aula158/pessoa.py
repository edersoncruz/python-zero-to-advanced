from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade
    
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome (self, valor):
        self._nome = valor

    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade (self, valor):
        self._idade = valor


class Cliente(Pessoa):
    def __init__(self, nome, idade, conta):
        super().__init__(nome, idade)
        self.conta = conta

if __name__ == '__main__':
    from conta import ContaCorrente, ContaPoupanca
