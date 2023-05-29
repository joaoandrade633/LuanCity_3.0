# Nova dinâmica do jogo, agora os obstáculos são criados aleatoriamente.

import pygame
from sys import exit
from random import randint #módulo para gerar números aleatórios dentro de um intervalo.

#Função para contar a pontuação na tela.
def mostra_pontuacao():
    contagem_tempo = int(pygame.time.get_ticks() / 1000) - tempo_inicial #pega os milliseconds e subtrai do tempo inicial quando reiniciar o jogo (precisa dividir por mil para ficar em segundos)
    texto_pontuacao_tela = fonte.render(f'Pontuação: {contagem_tempo}', False, (64,64,64)) #variavel para definir a pontuação
    texto_pontuacao_retangulo = texto_pontuacao_tela.get_rect(center = (500, 50)) #cria a pontuação
    janela.blit(texto_pontuacao_tela, texto_pontuacao_retangulo) #desenha a pontuação na janela
    return contagem_tempo #retorna a pontuação

#Função para movimentar os obstaculos aleatórios.
def obstaculo_movimentacao(obstaculo_retangulo_lista):
    if obstaculo_retangulo_lista: 
        for obstaculo_retangulo in obstaculo_retangulo_lista:
            obstaculo_retangulo.x -= 9 #Velocidade dos obstáculos
            janela.blit(obstaculo_imagem, obstaculo_retangulo)
        
        #Exclui os obstáculos que estão fora da janela em -100
        obstaculo_retangulo_lista = [
            obstaculos for obstaculos in obstaculo_retangulo_lista
            if obstaculos.x > -100
            ]

        return obstaculo_retangulo_lista #retorna a lista de obstáculos
    else:
        return [] #retorna a lista vazia se não criou a lista ainda.



pygame.init() #iniciar o pygame

janela = pygame.display.set_mode([1000,500]) #cria a janela no pygame
pygame.display.set_caption("Festa do Cavalo") #altera o nome da janela
frames = pygame.time.Clock() #variavel para definir o frames
fonte = pygame.font.Font(None, 35) #variavel para definir a fonte (não coloquei nenhuma)
jogo_ativo = False #Começa o jogo ou tela de gameover
tempo_inicial = 0 #zera a pontuação ao reiniciar o jogo
pontuacao = 0

#Imagens do Jogo
ceu_imagem = pygame.image.load('assets/ceu.png').convert() #carrega a imagem do céu.
chao_imagem = pygame.image.load('assets/chao.png').convert_alpha() #carrega a imagem do chão

#Tela Inicial
tela_inicial_imagem = pygame.image.load('assets/tela_inicial.png').convert() #carrega a imagem da tela inicial.

#Imagens do Obstáculo
obstaculo_imagem = pygame.image.load('assets/obstaculo.png').convert_alpha() #carrega a imagem do chão
obstaculo_retangulo = obstaculo_imagem.get_rect(bottomright = (1000, 409)) #cria retangulo e centraliza no bottomright

obstaculo_retangulo_lista = [] #lista vazia para colocar os obstáculos gerados aleatórios.

#Imagem do Cavalo
player_cavalo = pygame.image.load('assets/cavalo/cavalo_1.png').convert_alpha() #carrega a imagem do cavalo
player_cavalo_retangulo = player_cavalo.get_rect(bottomleft = (10, 412)) #cria um retangulo em volta da imagem do cavalo
player_gravidade = 0

#Evento Personalizado criar um Contador (Timer) que gera Obstáculos Aleatórios a cada X segundos
obstaculo_cronometro = pygame.USEREVENT + 1
pygame.time.set_timer(obstaculo_cronometro, 1500)



while True: #while para atualizar atualizar o janela e não fechar.
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #pega o evento QUIT do event.
            pygame.quit() #fecha a janela
            exit() #fecha o python
        
        # Lista de teclas: https://www.pygame.org/docs/ref/key.html
        # Verifica se foi pressionado a tecla e faz o personagem pular com o aumento da posição em Y (gravidade)
        
        if jogo_ativo:
            if event.type == pygame.KEYDOWN: #Botão espaço para pular
                if event.key == pygame.K_SPACE and player_cavalo_retangulo.bottom >= 412: #verifica o espaço e se o cavalo está na posição original
                    player_gravidade = -20 #Gravidade do pulo -20
        else: #tela de game over
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                jogo_ativo = True
                obstaculo_retangulo.left = 1000
                tempo_inicial = int(pygame.time.get_ticks() / 1000)
        
        if event.type == obstaculo_cronometro and jogo_ativo:
            obstaculo_retangulo_lista.append(obstaculo_imagem.get_rect(bottomright = (randint(1000, 1400), 409))) #lista dos obstáculos

    if jogo_ativo:
        janela.blit(ceu_imagem, (0,0)) #desenha o fundo
        janela.blit(chao_imagem, (0,402)) #desenha o chao
        # janela.blit(texto_pontuacao, texto_pontuacao_retangulo) #desenha a fonte no centro
        pontuacao = mostra_pontuacao()

        # Obstáculo
        # obstaculo_retangulo.x -= 9 #movimenta o obstaculo
        # if obstaculo_retangulo.right <= 0:  #verificar e volta o obstaculo no começo da tela.
        #     obstaculo_retangulo.left = 1000
        # janela.blit(obstaculo_imagem, obstaculo_retangulo) #desenha o obstaculo

        # Player
        player_gravidade += 1 #adiciona mais 1 na gravidade
        player_cavalo_retangulo.y += player_gravidade  #verificar e corrige a gravidade no nível do terreno
        if player_cavalo_retangulo.bottom >= 412:
            player_cavalo_retangulo.bottom = 412
        janela.blit(player_cavalo, player_cavalo_retangulo) #desenha o cavalo e o retangulo em volta.

        # Obstáculo movimentação
        obstaculo_retangulo_lista = obstaculo_movimentacao(obstaculo_retangulo_lista)


        # Colisão Player e Obstáculo
        if obstaculo_retangulo.colliderect(player_cavalo_retangulo):
            jogo_ativo = False
    else:
        janela.blit(tela_inicial_imagem,(0,0)) #desenha a imagem da tela inicial
        pontuacao_texto = fonte.render(f'Sua Pontuação: {pontuacao}', False, (64,64,64)) #variavel para definir a pontuação na tela inicial
        pontuacao_texto_retangulo = pontuacao_texto.get_rect(midbottom = (500, 485)) #define o texto da pontuação

        if pontuacao != 0:
            janela.blit(pontuacao_texto, pontuacao_texto_retangulo) #desenha o texto da pontuação na tela inicial se for diferente de zero.

    pygame.display.update() #atualiza a janela a cada while.
    frames.tick(60) #define os frames por segundos.