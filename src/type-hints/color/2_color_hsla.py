import pygame, sys
from pygame.locals import *
pygame.init()

WIDTH : int = 800
HEIGHT : int = 600
screen : pygame.Surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Color with hsl values')

background_color : pygame.Color = pygame.Color(0)
background_color.hsla = (215, 69, 49, 100)


def main():
	run : bool = True
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		screen.fill(background_color)
		pygame.display.update()
	sys.exit()


if __name__ == '__main__':
	main()