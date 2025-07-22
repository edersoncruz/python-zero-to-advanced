nome = "Ederson Cruz"
tamanho = len(nome)
contador = 0
novo_nome = ''
while contador < tamanho:
    novo_nome += nome[contador] + "*"
    contador += 1
print (novo_nome)