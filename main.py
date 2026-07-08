from estacionamento import Estacionamento
from pessoa import Cliente
from veiculo import Carro, Moto, Caminhao
from vaga import Vaga
from excecoes import (
    VeiculoNaoEncontradoError,
    EstacionamentoLotadoError,
    PagamentoInvalidoError,
)


estacionamento = Estacionamento()

clientes_cadastrados = []



# Criar vagas
for i in range(1, 6):
    estacionamento.adicionar_vaga(Vaga(i, "Comum"))



# Menu
while True:

    print("\n==============================")
    print("   SMART PARKING - MENU")
    print("==============================")

    print("\n1 - Cadastrar cliente")
    print("2 - Cadastrar veículo")
    print("3 - Entrada de veículo")
    print("4 - Saída de veículo")
    print("5 - Relatório")
    print("0 - Sair")

    opcao = input("\nEscolha uma opção: ")


    if opcao == "1":

        print("\n=== CLIENTE ===")

        nome = input("Nome: ")
        cpf = input("CPF: ")

        cliente = Cliente(nome, cpf)

        estacionamento.cadastrar_cliente(cliente)
        clientes_cadastrados.append(cliente)

        print("Cliente cadastrado com sucesso!")


    elif opcao == "2":

        if len(clientes_cadastrados) == 0:
            print("Cadastre um cliente primeiro!")
            continue

        print("\n=== VEÍCULO ===")

        print("Clientes disponíveis:")
        for i, c in enumerate(clientes_cadastrados):
            print(f"{i} - {c.nome}")

        try:
            indice = int(input("Escolha o cliente: "))
            cliente = clientes_cadastrados[indice]
        except (ValueError, IndexError):
            print("\nERRO: Cliente inválido.")
            continue

        placa = input("Placa: ")
        modelo = input("Modelo: ")
        tipo = input("Tipo (carro/moto/caminhao): ").lower().strip()

        if tipo == "carro":
            veiculo = Carro(placa, modelo, cliente)
        elif tipo == "moto":
            veiculo = Moto(placa, modelo, cliente)
        elif tipo == "caminhao":
            veiculo = Caminhao(placa, modelo, cliente)
        else:
            print("\nERRO: Tipo de veículo inválido.")
            continue

        estacionamento.cadastrar_veiculo(veiculo)

        print("Veículo cadastrado com sucesso!")

    elif opcao == "3":

        print("\n=== ENTRADA ===")

        placa = input("Placa: ")

        try:
            estacionamento.registrar_entrada(placa)

        except VeiculoNaoEncontradoError as e:
            print("\nERRO:", e)

        except EstacionamentoLotadoError as e:
            print("\nERRO:", e)

    elif opcao == "4":

        print("\n=== SAÍDA ===")

        placa = input("Placa: ")

        try:
            horas = int(input("Horas estacionado: "))
            forma_pagamento = input("Forma de pagamento (pix/cartao/dinheiro): ")

            estacionamento.registrar_saida(placa, horas, forma_pagamento)

        except VeiculoNaoEncontradoError as e:
            print("\nERRO:", e)

        except ValueError:
            print("\nERRO: Digite um número válido de horas.")

        except PagamentoInvalidoError as e:
            print("\nERRO:", e)

    elif opcao == "5":
        estacionamento.relatorio()


    elif opcao == "0":
        print("\nSaindo do sistema...")
        break

    else:
        print("\nOpção inválida. Tente novamente.")