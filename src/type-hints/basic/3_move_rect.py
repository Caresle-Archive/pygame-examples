# Check the draw/1_draw_rect before this.
# For understand the Rect for move section

from typing import List
import pygame, sys
from pygame.locals import *

pygame.init()

WIDTH : int = 800
HEIGHT : int = 600
screen : pygame.Surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Move rect')

# Rect for move
player_rect : pygame.Rect = pygame.Rect((WIDTH // 2) - 16, (HEIGHT // 2) - 16, 32, 32)
player_color : List = (255, 255, 255)

# Speed to move the player
speed : int = 1


def main() -> None:
	run : bool = True
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		# We get the state of all keyboard buttons
		key : List = pygame.key.get_pressed()
		
		# Check if the left arrow key is pressed
		if key[pygame.K_LEFT]:
			# We subtrac our speed value in the current value in x 
			player_rect.x -= speed
		if key[pygame.K_RIGHT]:
			# We add our speed value in the current value in x
			player_rect.x += speed
		
		# We fill the screen for re draw
		# See file 4 (draw_order) to check this
		screen.fill((0, 0, 0))
		# We draw our rectangle in the screen
		pygame.draw.rect(screen, player_color, player_rect)
		pygame.display.update()
	sys.exit()


if __name__ == '__main__':
	main()
