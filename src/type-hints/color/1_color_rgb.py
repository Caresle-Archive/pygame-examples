import pygame, sys
from pygame.locals import *

pygame.init()

WIDTH : int = 800
HEIGHT : int = 600
screen : pygame.Surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Example of color rgb')

backgorund_color : pygame.Color = pygame.Color(38, 109, 211)


def main() -> None:
	run : bool = True
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		screen.fill(backgorund_color)
		pygame.display.update()
	sys.exit()


if __name__ == '__main__':
	main()