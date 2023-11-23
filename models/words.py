import random
from time import sleep
from unicodedata import normalize
import forca


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


def remove_acentos(palavra_sorteada):
    return normalize('NFKD', palavra_sorteada).encode('ASCII', 'ignore').decode('ASCII')


def checar_letra(chute):
    while not chute.isalpha() or len(chute) > 1:
        print('\033[0;30;41mChute inválido! Tente novamente!\033[m')
        sleep(1)
        chute = str(input('\nEscolha uma letra: ')).upper()


def verifica_chute_sorteada(chute, letras_usadas, sorteada, letters_hit, erros):
    pass


def venceu_perdeu(sorteada, letters_hit, erros):
    sao_iguais = ''
    for letter in letters_hit:
        sao_iguais += letter
        if sao_iguais == sorteada:
            print('\033[1;30;32mVocê venceu! :)\nParabéns!\033[m')
            print(f'\033[1;30;32mPalavra sorteada: {sorteada}\033[m')
            jogar_novamente()
        if erros == 6:
            print(f'\033[0;30;33mNão foi dessa vez :(, tente novamente!\nA palavra sorteada foi: {sorteada}\033[m')
            jogar_novamente()


def jogar_novamente():
    decisao = str(input('1 - Jogar Novamente!\n'
                        '2 - Desistir!\n = '))
    while decisao:
        if decisao == 1 or decisao == '1':
            forca.game()
        else:
            exit()
