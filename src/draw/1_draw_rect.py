import pygame, sys
from pygame.locals import *

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Draw a rect')

# We create a pygame.Rect object
# the arguments for pygame.Rect are (left, top, width, height)
# We set the left and top position in the middle of the screen
rect_to_draw = pygame.Rect((WIDTH // 2) - 32, (HEIGHT // 2) - 32, 64, 64)
color = (255, 255, 255)

def main():
	run = True
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		# For draw a rect we call the pygame.draw.rect method
		pygame.draw.rect(screen, color, rect_to_draw)
		pygame.display.update()
	sys.exit()


if __name__ == '__main__':
	main()
