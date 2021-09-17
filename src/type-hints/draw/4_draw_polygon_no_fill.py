from typing import List
import pygame, sys
from pygame.locals import *

pygame.init()

WIDTH : int = 800
HEIGHT : int = 600
screen : pygame.Surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Draw polygon no fill')

polygon_points : List = [(50, 50), (250, 50), (150, 150)]
polygon_color : List = (255, 255, 255)
line_wdith : int = 1


def main() -> None:
	run : bool = True
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		pygame.draw.polygon(screen, polygon_color, polygon_points, line_wdith)
		pygame.display.update()
	sys.exit()


if __name__ == '__main__':
	main()
