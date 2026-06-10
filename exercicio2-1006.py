class produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def exibir_dados(self):
        return f'''
                   Produto: {self.nome}
                   Preço: R$ {self.preco}
                   Quantidade: {self.quantidade}'''

produtoo = produto("Caderno", 15.90, 3)

print(produtoo.exibir_dados())