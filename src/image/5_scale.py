"""
Scale an image
"""
import pygame, sys
from pygame.locals import *
pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Scale an image")
original_image = pygame.image.load("src/assets/cube.png").convert_alpha()

def main():
	run = True
	# The scale values doesn't multiply for the original
	# image resolution, the scale values resize the image
	# to the given values.
	# In this case from a 64x64 image to 128x128 image.
	scaled_image = pygame.transform.scale(original_image, (128, 128))
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				pygame.quit()
				sys.exit()
		screen.fill((0, 0, 0))
		screen.blit(original_image, (20, 20))
		screen.blit(scaled_image, (420, 20))
		pygame.display.update()


if __name__ == '__main__':
	main()