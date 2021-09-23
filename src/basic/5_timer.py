import pygame, sys
from pygame.locals import *

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Timer')

# We create the clock
clock = pygame.time.Clock()
# We set the fps (frame per second) that our game will run
FPS = 60


def main():
	run = True
	while run:
		# This set the FPS to FPS var
		# If the pc doesn't have enough power the game can have bugs
		# with the speed in the player, etc.
		clock.tick(FPS)
		print(clock.get_fps())
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
	sys.exit()


if __name__ == '__main__':
	main()
