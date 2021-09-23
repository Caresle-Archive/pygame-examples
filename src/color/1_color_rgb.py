import pygame, sys
from pygame.locals import *

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Example of color rgb')

backgorund_color = pygame.Color(38, 109, 211)


def main():
	run = True
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		screen.fill(backgorund_color)
		pygame.display.update()
	sys.exit()


if __name__ == '__main__':
	main()