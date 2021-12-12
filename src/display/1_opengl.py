"""
Use opengl in the pygame.display.set_mode
"""
import pygame, sys
from pygame.locals import *
pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.OPENGL)
pygame.display.set_caption("Use opengl in the display set_mode")


def main():
	run = True
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				pygame.quit()
				sys.exit()
			screen.fill((0, 0, 0))


if __name__ == '__main__':
	main()