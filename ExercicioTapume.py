print("digite a largura")
varLargura=float(input())
print("digite o comprimento")
varComprimento=float(input())
print("Digite o tamanho do Tapume")
varTamanhoTapume=float(input())


tamanhoPiso=3.34
varArea= varLargura *varComprimento
varQuantCaixa=varArea/tamanhoPiso

varQuantTapume=varArea/varTamanhoTapume

print("aqui esta",round (varQuantCaixa))
print("aqui esta",round (varQuantTapume))

