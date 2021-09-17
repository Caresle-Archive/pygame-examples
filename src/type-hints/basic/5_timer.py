import pygame, sys
from pygame.locals import *

pygame.init()

WIDTH : int = 800
HEIGHT : int = 600
screen : pygame.Surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Timer')

clock : pygame.time.Clock = pygame.time.Clock()
FPS : int = 60


def main() -> None:
	run : bool = True
	while run:
		clock.tick(FPS)
		print(clock.get_fps())
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
	sys.exit()


if __name__ == '__main__':
	main()
