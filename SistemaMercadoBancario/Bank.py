from User import User
from Account import Account

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