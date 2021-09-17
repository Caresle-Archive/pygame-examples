from typing import List
import pygame, sys
from pygame.locals import *

pygame.init()

WIDTH : int = 800
HEIGHT : int = 600
screen : pygame.Surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Draw circle')

circle_color : List = (255, 255, 255)
circle_radius : int = 32
circle_center : int = (WIDTH // 2, HEIGHT // 2)


def main() -> None:
	run : bool = True
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		pygame.draw.circle(screen, circle_color, circle_center, circle_radius)
		pygame.display.update()
	sys.exit()


if __name__ == '__main__':
	main()
