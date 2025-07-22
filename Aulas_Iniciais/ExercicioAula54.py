"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""

lista_compras = []

while True:
    
    acao = input("[I]nserir [A]pagar [L]istar :")
    acao_isletra = acao.isalpha()
    acao_turnedlower = acao.lower()

    if acao_isletra:
        if len(acao_turnedlower) > 1:
            print("Digitar apenas uma letra com o comando desejado!")
            continue

        else:
            if acao_turnedlower == 'i':
                item = input("Digite o item: ")
                lista_compras.append(item)
        
            elif acao_turnedlower == 'a':
                
                if lista_compras == []:
                    print("Lista Vazia insira primeiro!")
                    continue
                else:
                    print ('Lista atual:')
                    
                    for i, item in enumerate(lista_compras):
                        print (i, item)
                    
                    item_apagar = input("Qual item deseja apagar ? Digite o índice: ")
                    
                    try:
                        item_apagar_int = int(item_apagar)
                        
                        if item_apagar_int > len(lista_compras):
                            print("Índice maior que a lista! ")
                        
                        else:
                            for i, item in enumerate(lista_compras):
                                if item_apagar_int == i:
                                    del lista_compras[i]
                            
                    except:
                        print("Digite um valor válido!")

            elif acao_turnedlower == 'l':

                if lista_compras == []:
                    print ("Lista vazia, insira primeiro!")
                    continue
                else:
                    for i, item in enumerate(lista_compras):
                        print (i, item)
        
            else:
                print("Digitar um dos comandos I - A - L")
    else:
        print("Digitar apenas letras!")
        continue
        #item = input("")