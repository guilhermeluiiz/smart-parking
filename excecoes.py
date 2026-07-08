class EstacionamentoLotadoError(Exception):

    def __init__(self):
        super().__init__("Não há vagas disponíveis no estacionamento.")


class VeiculoNaoEncontradoError(Exception):

    def __init__(self, placa):
        mensagem = f"Veículo com placa '{placa}' não foi encontrado."
        super().__init__(mensagem)


class VagaOcupadaError(Exception):

    def __init__(self, numero):
        mensagem = f"A vaga {numero} já está ocupada."
        super().__init__(mensagem)


class VagaLivreError(Exception):

    def __init__(self, numero):
        mensagem = f"A vaga {numero} já está livre."
        super().__init__(mensagem)


class PagamentoInvalidoError(Exception):

    def __init__(self):
        super().__init__("Forma de pagamento inválida.")
