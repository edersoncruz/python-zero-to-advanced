"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

palavra_secreta = 'ederson'
tentativas = 0
palavra_descoberta = ['*'] *len(palavra_secreta)

print('Para descobrir a palavra secreta digite uma letra por vez, caso a letra esteja certa irei retornar que você acertou, caso contrário irá apenas aparecer um *')

while True: 
    letra_recebida = input('Digite uma letra: ')

    if len(letra_recebida) > 1:
        print ("Digite apenas 1 caractere de letra")
        continue

    else:
        is_letra = letra_recebida.isalpha() #verifica se é uma letra mesmo

        if is_letra:
            
            tentativas += 1

            if letra_recebida in palavra_secreta:
                
                for i, letra in enumerate(palavra_secreta):
                    if letra == letra_recebida:
                        palavra_descoberta[i] = letra_recebida
                
                print(letra_recebida)

                palavra_descoberta_formatada = "".join(palavra_descoberta)

                print(f'Palavra descoberta até agora: {palavra_descoberta_formatada}')

                if palavra_descoberta_formatada == palavra_secreta:
                    print(f"Você descobriu a palavra {palavra_descoberta_formatada} e a palavra secreta era {palavra_secreta} com {tentativas} tentativas")
                    break
            else:
                print(f'Palavra descoberta até agora: {palavra_descoberta_formatada}')

        else:
            print("O que você digitou não é uma letra!")
            continue