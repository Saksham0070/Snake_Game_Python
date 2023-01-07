import pygame #pygame module
import time #time module
from pygame.locals import * #To import locals event like KEYDOWN OR QUIT

def draw_block(block_x,block_y): 
    surface.fill((80,199,199)) #again fill the color of background so that it seems like previous blocks are disappearing
    surface.blit(block,(block_x,block_y))
    pygame.display.flip()

pygame.init() #always we have to initialise the pygame module

surface = pygame.display.set_mode((1000,500)) #game main screen
surface.fill((80,199,199)) #RGB color for background

block = pygame.image.load(r"C:\Users\sagar\OneDrive\Desktop\SeekPng.com_squares-png_1155496 (1).jpg").convert() #image of block use for snake body
block_x = 100
block_y = 100
surface.blit(block,(block_x,block_y)) #block coordinate

pygame.display.flip() #whenever we are changing any any thing in the screen then we have to call again this method
# time.sleep(5) #time lapse to show screen at least 5 seconds


#These helps to obtain the screen in infinte time
running = True

# while True:
#     pass

#but we have to end it somewhere ,then we have to use some event loop concept to end the UI in python

# while running :
#     pygame.event.get() #this event funct captures all the events, like we click right or left then it captures it.

#These piece of code helps to move the snake.
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            # if event.key == K_0:

            if event.key == K_ESCAPE:
                running = False

            if event.key == K_UP:
                block_y = block_y - 10
                draw_block(block_x,block_y)

            if event.key == K_DOWN:
                block_y = block_y + 10
                draw_block(block_x,block_y)

            if event.key == K_LEFT:
                block_x = block_x - 10
                draw_block(block_x,block_y)

            if event.key == K_RIGHT:
                block_x = block_x + 10
                draw_block(block_x,block_y)

        elif event.type == QUIT:   # Quit event is used in cancel the program
             running = False


