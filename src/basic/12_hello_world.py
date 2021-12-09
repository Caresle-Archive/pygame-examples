import pygame, sys
from pygame.locals import *
pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hello world")

font = pygame.font.Font("src/assets/KenneyPixelSquare.ttf", 16)

def main():
	run = True
	hello_world_text = font.render("Hello world!", False, (255, 255, 255))
	# for center the text in the x and y axis
	text_pos_x = (WIDTH // 2) - (hello_world_text.get_width() // 2)
	text_pos_y = (HEIGHT // 2) - (hello_world_text.get_height() // 2)

	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				pygame.quit()
				sys.exit()
		screen.fill((0, 0, 0))
		screen.blit(hello_world_text, (text_pos_x, text_pos_y))
		pygame.display.update()



if __name__ == '__main__':
	main()