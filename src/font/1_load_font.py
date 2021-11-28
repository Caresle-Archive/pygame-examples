"""
Load a .ttf and draw a text in the screen
"""

import pygame, sys
from pygame.locals import *
pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Load font")

font = pygame.font.Font("src/assets/KenneyPixelSquare.ttf", 16)

def main():
	run = True
	text = font.render("Text example", False, (255, 255, 255))
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				pygame.quit()
				sys.exit()
		
		screen.fill((0, 0, 0))
		screen.blit(text, (120, 120))
		pygame.display.update()


if __name__ == '__main__':
	main()