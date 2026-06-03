from models import Bank, Account, User

bank = Bank()
account = Account()

user_logged = None

def login(bank, identifier, password):
    verify_account = bank.consult_account(identifier)

    if verify_account:
        if password == verify_account.account.password:
            user_logged = verify_account
            return user_logged
        else:
            print("Senha incorreta.")
    else:
        print("Conta não encontrada.")
        
    

while True:
    """
    ======================
        TELA INICIAL
    ======================
    1. Login
    2. Cadastro

    """

    opcao = int(input("Opção: "))

    match opcao:
        case 1:
            pass