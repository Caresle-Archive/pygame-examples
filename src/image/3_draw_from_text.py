import pygame, sys
from pygame.image import load
from pygame.locals import *

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Draw from text")

# Floor
floor_img = pygame.image.load("src/assets/floor.png").convert_alpha()
floor2_img = pygame.image.load("src/assets/floor2.png").convert_alpha()
floor3_img = pygame.image.load("src/assets/floor3.png").convert_alpha()


def load_text(path):
	f = open(path + '.txt', 'r')
	data = f.read()
	f.close()
	data = data.split('\n')
	grid_map = []
	for row in data:
		grid_map.append(list(row))
	return grid_map


def draw_map(path, screen):
	grid_map = load_text(path)
	position = [0, 0]
	for row in grid_map:
		for char in row:
			if char == '0':
				screen.blit(floor_img, position)
			if char == '1':
				screen.blit(floor2_img, position)
			if char == '2':
				screen.blit(floor3_img, position)
			position[0] += 16
			
		position[0] = 0
		position[1] += 16


def main():
	run = True
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
				run = False
		screen.fill((0, 0, 0))
		draw_map('src/image/background', screen)
		pygame.display.update()


if __name__ == '__main__':
	main()