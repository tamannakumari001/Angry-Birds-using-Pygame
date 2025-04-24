# import os
# import math
import random
import pygame
from working import *
from Modules import blocks,birds,Buttons,players



#you have to work on collisions. We already wrote functions which give us the side of collision.


pygame.init()
pygame.mixer.init()
screen=pygame.display.set_mode((1280,720),pygame.FULLSCREEN)

#load audio
pygame.mixer.music.load('Resources/audio/theme_song.mp3')
loaded = 1
dA = dB = dC= True
Prev_cords = 0

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
bs_1_pos = (width - block_side-(100)*factor_x, 400*factor_y)
bs_0_rect = pygame.Rect(bs_0_pos[0],bs_0_pos[1],2*block_side,5*block_side)
bs_1_rect = pygame.Rect(bs_1_pos[0]-block_side,bs_1_pos[1],2*block_side,5*block_side)
ground_rect = pygame.Rect(0,675*factor_y,width,height-675*factor_y)
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
game_over_surface = pygame.Surface((width,height),pygame.SRCALPHA)
game_over_surface.fill((0,0,0,185))
game_over_logo = pygame.image.load("Resources/game_over.png")
game_over_logo_rect = game_over_logo.get_rect(center = (width/2,height/2))
#BIRDS
big_Red_surf = pygame.image.load("Resources/big_red.png")
#player 0 birds
red_0=birds.red(player_bird_size,player_bird_size,sling0_center[0],sling0_center[1],0)
chuck_0=birds.chuck(player_bird_size,player_bird_size,sling0_center[0],sling0_center[1],0)
bomb_0=birds.bomb(player_bird_size,player_bird_size,sling0_center[0],sling0_center[1],0)
blue_0=birds.blue(player_bird_size,player_bird_size,sling0_center[0],sling0_center[1],0)
blueA_0=birds.blue(player_bird_size,player_bird_size,sling0_center[0],sling0_center[1],0)
blueB_0=birds.blue(player_bird_size,player_bird_size,sling0_center[0],sling0_center[1],0)
big_Red_0_surf = pygame.transform.flip((pygame.transform.scale(big_Red_surf, (player_bird_size*2,player_bird_size*2))),flip_x=0,flip_y=False)
#player 1 birds
red_1=birds.red(player_bird_size,player_bird_size,sling1_center[0],sling1_center[1],1)
chuck_1=birds.chuck(player_bird_size,player_bird_size,sling1_center[0],sling1_center[1],1)
bomb_1=birds.bomb(player_bird_size,player_bird_size,sling1_center[0],sling1_center[1],1)
blue_1=birds.blue(player_bird_size,player_bird_size,sling1_center[0],sling1_center[1],1)
blueA_1=birds.blue(player_bird_size,player_bird_size,sling1_center[0],sling1_center[1],1)
blueB_1=birds.blue(player_bird_size,player_bird_size,sling1_center[0],sling1_center[1],1)
big_Red_1_surf = pygame.transform.flip((pygame.transform.scale(big_Red_surf, (player_bird_size*2,player_bird_size*2))),flip_x=1,flip_y=False)
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

bomb_ability_active = False
triplify_bool = False
max_bomb_usage = random.randint(0,5)
red_ability_active = False
can_active_triplify = True


#PLAY BUTTON
buttons = pygame.image.load('Resources/selected-buttons.png').convert_alpha()
rect = pygame.Rect(265,0,230,230)
play_button_image = buttons.subsurface(rect).copy()
play_button = Buttons.Button("Play", (width/2,height/2.2), screen, play_button_image,factor_x,factor_y)
rect = pygame.Rect(150,112,120,120)
quit_button_image = buttons.subsurface(rect).copy()
quit_button = Buttons.Button("Quit", (width - 120, 100), screen, quit_button_image)
logo_surf = pygame.image.load("Resources/logo.png")
logo_surf = pygame.transform.scale(logo_surf,(factor_x*logo_surf.get_width()/0.8,factor_y*logo_surf.get_height()/0.8))
logo_rect = logo_surf.get_rect(center = (width/2,3*height/5))
loading_screen_surf = pygame.transform.scale(pygame.image.load('Resources/loading_screen.jpg'),(width,height))
loading_time = 600

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

winner_timer = 1200
puff_timer = 102

#puff_animation
puff_list = []
for i in range(2):
    puff_str = f"Resources/puff_Explode ({i}).png"
    puff_surf = pygame.transform.scale((pygame.image.load(puff_str)),(player_bird_size*2,player_bird_size*2))
    puff_list.append(puff_surf)




