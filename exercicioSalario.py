print("digite seu nome")
nome=input()
print("informe a quantidade de horas trabalhadas")
horasTrabalhadas=float(input())
print("digite seu salario")
salario=float(input())

def salarioHora():
    return salario/220
    
def novoSalario():
    if horasTrabalhadas >40:
        horasExtras=horasTrabalhadas-40
        valorHoraExtra=salarioHora()*1.5
        salarioExtra=horasExtras * valorHoraExtra
        return salario + salarioExtra
    else:
        return salario
       
            
def mostraDados():
    print (f"seu salario por hora é $,{salarioHora():.2f}")
    print(f"seu novo salario é $,{novoSalario():.2f}")
    
mostraDados()
