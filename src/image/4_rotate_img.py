"""
Example of how to rotate an image
"""

import pygame, sys
from pygame.locals import *
pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rotate image")

original_image = pygame.image.load("src/assets/cube.png").convert_alpha()
rotate_angle = 0

def main():
	run = True
	global rotate_angle
	# Remember to rotate the original image and not the rotate one
	# Because could make some pixels looks weird
	image = pygame.transform.rotate(original_image, rotate_angle)
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					rotate_angle += 15
					image = pygame.transform.rotate(original_image, rotate_angle)
				if event.key == pygame.K_LEFT:
					rotate_angle -= 15
					image = pygame.transform.rotate(original_image, rotate_angle)
		screen.fill((0, 0, 0))
		screen.blit(image, (120, 120))
		pygame.display.update()


if __name__ == '__main__':
	main()