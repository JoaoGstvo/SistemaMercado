from Product import Product

class Market:
    def __init__(self, itens_list = None):
        
        if itens_list == None:
            self.itens_list = []
        else:
            self.itens_list = itens_list

    

    def consult_product(self, name):
        for i in self.itens_list:
            if i.name == name:
                return i
        else:
            return None



    def add_product(self, name, price, storage = 0):
        verify = self.consult_product(name)

        if not verify:
            new_product = Product(name, price, storage)
            print(f"Produto {new_product.name} adicionado a lista.")
        else:
            print("Este produto já existe.")



    def sell_product(self, name, qtd):
        verify = self.consult_product(name)

        if verify:
            if verify.storage > 0:
                if verify.storage <= qtd:
                    verify.storage -= qtd
                    print("Vendido.")
                else:
                    print("Quantidade em estoque não disponível.")
            else:
                print("Quantidade para comprar tem que ser maior do que 0.")
        else:
            print("Este produto não existe")


    def show_product(self):
        for i in self.itens_list:
            print(i.name, i.price, i.storage)