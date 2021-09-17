from typing import List
import pygame, sys
from pygame.locals import *

pygame.init()

WIDTH : int = 800
HEIGHT : int = 600
screen : pygame.Surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Draw order')

rect_1 : pygame.Rect = pygame.Rect(64, 64, 64, 64)
white_color : List = (255, 255, 255)

rect_2 : pygame.Rect= pygame.Rect(96, 64, 64, 64)
purple_color : List = (179, 103, 155)

# If it's true calls the draw_order_2
draw_1 : bool = False

def draw_order_1() -> None:
	pygame.draw.rect(screen, white_color, rect_1)
	pygame.draw.rect(screen, purple_color, rect_2)


def draw_order_2() -> None:
	pygame.draw.rect(screen, purple_color, rect_2)
	pygame.draw.rect(screen, white_color, rect_1)


def main() -> None:
	run : bool = True
	global draw_1
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					draw_1 = not draw_1
		screen.fill((0, 0, 0))
		if draw_1:
			draw_order_1()
		else:
			draw_order_2()
		pygame.display.update()
	sys.exit()


if __name__ == '__main__':
	print('You should see two squares overlapping')
	print('Press Space for change the order of draw')
	main()
