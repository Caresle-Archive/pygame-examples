import pygame, sys
from pygame.locals import *

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Draw a circle with no fill')

circle_color = (255, 255, 255)
circle_radius = 32
circle_center = (WIDTH // 2, HEIGHT // 2)
line_width = 1


def main():
	run = True
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		pygame.draw.circle(screen, circle_color, circle_center, circle_radius, line_width)
		pygame.display.update()
	sys.exit()


if __name__ == '__main__':
	main()
