import pygame
pygame.init()

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class Building():
	def __init__(self, color, height, width, x_point, y_point):
		self.color   = color
		self.height  = height
		self.width   = width
		self.x_point = x_point
		self.y_point = y_point
	
	def draw_building(self):
		pygame.draw.rect(screen, self.color, [self.x_point, self.y_point, self.width, self.height])
	
	def move_building(self):
		self.x_point -= 3

	
	

