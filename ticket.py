class Ticket:

    def __init__(self, veiculo, vaga):
        self.veiculo = veiculo 
        self.vaga = vaga    
        self.horas = 0
        self.valor = 0

    def finalizar_ticket(self, horas):
        self.horas = horas
        self.valor = self.veiculo.calcular_tarifa(horas)

    def exibir_ticket(self):
        print("\n========== TICKET ==========")
        print(f"Cliente : {self.veiculo.cliente.nome}")
        print(f"Veículo : {self.veiculo.modelo}")
        print(f"Placa   : {self.veiculo.placa}")
        print(f"Vaga    : {self.vaga.numero}")
        print(f"Horas   : {self.horas}")
        print(f"Valor   : R$ {self.valor:.2f}")
        print("============================")