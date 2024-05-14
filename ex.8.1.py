class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print()

pessoa1 = Pessoa("Alice", 30)
pessoa2 = Pessoa("Bruno", 25)

print("Dados da primeira pessoa:")
pessoa1.mostrar_dados()

print("Dados da segunda pessoa:")
pessoa2.mostrar_dados()
