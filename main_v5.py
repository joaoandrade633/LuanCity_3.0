# Implantação da Pontuação

import pygame
from sys import exit

#Função para contar a pontuação na tela.
def mostra_pontuacao():
    contagem_tempo = int(pygame.time.get_ticks() / 1000) - tempo_inicial #pega os milliseconds e subtrai do tempo inicial quando reiniciar o jogo (precisa dividir por mil para ficar em segundos)
    texto_pontuacao_tela = fonte.render(f'Pontuação: {contagem_tempo}', False, (64,64,64)) #variavel para definir a pontuação
    texto_pontuacao_retangulo = texto_pontuacao_tela.get_rect(center = (500, 50)) #cria a pontuação
    janela.blit(texto_pontuacao_tela, texto_pontuacao_retangulo) #desenha a pontuação na janela

pygame.init() #iniciar o pygame

janela = pygame.display.set_mode([1000,500]) #cria a janela no pygame
pygame.display.set_caption("Festa do Cavalo") #altera o nome da janela
frames = pygame.time.Clock() #variavel para definir o frames
fonte = pygame.font.Font(None, 40) #variavel para definir a fonte (não coloquei nenhuma)
jogo_ativo = True
tempo_inicial = 0 #zera a pontuação ao reiniciar o jogo

ceu_imagem = pygame.image.load('assets/ceu.png').convert() #carrega a imagem do céu.
chao_imagem = pygame.image.load('assets/chao.png').convert_alpha() #carrega a imagem do chão

# texto_pontuacao = fonte.render('Pontuação', False, 'Black') #carrega a fonte
# texto_pontuacao_retangulo = texto_pontuacao.get_rect(center = (500, 50))  #cria retangulo e centraliza a fonte

obstaculo_imagem = pygame.image.load('assets/obstaculo.png').convert_alpha() #carrega a imagem do chão
obstaculo_retangulo = obstaculo_imagem.get_rect(bottomright = (900, 430)) #cria retangulo e centraliza no bottomright

player_cavalo = pygame.image.load('assets/cavalo/cavalo_1.png').convert_alpha() #carrega a imagem do cavalo
player_cavalo_retangulo = player_cavalo.get_rect(midbottom = (100, 430)) #cria um retangulo em volta da imagem do cavalo
player_gravidade = 0


while True: #while para atualizar atualizar o janela e não fechar.
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #pega o evento QUIT do event.
            pygame.quit() #fecha a janela
            exit() #fecha o python
        
        # Lista de teclas: https://www.pygame.org/docs/ref/key.html
        # Verifica se foi pressionado a tecla e faz o personagem pular com o aumento da posição em Y (gravidade)
        
        if jogo_ativo:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_cavalo_retangulo.bottom >= 430:
                    player_gravidade = -20
        else: #tela de game over
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                jogo_ativo = True
                obstaculo_retangulo.left = 1000
                tempo_inicial = int(pygame.time.get_ticks() / 1000)


    if jogo_ativo:
        janela.blit(ceu_imagem, (0,0)) #desenha o fundo
        janela.blit(chao_imagem, (0,402)) #desenha o chao
        # janela.blit(texto_pontuacao, texto_pontuacao_retangulo) #desenha a fonte no centro
        mostra_pontuacao()

        # Obstáculo
        obstaculo_retangulo.x -= 9 #movimenta o obstaculo
        if obstaculo_retangulo.right <= 0:  #verificar e volta o obstaculo no começo da tela.
            obstaculo_retangulo.left = 1000
        janela.blit(obstaculo_imagem, obstaculo_retangulo) #desenha o obstaculo

        # Player
        player_gravidade += 1 #adiciona mais 1 na gravidade
        player_cavalo_retangulo.y += player_gravidade  #verificar e corrige a gravidade no nível do terreno
        if player_cavalo_retangulo.bottom >= 430:
            player_cavalo_retangulo.bottom = 430
        janela.blit(player_cavalo, player_cavalo_retangulo) #desenha o cavalo e o retangulo em volta.

        # Colisão Player e Obstáculo
        if obstaculo_retangulo.colliderect(player_cavalo_retangulo):
            jogo_ativo = False
    else:
        janela.fill('Black')

    pygame.display.update() #atualiza a janela a cada while.
    frames.tick(60) #define os frames por segundos.