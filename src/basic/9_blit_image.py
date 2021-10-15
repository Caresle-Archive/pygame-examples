import pygame, sys, os
from pygame.locals import *

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
img_url = os.path.join(os.getcwd(), os.path.abspath('src/assets/cube.png'))
img = pygame.image.load(img_url).convert_alpha()

def main():
	run = True
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		screen.blit(img, (200, 200))
		pygame.display.update()
	sys.exit()


if __name__ == '__main__':
	main()