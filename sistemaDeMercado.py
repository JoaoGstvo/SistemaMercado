# Sistema de Mercado
# Funções:
# Cadastrar produto
# Adicionar estoque
# Vender produto
# Ver estoque
# Ver histórico de vendas

produto = dict(id = 0, name = "", price = 0, estoque = 0)
lista_produto = []
extrato = []

def cadastrar_novo_produto(produto, lista_produto):
    nome_produto = input("Qual produto deseja cadastrar?: ")

    for i in lista_produto:
            if nome_produto == i["name"]:
                print("Desculpe, esse produto já existe!")

    preco_produto = input("Qual o preço deste produto?: ")
    estoque_produto = input("Quantos itens terá no Estoque?: ")
    
    try:
        int(preco_produto) and int(estoque_produto)
    
    except:
        print("Valor Inválido")
    
    else:
        produto["id"] = produto["id"] + 1
        produto["name"] = nome_produto
        produto["price"] = int(preco_produto)
        produto["estoque"] = int(estoque_produto)
    
        meu_produto = produto.copy()
    
        lista_produto.append(meu_produto)

    return lista_produto


def adicionar_estoque(lista_produto):
    produto_selecionado = input("Digite o Nome ou o ID do produto: ")

    try:
        int(produto_selecionado)
        for i in lista_produto:
            if i["id"] == int(produto_selecionado):
                novo_estoque = int(input("Quantos itens deseja adicionar?: "))
                i["estoque"] = i["estoque"] + novo_estoque

    except:
        for i in lista_produto:
            if i["name"] == produto_selecionado:
                novo_estoque = int(input("Quantos itens deseja adicionar?: "))
                i["estoque"] = i["estoque"] + novo_estoque

    return lista_produto
        

def vender_produto(lista_produto, extrato):
    produto_vender = input("Qual produto quer vender?: ")
    

    for i in lista_produto:
        if i["name"] == produto_vender:
            quantidade_produto = input("quantidade de itens a serem vendidos: ")
            if int(quantidade_produto) <= i["estoque"]:
                i["estoque"] = i["estoque"] - int(quantidade_produto)
                new_extrato = f"Foram vendidas {quantidade_produto} unidades do produto {produto_vender}"
                extrato.append(new_extrato)
                break

    else: 
            print("Não encontramos o produto ou não temos o estoque")
            

    return lista_produto, extrato


def verificar_estoque(lista_produto):
    produto = input("Qual produto deseja verificar o estoque?: ")
    for i in lista_produto:
        if i["name"] == produto:
            print (f'Estoque de: {i["estoque"]}') 


def ver_historico_vendas(extrato):
    print(extrato)


while True:
    opcao = input("")
    match opcao:
        case "a":
            cadastrar_novo_produto(produto, lista_produto)
        case "b":
            adicionar_estoque(lista_produto)
        case "c":
            verificar_estoque(lista_produto)
        case "d":
            vender_produto(lista_produto, extrato)
        case "e":
            ver_historico_vendas(extrato)
        case "f":
            print(lista_produto)