import pygame, sys
from pygame.locals import *

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Mouse click')

click_color = (255, 255, 255)
click_rect = pygame.Rect(0, 0, 32, 32)


def main():
	run = True
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		mouse = pygame.mouse.get_pressed()
		
		if mouse[0]:
			pos = pygame.mouse.get_pos()
			click_rect.x = pos[0] - (click_rect.width // 2)
			click_rect.y = pos[1] - (click_rect.height // 2)
			screen.fill((0, 0, 0))
			pygame.draw.rect(screen, click_color, click_rect)
		
		pygame.display.update()
	sys.exit()


if __name__ == '__main__':
	print('Click the left mouse button for draw a rectangle')
	main()
