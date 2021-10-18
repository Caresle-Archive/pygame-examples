import pygame, sys, os
from pygame.locals import *

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Load jpg image')

img_abspath = os.path.abspath('src/assets/image.jpg')
img_path = os.path.join(os.getcwd(), img_abspath)
img = pygame.image.load(img_path).convert()


def main():
	run = True
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		screen.blit(img, (200, 200))
		pygame.display.update()
	sys.exit()


if __name__ == '__main__':
	main()