from models.Bank import Bank
from models.Market import Market

bank = Bank()
market = Market()

user_logged = None



def login(identifier, password):
    verify_account = bank.consult_account(identifier)

    if verify_account:
        if password == verify_account.account.password:
            user_logged = verify_account
            return user_logged
        else:
            print("Senha incorreta.")



def menu_all(user):
    while True:
        menu = """
                =====================
                    Menu Principal
                =====================
                1. Banco
                2. Mercado
                0. Sair
                """
        print(menu)
        option = int(input("Opção: "))

        match option:
            case 1:
                if user.role == "managerbank":
                    menu_adm_bank()
                else:
                    menu_bank()

            case 2:
                if user.role == "managermarket":
                    menu_adm_market()
                else:
                    menu_market()

            case 0:
                print("Saindo...")
                break

            case _:
                print("Opção inválida.")



def menu_adm_bank():
    while True:
        menu = """
                =====================
                    Menu Banco
                =====================
                1. Depositar
                2. Sacar
                3. Transferir
                4. Extrato
                5. Mostrar Contas
                6. Editar Conta
                7. Deletar Conta
                8. Histórico Banco
                9. Voltar
                0. Sair
                """
        print(menu)
        option = int(input("Opção: "))

        match option:
            case 1:
                qtd = int(input("Quanto deseja depositar: "))
                bank.add_balance(user=user_logged, money=qtd)

            case 2:
                qtd = int(input("Quanto deseja sacar: "))
                bank.withdraw(user_logged, qtd)

            case 3:
                destiny = int(input("Conta de destino (CPF): "))
                qtd = int(input("Quanto deseja Transferir: "))
                bank.transfer_balance(destiny, qtd, user_logged)

            case 4:
                bank.show_history(user_logged)

            case 5:
                bank.show_account()

            case 6:
                pass

            case 7:
                user = int(input("Conta a ser excluída (CPF): "))
                bank.delete_account(user)
                
            case 8:
                for i in bank.history:
                    print(i)

            case 0:
                break



def menu_bank():
    while True:
        menu = """
                =====================
                    Menu Banco
                =====================
                1. Depositar
                2. Sacar
                3. Transferir
                4. Extrato
                5. Voltar
                0. Sair
                """
        print(menu)
        option = int(input("Opção: "))

        match option:
            case 1:
                qtd = int(input("Quanto deseja depositar: "))
                bank.add_balance(user_logged, qtd)

            case 2:
                qtd = int(input("Quanto deseja sacar: "))
                bank.withdraw(user_logged, qtd)
                
            case 3:
                destiny = int(input("Conta de destino (CPF): "))
                qtd = int(input("Quanto deseja Transferir: "))
                bank.transfer_balance(destiny, qtd, user_logged)

            case 4:
                bank.show_history(user_logged)

            case 5:
                menu_all(user_logged)
                
            case 0:
                pass


def menu_adm_market():
    while True:
        menu = """
                =====================
                    Menu Mercado
                =====================
                1. Comprar
                2. Ver Produtos
                3. Extrato
                4. Adicionar Produtos
                5. Editar Produtos
                6. Excluir Produtos
                7. Histórico Mercado
                8. Voltar
                9. Sair
                """
        print(menu)
        option = int(input("Opção: "))

        match option:
            case 1:
                name = input("Nome do produto: ")
                qtd = int(input("Quantidade desejada: "))

                market.sell_product(name, qtd, user_logged)

            case 2:
                market.show_product()
            case 3:
                pass

            case 4:
                name = input("Novo nome: ")
                price = float(input("Novo preço: "))
                storage = int(input("Novo Estoque: "))

                market.add_product(name, price, storage)

            case 5:
                name = input("Nome do produto: ")
                verify = market.consult_product(name)

                if verify:
                    new_name = input("Novo nome: ")
                    new_price = float(input("Novo preço: "))
                    new_storage = int(input("Novo Estoque: "))

                    market.edit_item(new_name, new_price, new_storage, verify)
                else:
                    print("Produto não encontrado.")

            case 6:
                name = input("Nome do produto: ")
                market.delete_product(name)

            case 7:
                pass

            case 8:
                menu_all()

            case 9:
                break



def menu_market():
    while True:
        menu = """
                =====================
                    Menu Mercado
                =====================
                1. Comprar
                2. Ver Produtos
                3. Extrato
                4. Voltar
                0. Sair
                """
        print(menu)
        option = int(input("Opção: "))

        match option:
            case 1:
                name = input("Nome do produto: ")
                qtd = int(input("Quantidade desejada: "))

                market.sell_product(name, qtd, user_logged)

            case 2:
                market.show_product()
            case 3:
                pass
            case 4:
                menu_all()
            case 0:
                break



while True:
    menu = """
            ======================
            TELA INICIAL
            ======================
            1. Login
            2. Cadastro
            0. Sair
            """
        
    print(menu)

    option = int(input("Opção: "))

    match option:
        case 1:
            identifier = input("Email ou CPF: ")
            password = input("Senha: ")
            user_logged = login(identifier, password)

            if user_logged:
                menu_all(user_logged)
            else:
                print("Usuário não encontrado")

        case 2:
            cpf = int(input("CPF (Apenas os Números): "))
            name = input("Nome: ")
            age = int(input("Idade: "))
            role = "managerbank"
            email = input("Email: ")
            password = input("Senha: ")
            balance = 0
            bank.create_account(cpf, name, age, role, email, password, balance)

        case 0:
            print("Saindo...")
            break

        case _:
            print("Opção inválida")