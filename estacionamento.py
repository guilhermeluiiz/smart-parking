from ticket import Ticket
from pagamento import Pix, Cartao, Dinheiro
from excecoes import (
    EstacionamentoLotadoError,
    VeiculoNaoEncontradoError,
    PagamentoInvalidoError,
)
 
class Estacionamento:

    def __init__(self):
        self.vagas = []        
        self.clientes = []       
        self.veiculos = []         
        self.tickets_ativos = {}   
        self.historico = []       

    def adicionar_vaga(self, vaga):
        self.vagas.append(vaga)

    def cadastrar_cliente(self, cliente):
        self.clientes.append(cliente)

    def cadastrar_veiculo(self, veiculo):
        veiculo.cliente.adicionar_veiculo(veiculo)
        self.veiculos.append(veiculo)

    def buscar_veiculo(self, placa):
        for veiculo in self.veiculos:
            if veiculo.placa == placa:
                return veiculo
        raise VeiculoNaoEncontradoError(placa)

    def buscar_vaga_livre(self):
        for vaga in self.vagas:
            if vaga.esta_livre():
                return vaga
        return None


    def registrar_entrada(self, placa):
        veiculo = self.buscar_veiculo(placa)

        vaga = self.buscar_vaga_livre()
        if vaga is None:
            raise EstacionamentoLotadoError()

        vaga.ocupar()
        ticket = Ticket(veiculo, vaga)
        self.tickets_ativos[placa] = ticket

        print(f"\nEntrada registrada! Vaga {vaga.numero} ocupada por {veiculo.modelo}.")


    def registrar_saida(self, placa, horas, forma_pagamento):
        if placa not in self.tickets_ativos:
            raise VeiculoNaoEncontradoError(placa)

        ticket = self.tickets_ativos.pop(placa)
        ticket.finalizar_ticket(horas)
        ticket.vaga.liberar()

        pagamento = self._criar_pagamento(forma_pagamento, ticket.valor)
        pagamento.processar_pagamento()
        ticket.exibir_ticket()

        self.historico.append(ticket)

    def _criar_pagamento(self, forma_pagamento, valor):

        forma_pagamento = forma_pagamento.lower().strip()

        if forma_pagamento == "pix":
            return Pix(valor)
        elif forma_pagamento == "cartao":
            return Cartao(valor)
        elif forma_pagamento == "dinheiro":
            return Dinheiro(valor)
        else:
            raise PagamentoInvalidoError()


    def relatorio(self):
        livres = sum(1 for vaga in self.vagas if vaga.esta_livre())
        ocupadas = len(self.vagas) - livres
        arrecadado = sum(ticket.valor for ticket in self.historico)

        print("\n========== RELATÓRIO ==========")
        print(f"Total de vagas       : {len(self.vagas)}")
        print(f"Vagas livres         : {livres}")
        print(f"Vagas ocupadas       : {ocupadas}")
        print(f"Clientes cadastrados : {len(self.clientes)}")
        print(f"Veículos cadastrados : {len(self.veiculos)}")
        print(f"Veículos no pátio    : {len(self.tickets_ativos)}")
        print(f"Tickets finalizados  : {len(self.historico)}")
        print(f"Total arrecadado     : R$ {arrecadado:.2f}")
        print("================================")

        if self.vagas:
            print("\n--- Status das vagas ---")
            for vaga in self.vagas:
                vaga.exibir_dados()