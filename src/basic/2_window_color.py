import pygame, sys
from pygame.locals import *

pygame.init()

WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (221, 255, 217)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Window with color')


def main():
	run = True
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		screen.fill(BACKGROUND_COLOR)
		pygame.display.update()
	sys.exit()


if __name__ == '__main__':
	main()