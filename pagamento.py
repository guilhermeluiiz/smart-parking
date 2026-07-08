from abc import ABC, abstractmethod

class Pagamento(ABC):

    def __init__(self, valor):
        self.valor = valor

    @abstractmethod
    def processar_pagamento(self):
        pass


class Pix(Pagamento):

    def processar_pagamento(self):
        print("\n===== PAGAMENTO =====")
        print("Forma de pagamento: PIX")
        print(f"Valor pago: R$ {self.valor:.2f}")
        print("Pagamento realizado com sucesso!")
        print("=====================")


class Cartao(Pagamento):

    def processar_pagamento(self):
        print("\n===== PAGAMENTO =====")
        print("Forma de pagamento: Cartão")
        print(f"Valor pago: R$ {self.valor:.2f}")
        print("Pagamento realizado com sucesso!")
        print("=====================")


class Dinheiro(Pagamento):

    def processar_pagamento(self):
        print("\n===== PAGAMENTO =====")
        print("Forma de pagamento: Dinheiro")
        print(f"Valor pago: R$ {self.valor:.2f}")
        print("Pagamento realizado com sucesso!")
        print("=====================")