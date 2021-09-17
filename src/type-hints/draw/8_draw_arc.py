from typing import List
import pygame, sys, math
from pygame.locals import *

pygame.init()

WIDTH : int = 800
HEIGHT : int = 600
screen : pygame.Surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Draw arc')

arc_color : List = (255, 255, 255)
arc_rect : pygame.Rect = pygame.Rect((WIDTH // 2) - 64, (HEIGHT // 2) - 64, 128, 128)
arc_line_width : int = 2
# angle in radians
start_angle : float = 0
stop_angle : float = math.radians(180)

def main() -> None:
	run : bool = True
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		pygame.draw.arc(screen, arc_color, arc_rect, start_angle, stop_angle, arc_line_width)
		pygame.display.update()
	sys.exit()


if __name__ == '__main__':
	main()
