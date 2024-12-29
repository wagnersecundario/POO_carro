class Carro:
    def __init__(self, marca, modelo, placa):
        self.__marca=marca
        self.__modelo=modelo
        self.__placa=placa
        self.__velocidade=0

    def imprimir(self):
        print(f'Marca: {self.__marca}, modelo: {self.__modelo}, placa: {self.__placa}')

    def acelerar(self, incremento):
        self.__velocidade+=incremento
        print(f'O carro acelerou para {self.__velocidade}km\h')

    def frear(self, decremento):
        self.__velocidade-=decremento
        if self.__velocidade<0:
            self.__velocidade=0
        print(f'O carro freou para {self.__velocidade}km\h')

    def set_marca(self, marca):
        self.__marca=marca
    def get_marca(self):
        return self.__marca
    
    def set_modelo(self, modelo):
        self.__modelo=modelo
    def get_modelo(self):
        return self.__modelo
    
    def set_placa(self, placa):
        self.__placa=placa
    def get_placa(self):
        return self.__placa
    

c=Carro('VW', 'Gol', 'AAA0B00')
c.imprimir()
c.acelerar(10)
c.frear(11)

c.set_marca('Fiat')
print('\nA nova marca é: ' + c.get_marca())
c.set_modelo('Argo')
print('O novo modelo é: ' + c.get_modelo())
c.set_placa('BBB1B11')  
print('A nova placa é: ' + c.get_placa())