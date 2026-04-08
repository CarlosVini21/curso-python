# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

#as maçãe custam R$1,30 cada se forem compradas menos de 1 duzia, e R$1,00 se forem compradas pelo menos 12.Escreva um programa que leia o número de maçãs comprdas pelo menos 12. Escreva um programa que leia o numero de maçãs compradas, calcule e revele o custo total.
print("Try programiz.pro")

print("digite um numero de maçãs compradas")
macas=int(input())

if macas>12:
    valor=macas*1
    print("o valor das maçães será", valor)
else:
    valor=macas*1.30
    print(" o valor das maçães serà", valor)
