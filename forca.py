import models.words as mw
import models.mount_body as mmb
import tkinter
import os
import utils.helper as uh

# janela = tkinter.Tk()


def main() -> None:
    game()


def game() -> None:

    print('Bem vindo!\n'
          'Esse é o jogo da forca, você consegue acertar a palavra?')
    erros = 0
    sorteada = mw.remove_acentos(mw.gerar_palvra())
    letras_usadas = []
    letters_hit = ['_' for letra in sorteada]
    while erros <= 6:
        # os.system('clear')
        for a in letters_hit:
            print(a, end=' ')
        print(f'\nVocê tem: {erros} erro(s)')
        print(f"\nLetras usadas:")
        for b in letras_usadas:
            print(b, end=' ')
        chute = str(input('\nEscolha uma letra: ')).upper()
        mw.checar_letra(chute)
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
                print(f'\033[1;30;31mNão tem essa letra :( {chute}\033[m')
                erros += 1
        else:
            print('\033[1;30;31mLetra já usada, escolha outra\033[m')
        print(f"\n\n/----------"
              f"\n|         |"
              f"\n|      {mmb.mount_body(erros)}"
              f"\n|         "
              f"\n|       "
              f"\n|         ")
        print("#################")
        mw.venceu_perdeu(sorteada, letters_hit, erros)


if __name__ == '__main__':
    main()

# botao = tkinter.Button(janela, text='Enviar', command=main)
# botao.pack(padx=10, pady=10)
# janela.mainloop()
