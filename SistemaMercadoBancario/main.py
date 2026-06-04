from models import Bank, Account, User

bank = Bank()
account = Account()

user_logged = None


def login(identifier, password, bank):
    verify_account = bank.consult_account(identifier)

    if verify_account:
        if password == verify_account.account.password:
            user_logged = verify_account
            return user_logged
        else:
            print("Senha incorreta.")
    else:
        print("Conta não encontrada.")
        

def menu_all(user):
    while True:
        menu = """
                =====================
                    Menu Principal
                =====================
                1. 
                2.
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
                1. 
                2.
                3.
                4.
                5.
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


def menu_bank():
    while True:
        menu = """
                =====================
                    Menu Banco
                =====================
                1. 
                2.
                3.
                4.
                5.
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


def menu_adm_market():
    while True:
        menu = """
                =====================
                    Menu Mercado
                =====================
                1. 
                2.
                3.
                4.
                5.
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
                1. 
                2.
                3.
                4.
                5.
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

        case 2:
            pass

        case _:
            print("Opção inválida")