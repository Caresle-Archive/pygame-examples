# We import pygame lib
import pygame, sys
from pygame.locals import *

pygame.init()

# Screen dimension
WIDTH, HEIGHT = 800, 600
# We create our screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# Set the title of our screen
pygame.display.set_caption('Basic window')


def main():
	run = True
	# Main loop
	while run:
		# We check when the game will be closed
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
	sys.exit()


if __name__ == '__main__':
	print(f'You should see a black screen of {WIDTH}x{HEIGHT}')
	main()
