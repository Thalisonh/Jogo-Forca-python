import PySimpleGUI as sg
import random
import json
#transformar string em dicionario
import ast

#abre o arquivo com as palavras brasileiras
with open('palavras.json','r') as arquivo:
    conteudo = arquivo.read()

#salva o json em um dicionario
dicionario = ast.literal_eval(conteudo)

rand = (random.randint(0, 28638))

escondida = list(dicionario[rand])
tamanho = len(escondida)
asteriscos = list('_' * tamanho)
letraCerta = list('_' * tamanho)
letrasDigitadas = list()
letra = list()
cont = True

print(asteriscos)
def forca(escondida, tamanho,letra, asteriscos, letraCerta):
    for i in range(tamanho):
        if letra == escondida[i]:
            letraCerta[i] = letra
            asteriscos[i] = escondida[i]
            print(asteriscos)
            if letraCerta == escondida:
                print("VOCE GANHOU")
                return 0

while(cont != 0):
    letra = input('Digite uma letra: ').upper()
    cont = forca(escondida, tamanho, letra, asteriscos, letraCerta)
    


