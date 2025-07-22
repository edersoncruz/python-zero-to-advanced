# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela


class Carro():
     def __init__ (self, nome, motor, fabricante):
        self.nome = nome
        self.motor = motor
        self.fabricante = fabricante

class Motor():
     def __init__ (self, nome):
        self.nome = nome


class Fabricante():
     def __init__ (self, nome):
        self.nome = nome

motor1 = Motor('1.0')
fabricante1 = Fabricante('Chevrolet')
carro1 = Carro('Fusca', motor1, fabricante1)
carro2 = Carro('Celta', motor1, fabricante1)

print(carro1.nome, carro1.motor.nome, carro1.fabricante.nome)
print(carro2.nome, carro2.motor.nome, carro2.fabricante.nome)