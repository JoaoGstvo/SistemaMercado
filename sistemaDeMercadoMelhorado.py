# Funções:
# Cadastrar produto
# Adicionar estoque
# Vender produto
# Ver estoque
# Ver histórico de vendas

class Product:
    def __init__(self, id, name, price, storage):
        self.id = id
        self.name = name
        self.price = price
        self.storage = storage



class Market:
    def __init__(self, itens_list = None, itens_updates = None):
        
        if itens_list == None:
            self.itens_list = []
        else:
            self.itens_list = itens_list

        if itens_updates == None:
            self.itens_updates = []
        else:
            self.itens_updates = itens_updates


        self.id_count = 0



    def consult_product(self, product):
        try:
            int(product)
            for i in self.itens_list:
                if int(product) == i.id:
                    return i
        except:
            for i in self.itens_list:
                if product.lower().strip() == i.name:
                    return i
                
        return None
            


    def add_product(self, name, price, storage):
        
        if not self.consult_product(name):
            self.id_count +=1
            new_product = Product(self.id_count, name, price, storage)
            self.itens_list.append(new_product)

            self.itens_updates.append(f"Produto {name} adicionado ao catálogo.")
            print("Produto adicionado")

        else:
            print("Produto já existe")



    def sell_product(self, name, qtd):

        product_to_sell = self.consult_product(name)

        if product_to_sell:
            if qtd > 0:
                if qtd <= product_to_sell.storage:
                    product_to_sell.storage -= qtd
                    print("Venda realizada com sucesso.")
                    self.itens_updates.append(f"Vendeu {qtd} unidade(s) do produto {name}")

                else:
                    print(f"Sem estoque suficiente. Estoque do produto {name}: {product_to_sell.storage}")
            else:
                print("Quantidade Inválida")
        else:
            print("Produto não encontrado")



    def delete_product(self, name):
        product_to_delete = self.consult_product(name)

        if product_to_delete:
            self.itens_list.remove(product_to_delete)
            self.itens_updates.append(f"O produto {name} foi excluído do catálogo")
            print("Produto excluído com sucesso.")

        else:
            print("Este produto não existe")



    def add_stock(self, product, storage):
        new_stock = self.consult_product(product)
        if storage > 0:
            if new_stock:
                new_stock.storage += storage

            else:
                print("Produto não encontrado")
        else:
            print("Quantidade inválida")
            return

        print(f"Produto {product} atualizado com sucesso.")
        

    
    def show_itens(self):
        if len(self.itens_list) > 0:
            for i in self.itens_list:
                print(f"{i.id} | {i.name} | R${i.price} | {i.storage}")
        else:
            print("Nenhum produto encontrado.")



    def show_update(self):
        if len(self.itens_updates) > 0:
            for i in self.itens_updates:
                print("-> " + i)
        else:
            print("Nenhuma movimentação foi feita.")


market = Market()

while True:
    option = input("Opção: ")

    match option:
        case "1":
            try:
                name = input("Nome: ").lower().strip()
                if name == "":
                    raise ValueError
                price = float(input("Preço: "))
                storage = int(input("Storage: "))
                market.add_product(name, price, storage)

            except ValueError:
                print("Valor inválido!")

        case "2":
            try:
                name = input("Nome: ").lower().strip()
                if name == "":
                    raise ValueError
                qtd = int(input("Quantidade: "))
                market.sell_product(name, qtd)

            except ValueError:
                print("Valor inválido!")

        case "3":
            try:
                name = input("Nome: ").lower().strip()
                if name == "":
                    raise ValueError
                
                qtd = int(input("Quantidade: "))
                market.add_stock(name, qtd)

            except ValueError:
                print("Valor inválido")

        case "4":
            try:
                name = input("Nome: ").lower().strip()
                if name == "":
                    raise ValueError
                else:
                    market.delete_product(name)
                
            except ValueError:
                print("Valor inválido")

        case "5":
            market.show_itens()

        case "6":
            market.show_update()

        case _:
            print("Opção inválida!")


