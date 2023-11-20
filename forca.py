import models.words as mw
import models.mount_body as mmb
import os
import utils.helper as uh

erros = 0
sorteada = mw.gerar_palvra()
letras_usadas = []
letters_hit = ['_' for letra in sorteada]
while erros < 6:
    # os.system('clear')
    for a in letters_hit:
        print(a, end=' ')
    print(f'\nVocê tem: {erros} erro(s)')
    print(f"\nLetras usadas:")
    for b in letras_usadas:
        print(b, end=' ')
    chute = str(input('\nEscolha uma letra: ')).upper()
    if chute not in letras_usadas:
        letras_usadas.append(chute)
        if chute in sorteada:
            index = -1
            for letra in sorteada:
                index += 1
                if chute == letra:
                    letters_hit[index] = chute
                    erros = erros
        else:
            print(f'Não tem essa letra :( {chute}')
            erros += 1
    else:
        print('Letra já usada, escolha outra')
    print(f"\n\n/----------"
          f"\n|         |"
          f"\n|      {mmb.mount_body(erros)}"
          f"\n|         "
          f"\n|       "
          f"\n|         ")

    print("#################")

