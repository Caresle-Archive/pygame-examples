from typing import List
import pygame, sys
from pygame.locals import *

pygame.init()

WIDTH : int = 800
HEIGHT : int = 600
screen : pygame.Surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Draw a rect without fill')

rect_to_draw : pygame.Rect = pygame.Rect((WIDTH // 2) - 32, (HEIGHT // 2) - 32, 64, 64)
# line width to rect rectangle
line_width : int = 1
color_rect : List = (255, 255, 255)

def main() -> None:
	run : bool = True
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		pygame.draw.rect(screen, color_rect, rect_to_draw, line_width)
		pygame.display.update()
	sys.exit()


if __name__ == '__main__':
	main()
