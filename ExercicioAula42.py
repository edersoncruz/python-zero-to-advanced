frase = 'O Python é uma linguagem de programação multiparadigma. Python foi criado por Guido Van Rossum'
frase_nova = frase.lower()

# Qual letra apareceu mais vezes na frase?

i = 0 
tamanho_frase = len(frase)
max = 0

while i < tamanho_frase:
    letra = frase_nova[i]

    if letra == ' ':
        i += 1
        continue


    quantidade_letras = frase_nova.count(letra)
    if quantidade_letras > max:
        max = quantidade_letras
        letra_maior = letra
    
    i += 1

print(max)
print(letra_maior)