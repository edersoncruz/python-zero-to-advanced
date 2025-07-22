frase = 'O Python é uma linguagem de programação multiparadigma. Python foi criado por Guido Van Rossum'
frase_nova = frase.lower()

# Qual letra apareceu mais vezes na frase?

i = 0 
tamanho_frase = len(frase)
maximo = 0

while i < tamanho_frase:
    letra = frase_nova[i]

    if letra == ' ':
        i += 1
        continue


    quantidade_letras = frase_nova.count(letra)
    if quantidade_letras > maximo:
        maximo = quantidade_letras
        letra_maior = letra
    
    i += 1

print(maximo)
print(letra_maior)