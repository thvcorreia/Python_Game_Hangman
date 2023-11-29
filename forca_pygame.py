import pygame
import sys

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
word = "PYTHON"  # Palavra a ser adivinhada
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

    # Desenhar letras já usadas
    draw_text('Letras usadas: ' + ' '.join(used_letters), BLACK, 280, 450)

    # Desenhar imagem da forca
    screen.blit(hangman_images[wrong_attempts], (100, 50))

    # Verificar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key >= pygame.K_a and event.key <= pygame.K_z:
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
    elif wrong_attempts == 6:
        draw_text('Você perdeu!', RED, 300, 200)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
