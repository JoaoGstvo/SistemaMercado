class Bank:
    def __init__(self, account_list = None, id_count = 0):
        
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
        
        except:
            for i in self.account_list:
                if i.email == identifier:
                    return i
                
        return None