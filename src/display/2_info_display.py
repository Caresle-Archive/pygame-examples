"""
Get information about the display
"""
import pygame, sys
from pygame.locals import *
pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Info display")

def main():
	run = True
	info = pygame.display.Info()
	print(info)
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				pygame.quit()
				sys.exit()

		screen.fill((0, 0, 0))

		pygame.display.update()

if __name__ == '__main__':
	main()