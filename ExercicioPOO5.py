class Controle:
    def __init__(self,quantidadeEstoque=0,valor=0,nomeProduto="",encerrar="n"):
        self.quantidadeEstoque=quantidadeEstoque
        self.valor=valor
        self.nomeProduto=nomeProduto
        self.encerrar=encerrar
    
    def obterDado(self):
        while self.encerrar !="s":
            print("Diga o nome do produto")
            self.nomeProduto=input()
        
            print("Diga a quantidade em estoque")
            self.quantidadeEstoque=int(input())
        
            print("Diga o valor do produto")
            self.valor=float(input())
            
            self.MostraDados()
            print("deseja encerrar s/n")
            self.encerrar=input().lower()
        
        
    def saldoEstoque(self):
        return self.quantidadeEstoque*self.valor
        
    
    def MostraDados(self):
        print(f"Produto {self.nomeProduto}")
        print(f"Quantidade: {self.quantidadeEstoque}")
        print(f"Valor Unitario :{self.valor:.2f}")
        print(f"valor do estoque: {self.saldoEstoque():.2f}")
        
controle=Controle()
controle.MostraDados()
controle.obterDado()
