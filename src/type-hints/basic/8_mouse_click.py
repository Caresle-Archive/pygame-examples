from typing import List
import pygame, sys
from pygame.locals import *

pygame.init()

WIDTH : int = 800
HEIGHT : int = 600
screen : pygame.Surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Mouse click')

click_color : List = (255, 255, 255)
click_rect : pygame.Rect = pygame.Rect(0, 0, 32, 32)


def main() -> None:
	run : bool = True
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		mouse : List = pygame.mouse.get_pressed()
		
		if mouse[0]:
			pos : List = pygame.mouse.get_pos()
			click_rect.x = pos[0] - (click_rect.width // 2)
			click_rect.y = pos[1] - (click_rect.height // 2)
			screen.fill((0, 0, 0))
			pygame.draw.rect(screen, click_color, click_rect)
		
		pygame.display.update()
	sys.exit()


if __name__ == '__main__':
	print('Click the left mouse button for draw a rectangle')
	main()