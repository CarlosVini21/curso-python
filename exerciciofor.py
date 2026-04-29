numeros=[]
soma=0
valor=float
while valor != 0:
    valor=float(input("Digite um numero (zero para fechar)"))
    numeros.append(valor)
for valor in numeros:
    soma = soma + valor
print(" a soma dos numeros é:",soma)
