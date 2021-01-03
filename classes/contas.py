from .abstracao import Conta


class ContaPoupanca(Conta):

    def __init__(self, agencia, conta, saldo):
        super().__init__(agencia, conta, saldo)

    # Getter
    @property
    def agencia(self):
        return self._agencia

    @property
    def conta(self):
        return self._conta

    @property
    def saldo(self):
        return self._saldo


    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente")
        else:
            self._saldo -= valor
            print(f"Saque: R${valor:.2f}")
            self.detalhes_conta()


class ContaCorrente(Conta):
    
    def __init__(self, agencia, conta, saldo, limite=100):
        super().__init__(agencia, conta, saldo)
        self._limite = limite
    # Getter
    @property
    def agencia(self):
        return self._agencia

    @property
    def conta(self):
        return self._conta

    @property
    def saldo(self):
        return self._saldo

    @property
    def limite(self):
        return self._limite


    def sacar(self, valor):
        if valor > self.saldo + self.limite:
            print("Saldo e limite insuficientes")
        elif valor <= self.saldo:
            self._saldo -= valor
            print(f"Saque: R${valor:.2f}")
            self.detalhes_conta()
            print(f"Limite: R${self.limite:.2f}")
        else:
            print("limite acionado")
            print(f"Saque: R${valor:.2f}")
            valor -= self._saldo
            self._limite -= valor
            self._saldo = 0
            self.detalhes_conta()
            print(f"Limite: R${self.limite:.2f}")

            
        
