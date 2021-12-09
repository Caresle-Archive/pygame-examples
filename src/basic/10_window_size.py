"""
Differents windows sizes
Use the left & right arrow key to change between
resolutions
"""
import pygame, sys
from pygame.locals import *
pygame.init()

# Default width and height
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Window size")

# The resolutions which will have to choose
resolutions = [
	(160, 90),
	(320, 180),
	(640, 360),
	(800, 600),
	(1280, 720),
	(1920, 1080),
]

def main():
	run = True
	ind = 0
	global screen
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					ind += 1
					if ind < len(resolutions) - 1:
						# Change resolution
						screen = pygame.display.set_mode(resolutions[ind])
					else:
						ind = 0
				if event.key == pygame.K_LEFT:
					if ind == 0:
						ind = len(resolutions) - 1
					else:
						ind -= 1
					# Change resolution
					screen = pygame.display.set_mode(resolutions[ind])
		screen.fill((130, 130, 255))
		pygame.display.update()


if __name__ == '__main__':
	main()