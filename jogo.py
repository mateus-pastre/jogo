import pygame
import time
import random
pygame.init()
largura = 800
altura = 600
configTela = (largura, altura)
gameDisplay = pygame.display.set_mode(configTela)
clock = pygame.time.Clock()
black = (0, 0, 0)
white = (255, 255, 255)
pygame.display.set_caption("Peaky Blinders - Mateus")
icone = pygame.image.load("imagens/thomas.shelby.png")
pygame.display.set_icon(icone)
thomas = pygame.image.load("imagens/thomas.shelby.png")
larguraThomas = 100
fundo = pygame.image.load("imagens/fundo.jpg")
boina = pygame.image.load("imagens/cap.png")
som_peaky= pygame.mixer.Sound("imagens/peaky.mpeg")
som_peaky.set_volume(1)
nomeJogador = str(input("Insira o seu nome: "))
emailJogador = str(input("Insira o seu email: "))
arquivo = open("historico.txt", "a")
arquivo.write("Participante: " + nomeJogador + "\n email: " + emailJogador + "\n")
def mostraThomas(x, y):
    gameDisplay.blit(thomas, (x, y))
def mostraBoina(x, y):
    gameDisplay.blit(boina, (x, y))
def text_objects(texto, font):
    textSurface = font.render(texto, True, white)
    return textSurface, textSurface.get_rect()
def escreverTela(texto):
    fonte = pygame.font.Font("freesansbold.ttf", 20)
    TextSurf, TextRect = text_objects(texto, fonte)
    TextRect.center = ((largura/2, altura/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(5)
    game()
def escreverPlacar(contador):
    fonte = pygame.font.SysFont(None, 50)
    texto = fonte.render("Desvios:"+str(contador), True, white)
    gameDisplay.blit(texto, (10,10))
def dead():
    pygame.mixer.Sound.play(som_peaky)
    pygame.mixer.music.stop()
    escreverTela("By the order of the Peaky Blinders, você Morreu!")
def game():
    thomasPosicaoX = largura*0.42
    thomasPosicaoY = altura*0.8
    movimentoX = 0
    velocidade = 20
    boinaAltura = 50
    boinaLargura = 50
    boinaVelocidade = 3
    boinaX = random.randrange(0, largura)
    boinaY = -200
    desvios = 0
 
    while True:
        acoes = pygame.event.get() 
        for acao in acoes:
            if acao.type == pygame.QUIT:
                pygame.quit()
                quit()
            if acao.type == pygame.KEYDOWN:
                if acao.key == pygame.K_LEFT:
                    movimentoX = velocidade*-1
                elif acao.key == pygame.K_RIGHT:
                    movimentoX = velocidade
            if acao.type == pygame.KEYUP:
                movimentoX = 0
        gameDisplay.fill(white)
        gameDisplay.blit(fundo, (0, 0))
        escreverPlacar(desvios)
        boinaY = boinaY + boinaVelocidade
        mostraBoina(boinaX, boinaY)
        if boinaY > altura:
            boinaY = -200
            boinaX = random.randrange(0, largura)
            desvios = desvios+1
            boinaVelocidade += 3         
        thomasPosicaoX += movimentoX
        if thomasPosicaoX < 0:
            thomasPosicaoX = 0
        elif thomasPosicaoX > largura-larguraThomas:
            thomasPosicaoX = largura-larguraThomas
    
        if thomasPosicaoY < boinaY + boinaAltura:
            if thomasPosicaoX < boinaX and thomasPosicaoX+larguraThomas > boinaX or boinaX+boinaLargura > thomasPosicaoX and boinaX+boinaLargura < thomasPosicaoX+larguraThomas:
                dead()
        mostraThomas(thomasPosicaoX, thomasPosicaoY)
        pygame.display.update()
        clock.tick(60)
game()
