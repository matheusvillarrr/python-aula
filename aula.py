class Conta:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
        self.historico = []

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente!")
        else:
            self.saldo -= valor
            self.historico.append(f"Saque: -{valor}")
            print(f"Saque realizado. Saldo atual: {self.saldo}")

    def depositar(self, valor):
        self.saldo += valor
        self.historico.append(f"Depósito: +{valor}")
        print(f"Depósito realizado. Saldo atual: {self.saldo}")

    def emitir_extrato(self):
        print(f"Extrato da conta de {self.titular}:")
        for transacao in self.historico:
            print(transacao)
        print(f"Saldo atual: {self.saldo}")

    def emitir_historico(self):
        print(f"Histórico de transações da conta de {self.titular}:")
        for transacao in self.historico:
            print(transacao)


class Banco:
    def __init__(self):
        self.contas = []

    def cadastrar_conta(self, titular):
        nova_conta = Conta(titular)
        self.contas.append(nova_conta)
        print(f"Conta cadastrada para {titular}.")

    def buscar_conta(self, titular):
        for conta in self.contas:
            if conta.titular == titular:
                return conta
        print("Conta não encontrada!")
        return None


def menu():
    banco = Banco()
    while True:
        print("\n===== Menu Principal =====")
        print("1. Cadastrar conta")
        print("2. Logar em conta")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titular = input("Informe o nome do titular: ")
            banco.cadastrar_conta(titular)
        elif opcao == "2":
            titular = input("Informe o nome do titular: ")
            conta = banco.buscar_conta(titular)
            if conta:
                while True:
                    print("\n===== Menu da Conta =====")
                    print("1. Sacar")
                    print("2. Depositar")
                    print("3. Emitir Extrato")
                    print("4. Emitir Histórico")
                    print("5. Voltar ao Menu Principal")
                    opcao_conta = input("Escolha uma opção: ")

                    if opcao_conta == "1":
                        valor = float(input("Informe o valor para saque: "))
                        conta.sacar(valor)
                    elif opcao_conta == "2":
                        valor = float(input("Informe o valor para depósito: "))
                        conta.depositar(valor)
                    elif opcao_conta == "3":
                        conta.emitir_extrato()
                    elif opcao_conta == "4":
                        conta.emitir_historico()
                    elif opcao_conta == "5":
                        break
                    else:
                        print("Opção inválida!")
        elif opcao == "3":
            print("Encerrando o sistema. Até logo!")
            break
        else:
            print("Opção inválida!")


# Executa o sistema
menu()
