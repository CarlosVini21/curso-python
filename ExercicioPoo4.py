class HoraExtra:
    def __init__(self,nome,salario, jornadaTrabalho):
        self.nome=nome
        self.salario=salario
        self.jornadaTrabalho=jornadaTrabalho
        
    def questionario(self):
        print("Digite seu nome")
        self.nome=input()
        print("Digite seu salario")
        self.salario=float(input())
        print("Digite sua Jornada de trabalho")
        self.jornadaTrabalho=int(input())
        
    def somaHoraExtra(self):
        if self.jornadaTrabalho>40:
            hora_extra=self.jornadaTrabalho-40
            return (self.salario/40)*0.5*hora_extra
        else:
            return 0
    
    def novoSalario(self):
        return self.salario+self.somaHoraExtra()
    
    def mostraDados(self):
        print(f"Olá {self.nome}")
        print(f"Quantidade de horas trabalhadas: {self.jornadaTrabalho:.2f}")
        print(f"valor das horas extras: {self.somaHoraExtra():.2f}")
        print(f"Novo salario: {self.novoSalario():.2f}")

HoraExtra=HoraExtra("",0,0)
HoraExtra.questionario()
HoraExtra.mostraDados()
    
