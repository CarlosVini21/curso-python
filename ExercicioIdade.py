varMes=0
VarAno=0
varDia=0
varIdade=0
varNome=0

print("Digite seu nome")
varNome=input()

print("Digite sua idade/Anos")
varAno=int(input())

print("Digite sua idade/Mes")
varMes=int(input())

print("Digite sua idade/dias")
varDia=int(input())
varIdade= (varAno*365)+(varMes*30)+varDia

print("você",varNome)
print("tem essa idade em dias",varIdade)
