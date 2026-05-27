class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def cumprimentar(self):
        print(f"meu nome é {self.nome},tenho {self.idade},anos")
        
pessoa1 = Pessoa("Carlos",26)
pessoa1.cumprimentar()
