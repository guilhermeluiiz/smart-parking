from excecoes import VagaOcupadaError, VagaLivreError


class Vaga:

    def __init__(self, numero, tipo):
        self.numero = numero
        self.tipo = tipo
        self.ocupada = False

    def ocupar(self):
        
        if self.ocupada:
            raise VagaOcupadaError(self.numero)
        self.ocupada = True

    def liberar(self):
        
        if not self.ocupada:
            raise VagaLivreError(self.numero)
        self.ocupada = False

    def esta_livre(self):
        
        return not self.ocupada

    def exibir_dados(self):
        
        status = "Ocupada" if self.ocupada else "Livre"
        print(f"Vaga: {self.numero}")
        print(f"Tipo: {self.tipo}")
        print(f"Status: {status}")
