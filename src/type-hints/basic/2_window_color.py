from typing import List
import pygame, sys
from pygame.locals import *

pygame.init()

WIDTH : int = 800
HEIGHT : int = 600
# Color for fill the screen
BACKGROUND_COLOR : List = (221, 255, 217)

screen : pygame.Surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Window with color')


def main() -> None:
	run : bool = True
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		# Fill the screen with the color we define up
		screen.fill(BACKGROUND_COLOR)
		# Update the current display, if not will stay in black
		pygame.display.update()
	sys.exit()


if __name__ == '__main__':
	print('You should see a screen with a color different to black')
	main()