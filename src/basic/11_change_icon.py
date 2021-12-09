import pygame, sys
from pygame.locals import *
pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Change icon")

# Laod the icon from the assets folder
icon = pygame.image.load("src/assets/icon.png").convert_alpha()

# set the icon
pygame.display.set_icon(icon)


def main():
	run = True
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				pygame.quit()
				sys.exit()
		pygame.display.update()


	
if __name__ == '__main__':
	main()