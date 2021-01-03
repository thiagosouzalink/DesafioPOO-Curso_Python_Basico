class Banco:

    def __init__(self):
        self._agencias = []
        self._clientes = []
        self._contas = []

    # Getters
    @property
    def agencias(self):
        return self._agencias
    
    @property
    def clientes(self):
        return self._clientes

    @property
    def contas(self):
        return self._contas
    

    def cadastrar_agencia(self, agencia):
        self.agencias.append(agencia)
    
    def cadastrar_cliente(self, cliente):
        self.clientes.append(cliente.nome)
        self.contas.append(cliente.conta.conta)
    

    def autenticar(self, cliente):
        if cliente.conta.agencia not in self.agencias:
            print(f"Agência {cliente.conta.agencia} não pertence a este banco.")
            return False
        
        if cliente.nome not in self.clientes:
            print(f"Cliente {cliente.nome} não pertence a este banco.")
            return False
        
        if cliente.conta.conta not in self.contas:
            print(f"Conta {cliente.conta.conta} não pertence a este banco.")
            return False
        
        return True
