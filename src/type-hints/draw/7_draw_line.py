from typing import List
import pygame, sys
from pygame.locals import *

pygame.init()

WIDTH : int = 800
HEIGHT : int = 600
screen : pygame.Surface= pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Draw line')

line_color : List = (255, 255, 255)
line_width : int = 1

line_start_pos : List = (0, 0)
line_end_post : List = (WIDTH // 2, HEIGHT // 2)


def main() -> None:
	run : bool = True
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		pygame.draw.line(screen, line_color, line_start_pos, line_end_post, line_width)
		pygame.display.update()
	sys.exit()


if __name__ == '__main__':
	main()
