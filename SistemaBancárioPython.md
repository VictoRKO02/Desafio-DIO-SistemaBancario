# Sistema Bancário em Python

## Descrição

Este projeto é um sistema bancário simples desenvolvido em Python como parte de um desafio da Digital Innovation One (DIO). O objetivo do sistema é permitir que os usuários realizem operações bancárias básicas, como saques, depósitos e consultas de extrato. Adicionalmente, o sistema implementa algumas regras e limitações para operações de saque.

## Funcionalidades

### Menu de Opções

Ao iniciar o programa, o usuário é apresentado com um menu de opções:

1. **Saque**
2. **Depósito**
3. **Extrato**
4. **Resetar saques diários**

### Saque

- O sistema permite realizar até 3 saques diários.
- Cada saque tem um limite máximo de R$ 500,00.
- O sistema verifica se o usuário possui saldo suficiente antes de permitir o saque.
- Se o valor do saque for maior que o saldo ou o limite por saque, uma mensagem é exibida.
- Cada saque realizado é registrado no extrato.

### Depósito

- O usuário pode depositar qualquer valor positivo em sua conta.
- O saldo é atualizado após cada depósito.
- Cada depósito realizado é registrado no extrato.

### Extrato

- O usuário pode visualizar todas as operações realizadas (saques e depósitos) juntamente com o saldo atual após cada operação.
- Se não houver operações realizadas, o extrato indicará que nenhuma operação foi feita.

### Resetar Saques Diários

- O sistema permite resetar a contagem de saques diários, útil para simular um novo dia de operações.

## Exemplo de Uso

```python
# Código exemplo para uso do sistema bancário
import sistema_bancario

banco = sistema_bancario.SistemaBancario()

# Realizando um depósito
banco.depositar(1000)

# Realizando um saque
banco.sacar(200)

# Consultando extrato
print(banco.extrato())
