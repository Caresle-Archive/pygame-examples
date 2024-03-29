import pygame, sys
from pygame.locals import *

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Move four directions')

player_rect = pygame.Rect((WIDTH // 2) - 32, (HEIGHT // 2) - 32, 64, 64)
player_color = (255, 255, 255)
speed = 1


def main():
	run = True
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		keys = pygame.key.get_pressed()
		if keys[pygame.K_LEFT]:
			player_rect.x -= speed
		if keys[pygame.K_RIGHT]:
			player_rect.x += speed
		if keys[pygame.K_UP]:
			player_rect.y -= speed
		if keys[pygame.K_DOWN]:
			player_rect.y += speed
		screen.fill((0, 0, 0))
		pygame.draw.rect(screen, player_color, player_rect)
		pygame.display.update()
	sys.exit()


if __name__ == '__main__':
	main()
