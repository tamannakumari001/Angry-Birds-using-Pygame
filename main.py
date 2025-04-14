# import os
# import sys
# import math
# import time
import pygame
from Modules import blocks

pygame.init()

screen=pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running=True
width , height = screen.get_size()
background = pygame.transform.scale(pygame.image.load('Resources/background.png').convert_alpha(),(width,height))
bs1 = blocks.block_set(screen)

while  running:
    events=pygame.event.get()
    for event in events:
        if event.type==pygame.QUIT:
            running=False

    screen.blit(background,(0,0))
    bs1.create_block_set((100,500),0)
    bs1.create_block_set((width - 100, 500),1)
    pygame.display.flip()
    clock.tick(60)


pygame.quit()