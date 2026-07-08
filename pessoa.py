class Pessoa:

    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")


class Cliente(Pessoa):

    def __init__(self, nome, cpf):
        super().__init__(nome, cpf)
        self.veiculos = []  # agregação: Cliente "possui" Veiculos

    def adicionar_veiculo(self, veiculo):
        self.veiculos.append(veiculo)

    def exibir_dados(self):
        super().exibir_dados()
        print(f"Quantidade de veículos: {len(self.veiculos)}")


class Funcionario(Pessoa):

    def __init__(self, nome, cpf, cargo):
        super().__init__(nome, cpf)
        self.cargo = cargo

    def exibir_dados(self):
        super().exibir_dados()
        print(f"Cargo: {self.cargo}")
