from .User import User
from .Account import Account

class Bank:
    def __init__(self, user_list = None, history = None):
        
        if user_list == None:
            self.user_list = []
        else:
            self.user_list = user_list

        if history == None:
            self.history = []
        else:
            self.history = history



    def consult_account(self, identifier):  
        try:
            int(identifier)
            for i in self.user_list:
                if i.cpf == int(identifier):
                    return i
        except:
           return None
                
        return None



    def create_account(self, cpf, name, age, role, email, password, balance = 0):
        verify_account = self.consult_account(cpf)

        if verify_account:
            print("Este CPF já está sendo utilizado.")

        else:
            new_user = User(cpf, name, age, role)
            new_account = Account(balance, email, password)
            new_user.account = new_account

            self.user_list.append(new_user)

            print("Usuário Cadastrado")

            self.history.append(f"Conta criada para {name}.")
            new_account.history.append(f"Conta criada.")



    def delete_account(self, cpf):
        account = self.consult_account(cpf)

        if not account:
            print("Conta não encontrada.")

        else:
            self.user_list.remove(account)
            print("Conta deletada.")



    def show_account(self):
        for i in self.user_list:
            print(f"{i.cpf} | {i.name} | {i.age} | {i.role} | {i.account.email} | {i.account.password} | {i.account.balance} \n")



    def add_balance (user, money):
            user.account.balance += money



    def withdraw (user, money):
            user.account.balance -= money



    def transfer_balance(self, destiny, balance, user):
        verify_account = self.consult_account(destiny)

        if verify_account:
            user.account.balance -= balance
            verify_account.account.balance += balance

        else:
            print("Conta de destino não encontrada")



    def show_history(user):
        for i in user.account.history:
            print(i)



    def consult_balance(user):
        return user.account.balance
            
