from abc import ABC,abstractmethod
from datetime import datetime

class Conta(ABC):
    def __init__(self,titular):
        self.titular = titular
        self._saldo = 0
        self._historico = []

    def depositar(self,valor):
        if valor <= 0:
            raise ValueError('Erro, valor não suportado, use valores maior' \
            'que 0 ')
        else:
            self._saldo += valor
            depositar = Transacao('depositar',valor)
            self._historico.append(depositar)
            return f'Depósito de R${valor:.2f} realizado com sucesso'
           
    @abstractmethod
    def sacar(valor):
        ...

    def ver_saldo(self):
        return f'O saldo da conta de {self.titular} é: R${self._saldo:.2f}'

    def ver_historico(self):
        print(f'\n=== Histórico de Transações de {self.titular} ===')
        for tr in self._historico:
                print(tr)
        print()
        return 'Sucesso ✔'
    
    def ver_titular(self):
        return f'Conta de {self.titular}'
        

class ContaCorrente(Conta):
    def sacar(self,valor):
        if self._saldo <= valor:
            return f'Saldo insuficiente, deposite primeiro.'
        else:
            valor_taxa = valor + 2
            self._saldo -= valor_taxa
            sacar = Transacao('saque',valor_taxa)
            self._historico.append(sacar)
            return f'Saque de R${valor_taxa:.2f} realizado com sucesso por {self.titular}'
        
class ContaPoupança(Conta):
    def sacar(self,valor):
        if valor <= 0:
            print('Não e possivel sacar um valor neutro')
        elif valor > self._saldo:
            raise ValueError('Não e possivel sacar um dinheiro que vc nao tem.')
        else:
            self._saldo -= valor
            sacar_poupança = Transacao('saque',valor)
            self._historico.append(sacar_poupança)
            return f'Saque de R${valor:.2f} realizado com sucesso por {self.titular}'

class Transacao:
    def __init__(self,tipo,valor):
        self.tipo = tipo
        self.valor = valor
        self._data = datetime.now()

    def __str__(self):
        return f'[{self._data.strftime("%d/%m/%Y %H:%M:%S")}] {self.tipo.capitalize()}: R${self.valor:.2f}'

def menu(conta):
    while True:
        print("\n=== MENU BANCO PYTHON ===")
        print("1 - Depositar")
        print("2 - Sacar")
        print("3 - Ver saldo")
        print("4 - Ver histórico")
        print("5 - Ver Titular da conta")
        print("6 - Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            try:
                valor = float(input("Digite o valor para depósito: R$ "))
                print(conta.depositar(valor))
            except ValueError as e:
                print(f"Erro: {e}")

        elif opcao == '2':
            try:
                valor = float(input("Digite o valor para saque: R$ "))
                print(conta.sacar(valor))
            except ValueError as e:
                print(f"Erro: {e}")

        elif opcao == '3':
            print(conta.ver_saldo())

        elif opcao == '4':
            conta.ver_historico()

        elif opcao == '5':
            print()
            print('----->',conta.ver_titular())

        elif opcao == '6':
            print("Saindo do sistema. Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")

conta1 = ContaCorrente('Emanuel')
menu(conta1)



    

        

        

        



        