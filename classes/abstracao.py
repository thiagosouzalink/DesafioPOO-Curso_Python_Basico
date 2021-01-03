from abc import ABC, abstractmethod

class Pessoa:

    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    # Getters
    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade

    

class Conta(ABC):

    def __init__(self, agencia, conta, saldo):
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo

    def depositar(self, valor):
        self._saldo += valor
        self.detalhes_conta()

    def detalhes_conta(self):
        print(f"Agência: {self._agencia}")
        print(f"Conta: {self._conta}")
        print(f"Saldo: R${self._saldo:.2f}")

    @abstractmethod
    def sacar(self):
        pass