class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    
    def mostrar_dados(self):
        print("Nome:", self.nome)
        print("Preço:", self.preco)
        print("Quantidade em estoque:", self.quantidade)

class ProdutoImportado(Produto):
    def __init__(self, nome, preco, quantidade, imposto):
        super().__init__(nome, preco, quantidade)
        self.imposto = imposto
    
    def preco_final(self):
        return self.preco * (1 + self.imposto)

produto_importado = ProdutoImportado("Notebook", 2500, 5, 0.15)

print("Dados do produto importado:")
produto_importado.mostrar_dados()

print("Preço final do produto com imposto:", produto_importado.preco_final())
