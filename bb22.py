import pygame
import random
'''
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
size = (800, 600)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
done = False
'''

# --- Class: Building
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
'''
# - Empty list for Building
list_building = []	




# --- Class: Snowflake
class SnowFlake():
	def __init__(self, size, position, wind=False): #initialize it and define attributes: size, position, wind
		self.size = size
		self.position = position
		self.wind = wind 

	def fall(self, speed):
		self.position[1] += speed #this moves the snowflake in some positive y direction
		if self.wind:
			self.position[0] += random.randint(-speed, speed) 
        
	def draw(self):
		pygame.draw.circle(screen, WHITE, self.position, 5)         

# - Empty list + Speed for Snow
speed = 1000
snow_list = []




# --- While loop
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	
	# - Background color
	screen.fill(BLUE)

	# - Building(color, height, width, x_point, y_point)
	my_building = Building(BLACK, random.randint(100,800), random.randint(25, 50), 800, random.randint(100, 600))
	list_building.append(my_building)
	
	# - For loop for Building
	for building in list_building:
		building.draw_building()
		building.move_building()
	
	# - Snowflake(size, position, wind=False)
	snowflake = SnowFlake(5, [random.randint(0, 750), 0], wind = True)
	snow_list.append(snowflake)
    
    # - For loop for Snowflake
	for snowflake in snow_list:
		snowflake.draw()
		snowflake.fall(1)
	
	
	
	
	
	pygame.display.flip()
# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
'''