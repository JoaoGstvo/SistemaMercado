from models.Bank import Bank

bank = Bank()

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
                9. Histórico Banco
                10. Voltar
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
                pass
            case 5:
                bank.show_account()
            case 6:
                pass
            case 7:
                pass
            case 8:
                menu_all()
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
                pass
            case 0:
                pass


def menu_adm_market():
    while True:
        menu = """
                =====================
                    Menu Mercado
                =====================
                1. Comprar
                2. Ver Itens
                3. Extrato
                4. Adicionar Itens
                5. Editar Itens
                6. Excluir Itens
                7. Histórico Mercado
                8. Sair
                """
        print(menu)
        option = int(input("Opção: "))

        match option:
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass


def menu_market():
    while True:
        menu = """
                =====================
                    Menu Mercado
                =====================
                1. Comprar
                2. Ver Itens
                3. Extrato
                8. Sair
                """
        print(menu)
        option = int(input("Opção: "))

        match option:
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass



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
            identifier = input("Email ou CPF:")
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
            teste = bank.create_account(cpf, name, age, role, email, password, balance)

        case 0:
            print("Saindo...")
            break

        case _:
            print("Opção inválida")