from typing import List
import pygame, sys
from pygame.locals import *

pygame.init()

WIDTH : int = 800
HEIGHT : int = 600
screen : pygame.Surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Draw a rect')

# We create a pygame.Rect object
# the arguments for pygame.Rect are (left, top, width, height)
# We set the left and top position in the middle of the screen
rect_to_draw : pygame.Rect = pygame.Rect((WIDTH // 2) - 32, (HEIGHT // 2) - 32, 64, 64)
color : List = (255, 255, 255)

def main() -> None:
	run : bool = True
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		# For draw a rect we call the pygame.draw.rect method
		pygame.draw.rect(screen, color, rect_to_draw)
		pygame.display.update()
	sys.exit()


if __name__ == '__main__':
	main()
