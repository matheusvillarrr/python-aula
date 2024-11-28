class Cliente:
    def __init__(self, nome, cpf, endereco, telefone):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.telefone = telefone

    def exibir_informacoes(self):
        print(f"\nInformações do Cliente:")
        print(f"Nome: {self.nome}")
        print(f"CPF: {self. cpf}")
        print(f"Endereço: {self.endereco}")
        print(f"Telefone: {self.telefone}")


class Conta:
    def __init__(self, cliente, saldo=0):
        self.cliente = cliente
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
        print(f"\nExtrato da conta de {self.cliente.nome}:")
        for transacao in self.historico:
            print(transacao)
        print(f"Saldo atual: {self.saldo}")

    def emitir_historico(self):
        print(f"\nHistórico de transações da conta de {self.cliente.nome}:")
        for transacao in self.historico:
            print(transacao)


class Banco:
    def __init__(self):
        self.contas = []

    def cadastrar_conta(self, nome, cpf, endereco, telefone):
        cliente = Cliente(nome, cpf, endereco, telefone)
        nova_conta = Conta(cliente)
        self.contas.append(nova_conta)
        print(f"\nConta cadastrada para o cliente {nome}.")
        return nova_conta

    def buscar_conta_por_cpf(self, cpf):
        for conta in self.contas:
            if conta.cliente.cpf == cpf:
                return conta
        print("Conta não encontrada!")
        return None


def menu():
    banco = Banco()
    while True:
        print("\n===== Menu Principal =====")
        print("1. Cadastrar conta")
        print("2. Entrar em uma conta")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\nCadastro de Conta")
            nome = input("Informe o nome do cliente: ")
            cpf = input("Informe o CPF do cliente: ")
            endereco = input("Informe o endereço do cliente: ")
            telefone = input("Informe o telefone do cliente: ")
            banco.cadastrar_conta(nome, cpf, endereco, telefone)

        elif opcao == "2":
            cpf = input("\nInforme o CPF do cliente: ")
            conta = banco.buscar_conta_por_cpf(cpf)
            if conta:
                while True:
                    print("\n===== Menu da Conta =====")
                    print("1. Sacar")
                    print("2. Depositar")
                    print("3. Emitir Extrato")
                    print("4. Emitir Histórico")
                    print("5. Exibir Informações do Cliente")
                    print("6. Voltar ao Menu Principal")
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
                        conta.cliente.exibir_informacoes()
                    elif opcao_conta == "6":
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
