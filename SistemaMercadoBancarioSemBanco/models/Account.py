
class Account:
    def __init__ (self, balance, email, password, history = None):
        self.balance = balance
        self.email = email
        self.password = password

        if history == None:
            self.history = []
        else:
            self.history = history