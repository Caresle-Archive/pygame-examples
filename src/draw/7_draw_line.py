import pygame, sys
from pygame.locals import *

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Draw line')

line_color = (255, 255, 255)
line_width = 1

line_start_pos = (0, 0)
line_end_post = (WIDTH // 2, HEIGHT // 2)


def main():
	run = True
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		pygame.draw.line(screen, line_color, line_start_pos, line_end_post, line_width)
		pygame.display.update()
	sys.exit()


if __name__ == '__main__':
	main()