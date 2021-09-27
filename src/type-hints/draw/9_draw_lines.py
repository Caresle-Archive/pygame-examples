from typing import List
import pygame, sys
from pygame.locals import *

pygame.init()

WIDTH : int = 800
HEIGHT : int = 600
screen : pygame.Surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Draw multiple lines')

color_line_1 : pygame.Color = pygame.Color(255, 255, 255)
line_points_1 : List = [(50, 50), (50, 270), (200, 270)]
color_line_2 : pygame.Color = pygame.Color(0, 148, 198)
line_points_2 : List = [(400, 200), (750, 200), (750, 350)]


def main() -> None:
	run : bool = True
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		pygame.draw.lines(screen, color_line_1, False, line_points_1)
		pygame.draw.lines(screen, color_line_2, True, line_points_2)
		pygame.display.update()
	sys.exit()


if __name__ == '__main__':
	main()