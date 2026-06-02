from models import Bank, Account, User

bank = Bank()
account = Account()

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