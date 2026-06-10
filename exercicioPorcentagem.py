print("digite a quantidade de votos em branco")
votoBranco=float(input())

print("digite a quantidade de votos nulos")
votoNulo=float(input())

print("digite a quantidade de votos validos")
votoValido=float(input())

def totalVotos():
    return votoBranco + votoNulo+ votoValido
    
def percentVotoBranco():
    return (votoBranco/totalVotos()) *100
    
def percentVotoNulo():
    return (votoNulo/totalVotos())*100
    
def percentVotoValido():
    return (votoValido / totalVotos())*100
    
def mostraDados():
    print(f"O total de Votos é: {totalVotos():.2f}")
    print(f"O percentual de votos Brancos é: {percentVotoBranco():.2f}%")
    print(f"O percentual de votos Nulos é: {percentVotoNulo():.2f}%")
    print(f"O percentual de votos Valido é: {percentVotoValido():.2f}%")
mostraDados()
