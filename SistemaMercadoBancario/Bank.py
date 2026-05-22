class Bank:
    def __init__(self, account_list = None):
        
        if account_list == None:
            self.account_list = []
        else:
            self.account_list = account_list



    def consult_account(self, identifier):  
        try:
            int(identifier)
            for i in self.account_list:
                if i.cpf == int(identifier):
                    return i
        
        except ValueError:
            print("CPF Inválido")
                
        return None
    


    def create_account(self, cpf, name, age, email, password):
        verify_account = self.consult_account(cpf)

        if verify_account:
            print("Este CPF já está sendo utilizado.")