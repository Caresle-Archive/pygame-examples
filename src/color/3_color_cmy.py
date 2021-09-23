import pygame, sys
from pygame.locals import *
pygame.init()

WIDHT, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDHT, HEIGHT))
pygame.display.set_caption('Color with cmy values')

background_color = pygame.Color(0)
background_color.cmy = (.85, .57, .17)


def main():
	run = True
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		screen.fill(background_color)
		pygame.display.update()
	sys.exit()


if __name__ == '__main__':
	main()