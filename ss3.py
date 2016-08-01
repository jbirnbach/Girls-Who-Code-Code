import pygame
import random
from PIL import Image
from blockk import *
from cityscroller import *
pygame.init()

pygame.image.load("sky2.jpeg")
im = pygame.image.load("sky2.jpeg")
screen_width = 700
screen_height = 500
screen = pygame.display.set_mode([screen_width, screen_height])

    
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
DARK_SLATE_BLUE = (72, 61, 139)
PINK = (255, 20, 147)
GRAY = (190, 190, 190)
TEAL = (135, 206, 250)

clock = pygame.time.Clock()
score = 0
lives = 6

city = []
x = 0
sky_pos = 0

## The scroller object is created here
#any_scroller = Scroller(screen_width, 300, screen_height, (255, 100, 100), 2)

## Font to allow for 
font = pygame.font.SysFont("Gill Sans", 25, True, False)

# Blocks for first run of game, stores them in all the lists
make_blocks()

#check that game is not done
done = False

#Start game loop
while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True
                
    # Clear the screen
    screen.fill(WHITE)
    sky = pygame.image.load('sky2.jpeg')
    screen.blit(sky, (sky_pos, 0))


    building = Building(BLACK, random.randint(100,800), random.randint(25, 50), 800, random.randint(100, 600))
    city.append(building)
    for building in city:
        building.draw_building()
        building.move_building()
    
		
    # Get the current mouse position. This returns the position
    # as a list of two numbers.
    pos = pygame.mouse.get_pos()
 
    # Fetch the x and y out of the list,
    # just like we'd fetch letters out of a string.
    # Set the player object to the mouse location
    player.rect.x = pos[0]
    player.rect.y = pos[1]

    # See if the player block has collided with anything.
    pink_blocks_hit_list = pygame.sprite.spritecollide(player, pink_block_list, True)
    green_blocks_hit_list = pygame.sprite.spritecollide(player, green_block_list, True)

    # Move the blocks.
    pink_block_list.update()
    green_block_list.update()

    # Check the list of collisions.
    for block in green_blocks_hit_list:
        score += 1

    for block in pink_blocks_hit_list:
        lives -= 1
        
    if lives <= -6:
    	screen.fill(BLACK)

    #Creates the scrote variables using pretty font    
    score_text = font.render("Score: " +str(score), True, BLACK)
    lives_text = font.render("Lives: "+ str(lives), True, BLUE)

    #keeps the text on the page at these coordinates
    screen.blit(score_text, [500, 50])
    screen.blit(lives_text, [50, 50])   

    # Draw the scrolling background
    #Add your scrolling background here
    #any_scroller.draw_buildings(screen)
    #any_scroller.move_buildings()

    #trying to add an image
    
    #sky.set_colorkey((255,255,255))
    #sky.get_rect()
    #sky.rect.x = 350
    #sky.rect.y = 400

    # Draw all the sprites  
    all_sprites_list.draw(screen)

    sky_pos -= 1

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Limit to 60 frames per second
    clock.tick(60)

pygame.quit()
exit()

