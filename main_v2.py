# Inclusão de imagens, textos e movimentação

import pygame
from sys import exit

pygame.init() #iniciar o pygame

janela = pygame.display.set_mode([1000,500]) #cria a janela no pygame
pygame.display.set_caption("Festa do Cavalo") #altera o nome da janela
frames = pygame.time.Clock() #variavel para definir o frames
fonte = pygame.font.Font(None, 40) #variavel para definir a fonte (não coloquei nenhuma)

ceu_imagem = pygame.image.load('assets/ceu.png').convert() #carrega a imagem do céu.
chao_imagem = pygame.image.load('assets/chao.png').convert_alpha() #carrega a imagem do chão

texto_fonte = fonte.render('Pontuação', False, 'Black')

obstaculo_imagem = pygame.image.load('assets/obstaculo.png').convert_alpha() #carrega a imagem do chão
# obstaculo_x_posicao = 1000 #posicao x do obstaculo
obstaculo_retangulo = obstaculo_imagem.get_rect(bottomright = (900, 430))

player_cavalo = pygame.image.load('assets/cavalo/cavalo_1.png').convert_alpha() #carrega a imagem do cavalo
player_cavalo_retangulo = player_cavalo.get_rect(midbottom = (100, 430)) #cria um retangulo em volta da imagem do cavalo


while True: #while para atualizar atualizar o janela e não fechar.
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #pega o evento QUIT do event.
            pygame.quit() #fecha a janela
            exit() #fecha o python

    janela.blit(ceu_imagem, (0,0)) #desenha o fundo
    janela.blit(chao_imagem, (0,402)) #desenha o chao
    janela.blit(texto_fonte, (420, 30)) #desenha a fonte
    
    obstaculo_retangulo.x -= 4 #movimenta o obstaculo
    if obstaculo_retangulo.right <= 0:
        obstaculo_retangulo.left = 1000

    janela.blit(obstaculo_imagem, obstaculo_retangulo) #desenha o obstaculo
    janela.blit(player_cavalo, player_cavalo_retangulo) #desenha o cavalo e o retangulo em volta.
    
    
    pygame.display.update() #atualiza a janela a cada while.
    frames.tick(60) #define os frames por segundos.