import pygame
from random import randrange

# Definição de cores
branco = (255,255,255)
preto = (0,0,0)
vermelho = (255,0,0)
verde = (0,255,0)
azul = (0,0,255)

try:
	pygame.init()
except:
	print("O modulo pygame não foi bem inicializado !")

# Definição do tamanho da tela
pygame.mixer.music.load('song.mp3')
largura = 320 
altura = 280
tamanho = 10
relogio = pygame.time.Clock() 
placar = 40

# Gera uma tela inicial
fundo = pygame.display.set_mode((largura, altura))

# Muda o titulo do jogo
pygame.display.set_caption("Snake")

# Definição de texto
def Texto(msg, cor, tam, x, y):
	font = pygame.font.SysFont(None, tam)
	texto1 = font.render(msg, True, cor)
	fundo.blit(texto1, [x, y])
def Cobra(CobraXY):
	for XY in CobraXY:
		pygame.draw.rect(fundo, verde, [XY[0],XY[1],tamanho,tamanho])

def Apple(pos_X, pos_Y):
	pygame.draw.rect(fundo, vermelho, [pos_X,pos_Y,tamanho,tamanho])	

def Jogo():
	Sair = True
	fimdejogo = False
	# Mecânicas da cobrinha
	pos_X = randrange(0,largura-tamanho,10)
	pos_Y = randrange(0,altura-tamanho-placar,10)
	Apple_X = randrange(0,largura-tamanho,10)
	Apple_Y = randrange(0,altura-tamanho-placar,10)
	velocidade_X= 0
	velocidade_Y= 0
	CobraXY = []
	CobraComp = 1
	ponto = 0
	pygame.mixer.music.play()
	pygame.event.wait()
	# Loop de eventos para o jogo funcionar e if para fechar o jogo
	while Sair:
		while fimdejogo:
			
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					Sair = False
					fimdejogo = False
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_c:
						Sair = True
						fimdejogo = False
						pos_X = randrange(0,largura-tamanho,10)
						pos_Y = randrange(0,altura-tamanho-placar,10)
						Apple_X = randrange(0,largura-tamanho,10)
						Apple_Y = randrange(0,altura-tamanho-placar,10)
						velocidade_X= 0
						velocidade_Y= 0
						CobraXY = []
						CobraComp = 1
						ponto = 0
						pygame.mixer.music.play()
					if event.key == pygame.K_s:
						Sair = False
						fimdejogo = False

				if event.type == pygame.MOUSEBUTTONDOWN:
					X = pygame.mouse.get_pos()[0]
					Y = pygame.mouse.get_pos()[1]

					if X > 45 and Y > 120 and X < 180 and Y < 147:
						Sair = True
						fimdejogo = False
						pos_X = randrange(0,largura-tamanho,10)
						pos_Y = randrange(0,altura-tamanho-placar,10)
						Apple_X = randrange(0,largura-tamanho,10)
						Apple_Y = randrange(0,altura-tamanho-placar,10)
						velocidade_X= 0
						velocidade_Y= 0
						CobraXY = []
						CobraComp = 1
						ponto = 0
						pygame.mixer.music.play()
						
					elif X > 190 and Y > 120 and X < 265 and Y < 147:
						Sair = False
						fimdejogo = False



			fundo.fill(branco)
			Texto("Game Over", vermelho, 50, 65, 30)
			Texto("Pontuação Final:"+str(ponto), preto, 30, 70, 80)
			pygame.draw.rect(fundo, preto, [45, 120, 135, 27])
			Texto("Continuar ", branco, 30, 50, 125)
			pygame.draw.rect(fundo, preto, [190, 120, 75, 27])
			Texto("Sair ", branco, 30, 195, 125)
			pygame.display.update()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				Sair = False

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT and velocidade_X != tamanho:
					velocidade_Y =0
					velocidade_X =-tamanho
				if event.key == pygame.K_RIGHT and velocidade_X != -tamanho:
					velocidade_Y=0
					velocidade_X=tamanho
				if event.key == pygame.K_UP and velocidade_Y != tamanho:
					velocidade_Y=-tamanho
					velocidade_X=0
				if event.key == pygame.K_DOWN and velocidade_Y != -tamanho:
					velocidade_Y=tamanho
					velocidade_X=0
				if event.key == pygame.K_SPACE:
					CobraComp += 1

		if Sair:
			pass
			fundo.fill(branco)
			pos_X += velocidade_X
			pos_Y += velocidade_Y

			# Mecânica de comer a maçã
			if pos_X == Apple_X and pos_Y == Apple_Y:
				Apple_X = randrange(0,largura-tamanho,10)
				Apple_Y = randrange(0,altura-tamanho-placar,10)
				CobraComp += 1
				ponto += 1

			# Mecanica de reaparecer do outro lado
			if pos_X + tamanho > largura:
				pos_X = 0
			if pos_X < 0:
				pos_X = largura-tamanho
			if pos_Y + tamanho > altura-placar:
				pos_Y = 0
			if pos_Y < 0:
				pos_Y = altura-tamanho-placar


			
			# Mecânica da cobra crescer
			CobraInicio = []
			CobraInicio.append(pos_X)
			CobraInicio.append(pos_Y)
			CobraXY.append(CobraInicio)
			
			if len(CobraXY) > CobraComp:
				del CobraXY[0]

			# Mecânica de colisão
			if any (Bloco == CobraInicio for Bloco in CobraXY[:-1]):
				pygame.mixer.music.stop()
				fimdejogo = True


			pygame.draw.rect(fundo, preto, [0, altura-placar, largura, placar])	
			Texto("Pontos: "+str(ponto), branco, 25, 10, altura-30)
			Cobra(CobraXY)
			Apple(Apple_X, Apple_Y)
			relogio.tick(10)
			pygame.display.update()
		

		



Jogo()
pygame.quit()
quit()
