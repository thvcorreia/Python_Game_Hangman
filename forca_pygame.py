import pygame
import sys
import models.words as mw

# Inicializar o Pygame
pygame.init()

# Definir cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Definir a janela do jogo
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Jogo da Forca")
clock = pygame.time.Clock()

# Carregar imagens da forca
hangman_images = [pygame.image.load(f'media\hangman{i}.gif') for i in range(7)]

# Definir variáveis do jogo
word = mw.remove_acentos(mw.gerar_palvra())  # Palavra a ser adivinhada
guessed = ['_' for _ in word]  # Lista para controlar letras adivinhadas
used_letters = set()  # Conjunto para letras já usadas
wrong_attempts = 0  # Contador de tentativas erradas

# Definir fonte
font = pygame.font.Font(None, 36)

# Função para desenhar texto na tela


def draw_text(text, color, x, y):

    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))


# Loop principal do jogo

running = True

while running:
    screen.fill(WHITE)

    # Desenhar palavra a ser adivinhada
    draw_text(' '.join(guessed), BLACK, 280, 400)
    draw_text(word, GREEN, 280, 370)
    # Desenhar letras já usadas
    draw_text('Letras usadas: ' + ' '.join(used_letters), BLACK, 280, 450)

    # Desenhar imagem da forca
    screen.blit(hangman_images[wrong_attempts], (100, 50))

    # Verificar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if pygame.K_a <= event.key <= pygame.K_z:
                letter = chr(event.key).upper()  # Converter tecla pressionada em letra
                if letter not in used_letters:
                    used_letters.add(letter)
                    if letter in word:
                        for i, char in enumerate(word):
                            if char == letter:
                                guessed[i] = letter
                    else:
                        wrong_attempts += 1

    # Verificar se o jogador ganhou ou perdeu
    if '_' not in guessed:
        draw_text('Você ganhou!', GREEN, 300, 200)
        draw_text(f'Teste', GREEN, 400, 300)
    elif wrong_attempts == 6:
        draw_text('Você perdeu!', RED, 300, 200)
        draw_text('Deseja jogar novamente', RED, 300, 230)
        draw_text('1 - Sim', RED, 300, 260)
        draw_text('2 - Não', RED, 300, 290)
        draw_text('= ' + ' '.join('Variavel aqui'), BLACK, 300, 320)
        pygame.BU
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_1:
                    opcao = event.key
                    pygame.init()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
