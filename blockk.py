import pygame
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DARK_SLATE_BLUE = (72, 61, 139)
PINK = (255, 20, 147)
GRAY = (190, 190, 190)
TEAL = (135, 206, 250)

pygame.init()

screen_width = 700
screen_height = 500
screen = pygame.display.set_mode([screen_width, screen_height])

'''
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
'''

class Block(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.x = screen_width

    def update(self):
        self.rect.x -= 3
        if self.rect.x < 0:
            self.rect.y = random.randrange(0, screen_height)
            self.rect.x = screen_width + 10


pink_block_list = pygame.sprite.Group()
green_block_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()
player = Block(GRAY, 20, 15)


def make_blocks():
    all_sprites_list.add(player)
    
    for i in range(50):   
        pink_block = Block(PINK, 20, 15)
        green_block = Block(TEAL, 20, 15)
        
        pink_block.rect.x = random.randrange(screen_width, screen_width * 2)
        pink_block.rect.y = random.randrange(screen_height)

        green_block.rect.x = random.randrange(screen_width, screen_width * 2)
        green_block.rect.y = random.randrange(screen_height)

        pink_block_list.add(pink_block)
        green_block_list.add(green_block)
        all_sprites_list.add(pink_block)
        all_sprites_list.add(green_block)
