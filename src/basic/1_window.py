import pygame, sys
from pygame.locals import *

pygame.init()

# Screen dimension
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Basic window')


def main():
	run = True
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
	sys.exit()


if __name__ == '__main__':
	print(f'You should see a black screen of {WIDTH}x{HEIGHT}')
	main()