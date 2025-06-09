class Banco():
    def __init__(self, agencias: list, contas: list, clientes: list):
        self.agencias = agencias
        self.clientes = clientes
        self.contas = contas

    def autenticar(self, cliente, conta):
        if conta.agencia not in self.agencias:
            print('Agência não pertence ao banco.')
            return False

        if cliente not in self.clientes:
            print('Cliente não pertence ao banco.')
            return False

        if conta not in self.contas:
            print('Conta não pertence ao banco.')
            return False

        if conta is not cliente.conta:
            print('Esta conta não pertence a este cliente.')
            return False
        return True


if __name__ == '__main__':
    ...
