numero=[10,7,5,6,8,4,3,2,1,0]
pares=0
impar=0
maior=0
menor=0
media=0
soma=0

for num in numero:
    if (num %2)==0:
        pares = pares+ 1
        
    else:
        impar= impar+1
        
soma = soma + num
media = soma/10

numero=[10,7,5,6,8,4,3,2,1,0]
pares=0
impar=0
maior=0
menor=0
media=0
soma=0

for num in numero:
    if (num % 2)==0:
        pares = pares + 1
    else:
        impar=impar +1
    if num > maior:
        maior=num
    else:
        num < menor
        menor = num
        
    soma = soma + num
media = soma/10

     
print("esse numero é par",pares)
print("esse numero é impar",impar)
print("esse é o total",soma)
print("esse é o maior numero",maior)
print("esse é o menor numero",menor)
print("essa é a media", media)
