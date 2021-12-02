import pygame
pygame.init()
x = 400
y = 300
velocidade = 5

janela = pygame.display.set_mode((800,600))
pygame.display.set_caption('Estudando PYGAME')

janela_aberta = True
while janela_aberta:
    pygame.time.delay(50)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    pygame.draw.circle(janela,(0,255,0),(400,300),50)
    pygame.display.update()

pygame.quit()
