import pygame, sys
from pygame.locals import *
pygame.init()

SIZE = WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Game menu")

font = pygame.font.Font("src/assets/KenneyPixelSquare.ttf", 16)

# Variable for manage scenes
current_scene = "MenuOne"

def menu_one():
	run = True
	global current_scene
	text_one = font.render("Press space to change to text 2", False, (255, 255, 255))
	pos_x = (WIDTH // 2) - (text_one.get_width() // 2)
	pos_y = (HEIGHT // 2) - (text_one.get_height() // 2)

	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					print('change to menu two')
					current_scene = "MenuTwo"
					run = False
		screen.fill((45, 45, 45))
		screen.blit(text_one, (pos_x, pos_y))
		pygame.display.update()


def menu_two():
	run = True
	global current_scene
	text_two = font.render("Press space to change to text 1", False, (0, 0, 0))
	pos_x = (WIDTH // 2) - (text_two.get_width() // 2)
	pos_y = (HEIGHT // 2) - (text_two.get_height() // 2)

	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					print('change to menu one')
					current_scene = "MenuOne"
					run = False
		screen.fill((145, 145, 145))
		screen.blit(text_two, (pos_x, pos_y))
		pygame.display.update()


def main():
	run = True

	while run:
		if current_scene == "MenuOne":
			menu_one()
		elif current_scene == "MenuTwo":
			menu_two()
		else:
			run = False
			pygame.quit()
			sys.exit()



if __name__ == '__main__':
	main()