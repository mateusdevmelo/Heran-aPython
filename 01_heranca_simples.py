class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas
    
    def ligar_mortor(self):
        print('Ligando o motor.')


class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def esta_carregado(self):
        print('Não estou carregado')

moto = Motocicleta('preta', 'abc-1234', 2)
moto.ligar_mortor()

carro = Carro('branco', 'xtv-8934', 4)
carro.ligar_mortor()

caminhao = Caminhao('cinza', 'lvt-1256', 8)
caminhao.ligar_mortor()
caminhao.esta_carregado()