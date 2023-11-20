import random


def gerar_palvra():
    arquivo = open("palavras.txt", "r", encoding="utf-8")
    palavras = []
    for palavra in arquivo:
        palavra = palavra.strip()
        palavras.append(palavra)
    numero = random.randrange(0, len(palavras))
    palavra_sorteada = palavras[numero].upper()
    arquivo.close()
    return palavra_sorteada


def checar_letra(chute):
    if chute in '[A-Z]':
        print(chute)
    else:
        print(f'Caractere inválido: {chute}')
