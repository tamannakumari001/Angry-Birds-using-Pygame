# import os
import sys
# import math
# import time
import pygame
from working import *
from Modules import blocks,birds,Buttons



pygame.init()

screen=pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running=True
width , height = screen.get_size()
background = pygame.transform.scale(pygame.image.load('Resources/background.png').convert_alpha(),(width,height))
bs1 = blocks.block_set(screen)
bs0 = bs1.copy()
bs_0_pos = (100,400)
bs_1_pos = (width - 100, 400)
bs_0_rect = pygame.Rect(bs_0_pos[0],bs_0_pos[1],2*blocks.block_side,5*blocks.block_side)
bs_1_rect = pygame.Rect(bs_1_pos[0],bs_1_pos[1],2*blocks.block_side,5*blocks.block_side)
sling0_pos = (300,710)
sling1_pos = (width-300,710)
sling0_center= (290,530)
sling1_center = (width-290,530)
sling0 = pygame.image.load("Resources/sling.png").convert_alpha()
sling0_rect = sling0.get_rect(midbottom = sling0_pos)
sling1 = pygame.transform.flip(sling0, flip_x=True,flip_y=False)
sling1_rect = sling1.get_rect(midbottom=sling1_pos)
b = birds.chuck(40,40,sling1_center[0],sling1_center[1],1)
b.isactive = True
b_Rect = b.surface.get_rect(center = sling1_center)
font = pygame.font.Font("Resources/Fonts/angrybirds-regular.ttf")
buttons = pygame.image.load('Resources/selected-buttons.png').convert_alpha()
rect = pygame.Rect(265,0,230,230)
play_button_image = buttons.subsurface(rect).copy()
play_button = Buttons.Button("Play", (width/2,height/2), screen, play_button_image)




