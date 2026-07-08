# Smart Parking - Sistema de Estacionamento Inteligente

## Descrição
O **Smart Parking** é um sistema orientado a objetos que simula o gerenciamento
de um estacionamento. Ele resolve um problema real enfrentado por
estacionamentos de shoppings, condomínios e empresas: controlar de forma
organizada a entrada e saída de veículos, a ocupação das vagas, o cadastro de
clientes e o cálculo automático do valor a ser pago conforme o tipo de veículo
e o tempo de permanência.

## Integrantes
- Kaio Javã
- Guilherme
- Arthur

## Funcionalidades
- Cadastro de clientes
- Cadastro de veículos (carro, moto ou caminhão), vinculados a um cliente
- Registro de entrada de veículo (associação automática a uma vaga livre)
- Registro de saída de veículo, com cálculo da tarifa e pagamento (PIX,
  cartão ou dinheiro)
- Relatório geral do estacionamento (vagas livres/ocupadas, arrecadação, etc.)

## Conceitos de POO utilizados
- **Classes e objetos**: `Pessoa`, `Cliente`, `Funcionario`, `Veiculo`,
  `Carro`, `Moto`, `Caminhao`, `Vaga`, `Ticket`, `Pagamento`, `Pix`, `Cartao`,
  `Dinheiro`, `Estacionamento`.
- **Encapsulamento**: atributos internos como `_ocupada` (vaga) e os
  totalizadores do `Estacionamento` são manipulados apenas por métodos da
  própria classe.
- **Construtores**: todas as classes inicializam seus objetos via `__init__`.
- **Herança**: `Cliente` e `Funcionario` herdam de `Pessoa`; `Carro`, `Moto` e
  `Caminhao` herdam de `Veiculo`; `Pix`, `Cartao` e `Dinheiro` herdam de
  `Pagamento`.
- **Polimorfismo**: cada veículo sobrescreve `calcular_tarifa()` e
  `descricao()` com sua própria regra; cada forma de pagamento sobrescreve
  `processar_pagamento()`.
- **Abstração**: `Veiculo` e `Pagamento` são classes abstratas (`ABC`) que
  definem um contrato para as subclasses.
- **Associação**: `Veiculo` está associado a um `Cliente`; `Ticket` está
  associado a um `Veiculo` e a uma `Vaga`.
- **Agregação**: `Cliente` agrega uma lista de `Veiculo` (o veículo pode
  existir de forma independente do cliente que o cadastrou).
- **Composição**: `Estacionamento` é composto por `Vaga` e por `Ticket` — eles
  não existem fora do estacionamento que os criou.
- **Coleções de objetos**: listas (`vagas`, `clientes`, `veiculos`,
  `historico`) e dicionário (`tickets_ativos`).
- **Tratamento de exceções**: exceções personalizadas para vaga ocupada/livre,
  veículo não encontrado, estacionamento lotado e forma de pagamento inválida.
- **Modularização**: o sistema é dividido em módulos (`pessoa.py`,
  `veiculo.py`, `vaga.py`, `ticket.py`, `pagamento.py`, `estacionamento.py`,
  `excecoes.py`, `main.py`).

## Diagrama de Classes
Disponível na pasta [`imagens`](imagens/diagrama_classes.png).

## Tecnologias utilizadas
- Python 3
- Graphviz (geração do diagrama UML)
- Git / GitHub

## Como executar
```bash
git clone <link-do-repositorio>
cd estacionamento
python3 main.py
```

