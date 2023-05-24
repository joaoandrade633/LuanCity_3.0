# Início do Jogo

import pygame
from sys import exit

pygame.init() #iniciar o pygame

janela = pygame.display.set_mode([1000,500]) #cria a janela no pygame
pygame.display.set_caption("Festa do Cavalo") #altera o nome da janela

while True: #while para atualizar atualizar o janela e não fechar.
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #pega o evento QUIT do event.
            pygame.quit() #fecha a janela
            exit() #fecha o python

    pygame.display.update() #atualiza a janela a cada while.