from abc import ABC, abstractmethod

class Veiculo(ABC):

    def __init__(self, placa, modelo, cliente):
        self.placa = placa
        self.modelo = modelo
        self.cliente = cliente  # associação: Veiculo -> Cliente

    @abstractmethod
    def calcular_tarifa(self, horas):
        pass

    @abstractmethod
    def descricao(self):
        pass

class Carro(Veiculo):

    TARIFA_HORA = 8

    def calcular_tarifa(self, horas):
        return horas * self.TARIFA_HORA

    def descricao(self):
        return (
            f"Carro | Modelo: {self.modelo} | "
            f"Placa: {self.placa} | "
            f"Cliente: {self.cliente.nome}"
        )


class Moto(Veiculo):

    TARIFA_HORA = 5

    def calcular_tarifa(self, horas):
        return horas * self.TARIFA_HORA

    def descricao(self):
        return (
            f"Moto | Modelo: {self.modelo} | "
            f"Placa: {self.placa} | "
            f"Cliente: {self.cliente.nome}"
        )


class Caminhao(Veiculo):

    TARIFA_HORA = 15

    def calcular_tarifa(self, horas):
        return horas * self.TARIFA_HORA

    def descricao(self):
        return (
            f"Caminhão | Modelo: {self.modelo} | "
            f"Placa: {self.placa} | "
            f"Cliente: {self.cliente.nome}"
        )
