import json

def dicionario():
    with open('palavras.txt','r') as arquivo:
        conteudo = arquivo.read()
        listaPalavras = conteudo.split('\n')
    
    listaNumerica = {i : listaPalavras[i] for i in range(0, len(listaPalavras))}

    with open('palavras.json','w') as arquivo:
        arquivo.write(str(listaNumerica))
    

dicionario()

