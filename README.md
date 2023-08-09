# Sistema Bancário

Este é um simples sistema bancário em Python que permite realizar operações de depósito, saque e visualização de extrato em uma conta bancária.

## Funcionalidades

- Depositar: Permite realizar depósitos em uma conta bancária. O saldo da conta é atualizado de acordo com o valor depositado.

- Sacar: Permite realizar saques em uma conta bancária. O saldo da conta é atualizado de acordo com o valor sacado, desde que o limite de saques e o saldo disponível sejam respeitados.

- Extrato: Permite visualizar o extrato das movimentações realizadas na conta bancária. O extrato exibe os detalhes dos depósitos e saques feitos, bem como o saldo atual.

## Requisitos

- Python 3.x

## Novas funções

Cadastrar usuário(cliente), cadastrar conta bancaria (vinculando essa conta ao usuário) e listar contas.

Cadastrar usuário: o programa deve armazenar os usuarios em uma lista, um usuario é composto por: nome, data de nascimento, cpf e endereço. O endereço é uma string com o formato: logradouro, numero - bairro - cidade/sigla do estado. CPF deve ser somente numeros e não podem ter 2 usuarios com o mesmo CPF.

Cadastrar conta bancaria: Deve armazenar contas em uma lista, a conta é composta por: agência, número da conta e usuário. O numero é sequencial começando em 1. O numero da agência sempre será 0001. O usuário pode ter mais de uma conta, uma conta pode pertence a somente um usuario.

Além disso a função saque deve receber os argumentos apenas por nome(keyword only).

A função de deposito deve receber os argumentos apenas por posição(positional only).

A função extrato deve receber os argumentos por posição e nome(keyword only e positional only). Argumentos posicionais: saldo, Argumentos nomeados: extrato
