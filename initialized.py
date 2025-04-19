# import os
import sys
# import math
import pygame
from working import *
from Modules import blocks,birds,Buttons,players





pygame.init()
screen=pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
width , height = screen.get_size()
factor_x = width/1280
factor_y = height/720
input_box_x = 500*factor_x
input_box_y = 100*factor_y
player_bird_size = 40 * factor_y
menu_bird_size = 80 * factor_y
background = pygame.transform.scale(pygame.image.load('Resources/background.png').convert_alpha(),(width,height))
bs1 = blocks.block_set(screen,)
bs0 = bs1.copy()
block_side=60*factor_y
bs_0_pos = (100*factor_x,400*factor_y)
bs_1_pos = (width - (100)*factor_x, 400*factor_y)
bs_0_rect = pygame.Rect(bs_0_pos[0],bs_0_pos[1],2*block_side,5*block_side)
bs_1_rect = pygame.Rect(bs_1_pos[0]-block_side,bs_1_pos[1],2*block_side,5*block_side)
sling0_pos = (300*factor_x,710*factor_y)
sling1_pos = (width-(300)*factor_x,710*factor_y)
sling0_center= (290*factor_x,530*factor_y)
sling1_center = (width-(290)*factor_x,530*factor_y)
sling0 = pygame.image.load("Resources/sling.png").convert_alpha()
sling0x,sling0y = sling0.get_size()
sling0 = pygame.transform.scale(sling0, (sling0x*factor_x,sling0y*factor_y))
sling0_rect = sling0.get_rect(midbottom = sling0_pos)
sling1 = pygame.transform.flip(sling0, flip_x=True,flip_y=False)
sling1_rect = sling1.get_rect(midbottom=sling1_pos)
font = pygame.font.Font("Resources/Fonts/angrybirds-regular.ttf",int(input_box_y/2 -15*factor_y))
font_winner = pygame.font.Font("Resources/Fonts/angrybirds-regular.ttf",int(150*factor_y))
birds_Selected_0 = birds_Selected_1= False
game_start = False
game_over = False

#BIRDS
#player 0 birds
red_0=birds.red(player_bird_size,player_bird_size,sling0_center[0],sling0_center[1],0)
chuck_0=birds.chuck(player_bird_size,player_bird_size,sling0_center[0],sling0_center[1],0)
bomb_0=birds.bomb(player_bird_size,player_bird_size,sling0_center[0],sling0_center[1],0)
blue_0=birds.blue(player_bird_size,player_bird_size,sling0_center[0],sling0_center[1],0)

#player 1 birds
red_1=birds.red(player_bird_size,player_bird_size,sling1_center[0],sling1_center[1],1)
chuck_1=birds.chuck(player_bird_size,player_bird_size,sling1_center[0],sling1_center[1],1)
bomb_1=birds.bomb(player_bird_size,player_bird_size,sling1_center[0],sling1_center[1],1)
blue_1=birds.blue(player_bird_size,player_bird_size,sling1_center[0],sling1_center[1],1)

#Menu_button_birds
font_menu = pygame.font.Font("Resources/Fonts/angrybirds-regular.ttf",50)
red_m = birds.red(menu_bird_size,menu_bird_size,width/2,3*height/8,1)
chuck_m = birds.chuck(menu_bird_size,menu_bird_size,width/2,4*height/8,1)
bomb_m = birds.bomb(menu_bird_size,menu_bird_size,width/2,5*height/8,1)
blue_m = birds.blue(menu_bird_size,menu_bird_size,width/2,6*height/8,1)
red_menu = Buttons.Button("RED",(red_m.x,red_m.y),screen,red_m.surface)
bomb_menu = Buttons.Button("BOMB",(bomb_m.x,bomb_m.y),screen,bomb_m.surface)
blue_menu = Buttons.Button("BLUE",(blue_m.x,blue_m.y),screen,blue_m.surface)
chuck_menu = Buttons.Button("CHUCK",(chuck_m.x,chuck_m.y),screen,chuck_m.surface)




#PLAY BUTTON
buttons = pygame.image.load('Resources/selected-buttons.png').convert_alpha()
rect = pygame.Rect(265,0,230,230)
play_button_image = buttons.subsurface(rect).copy()
play_button = Buttons.Button("Play", (width/2,height/2), screen, play_button_image)
rect = pygame.Rect(150,112,120,120)
quit_button_image = buttons.subsurface(rect).copy()
quit_button = Buttons.Button("Quit", (width - 120, 100), screen, quit_button_image)

#PLAYER_NAME_INPUT
input_player0 = pygame.Rect(width/2 - input_box_x/2, height/2 - 20*factor_y - input_box_y, input_box_x, input_box_y )
input_player1 = pygame.Rect(width/2 - input_box_x/2, height/2 + 20*factor_y + input_box_y, input_box_x, input_box_y )
input0_bool = input1_bool =True
input_box = pygame.image.load("Resources/intro_box.png").convert_alpha()
input_box = pygame.transform.scale(input_box,(input_box_x+70*factor_x,input_box_y+140*factor_y))
both_inputs_done = False
player0 = players.player("",bs0,sling0_center)
player1 = players.player("",bs1,sling1_center)
player0.activate_player()






