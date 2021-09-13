import pygame, sys
from pygame.locals import *

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Draw a rect')

rect_to_draw = pygame.Rect((WIDTH // 2) - 32, (HEIGHT // 2) - 32, 64, 64)
color = (255, 255, 255)

def main():
	run = True
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		pygame.draw.rect(screen, color, rect_to_draw)
		pygame.display.update()
	sys.exit()


if __name__ == '__main__':
	main()