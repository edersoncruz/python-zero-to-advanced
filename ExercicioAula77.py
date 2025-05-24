# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

resposta_indice = 0
acertos = 0
erros = 0
for i, pergunta in enumerate(perguntas):
    print(f"\nPergunta {i+1} {pergunta['Pergunta']} \n")
    
    for i, opcoes in enumerate(pergunta['Opções']):
        print(f'{i+1}) {opcoes}')
        if opcoes == pergunta['Resposta']:
            resposta_indice = i + 1

    resposta_enviada = int(input("\nEscolher uma opção: "))
    if resposta_enviada == resposta_indice:
        print(f'\n"Acertou 👍"')
        acertos += 1 
    else:
        print(f'\n"Errou ❌"')
        erros += 1

print(f'\nVocê teve {acertos} acertos e {erros} erros')