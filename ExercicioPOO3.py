class Olerite:
    def __init__(self,nome,salarioBruto):
        self.nome=nome
        self.salarioBruto=salarioBruto
        
    def apresentadados(self):
        self.nome=input("Digite seu nome:")
        self.salarioBruto=float(input("Digite seu salario:"))
            
    def desconto(self):
        return self.salarioBruto*(0.05+0.11+0.08)
        
    def salarioHora(self):
        return self.salarioBruto/220
            
    def salarioLiquido(self):
        return self.salarioBruto-self.desconto()
            
    def folhapagamento(self):
        print(f"ola {self.nome}")
        print(f"salario por hora {self.salarioHora():.2f}")
        print(f"Descontos {self.desconto():.2f}")
        print(f"Salario Liquido{self.salarioLiquido():.2f}")
                  
Olerite=Olerite("",0)
Olerite.apresentadados()
Olerite.folhapagamento()
            
        
