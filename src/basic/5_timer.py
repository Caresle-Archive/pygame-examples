import pygame, sys
from pygame.locals import *

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Timer')

clock = pygame.time.Clock()
FPS = 60


def main():
	run = True
	while run:
		clock.tick(FPS)
		print(clock.get_fps())
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
	sys.exit()


if __name__ == '__main__':
	main()
