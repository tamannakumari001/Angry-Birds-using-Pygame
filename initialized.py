''' Here I have initialized all the variable and class instances like birds,buttons,players etc.'''

import random
import pygame
from working import *
from Modules import blocks,birds,Buttons,players





pygame.init()
pygame.mixer.init()
screen=pygame.display.set_mode((1280,720),pygame.FULLSCREEN)
width , height = screen.get_size()


#load audio
pygame.mixer.music.load('Resources/audio/theme_song.mp3')
pygame.mixer.music.set_volume(0.5)
game_over_audio = pygame.mixer.Sound("Resources/audio/game_over.mp3")
bomb_audio = pygame.mixer.Sound("Resources/audio/bomb.mp3")
game_start_audio = pygame.mixer.Sound("Resources/audio/game_start.mp3")
puff_audio = pygame.mixer.Sound("Resources/audio/puff_sound.mp3")
loaded = 1
Prev_cords = 0

#colors
DARK_BROWN = (51,10,7)
MIDNIGHT_BLUE = (25,25,112)
MAROON = (128,0,0)


#backgrounds and surfaces
loading_screen_surf = load_image('Resources/loading.jpg',(width,height))
game_background = load_image('Resources/background.png',(width,height))
main_menu_background = load_image('Resources/play_background.jpg',(width,height))
pregame_background = load_image('Resources/VS.jpg',(width,height))
backgrounds = [loading_screen_surf,main_menu_background,game_background]
dim_surface = pygame.Surface((width,height),pygame.SRCALPHA)
dim_surface.fill((0,0,0,185))
first_to_zero_surf = pygame.image.load("Resources/first_to_zero_loses.png").convert_alpha()
VS = pygame.image.load("Resources/VS.png").convert_alpha()



clock = pygame.time.Clock()

#making it scalable
factor_x = width/1280
factor_y = height/720

#environment
input_box_x = 500*factor_x
input_box_y = 100*factor_y
player_bird_size = 40 * factor_y
menu_bird_size = 80 * factor_y
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
sling0_center= (290*factor_x,535*factor_y)
sling1_center = (width-(290)*factor_x,535*factor_y)
sling0 = pygame.image.load("Resources/sling.png").convert_alpha()
sling_hand=pygame.image.load("Resources/onehandofsling.png").convert_alpha()
sling0x,sling0y = sling0.get_size()
sling0 = pygame.transform.scale(sling0, (sling0x*factor_x,sling0y*factor_y))
slinghandx,slinghandy = sling_hand.get_size()
sling_0_hand = pygame.transform.scale(sling_hand, (slinghandx*factor_x,slinghandy*factor_y))
sling0_rect = sling0.get_rect(midbottom = sling0_pos)
sling1 = pygame.transform.flip(sling0, flip_x=True,flip_y=False)
sling_1_hand = pygame.transform.flip(sling_0_hand,flip_x = True, flip_y = False)
sling1_rect = sling1.get_rect(midbottom=sling1_pos)

#fonts
font = pygame.font.Font("Resources/Fonts/angrybirds-regular.ttf",int(input_box_y/2 -15*factor_y))
font_winner = pygame.font.Font("Resources/Fonts/angrybirds-regular.ttf",int(150*factor_y))
large_font = pygame.font.Font("Resources/Fonts/angrybirds-regular.ttf",int(175*factor_y))
small_font = pygame.font.Font("Resources/Fonts/angrybirds-regular.ttf",int(170*factor_y))

#game_state_booleans
game_start = False
game_over = False
played_game_over = False
music_is_paused=False
both_inputs_done = False
showing_rules = True
start_show = False
wind_state = [False,None]



game_over_logo = pygame.image.load("Resources/game_over.png").convert_alpha()
game_over_logo_rect = game_over_logo.get_rect(center = (width/2,height/2))

#BIRDS
big_Red_surf = load_image("Resources/big_red.png",(player_bird_size*2,player_bird_size*2))
red_description = pygame.image.load("Resources/red_description.png").convert_alpha()
red_description = pygame.transform.scale(red_description, (factor_x*red_description.get_width(),factor_x*red_description.get_height()))
chuck_description = pygame.image.load("Resources/chuck_description.png").convert_alpha()
chuck_description = pygame.transform.scale(chuck_description, (factor_x*chuck_description.get_width(),factor_x*chuck_description.get_height()))
bomb_description = pygame.image.load("Resources/bomb_description.png").convert_alpha()
bomb_description = pygame.transform.scale(bomb_description, (factor_x*bomb_description.get_width(),factor_x*bomb_description.get_height()))
blue_description = pygame.image.load("Resources/blue_description.png").convert_alpha()
blue_description = pygame.transform.scale(blue_description, (factor_x*blue_description.get_width(),factor_x*blue_description.get_height()))
bird_menu = pygame.image.load("Resources/menu.png").convert_alpha()
bird_menu = pygame.transform.scale(bird_menu, (factor_x*(bird_menu.get_width()-20),factor_x*(bird_menu.get_height()-20)))
position = (5*width/12,5*height/16)


#player 0 birds
red_0=birds.red(player_bird_size,player_bird_size,sling0_center[0],sling0_center[1],0)
chuck_0=birds.chuck(player_bird_size,player_bird_size,sling0_center[0],sling0_center[1],0)
bomb_0=birds.bomb(player_bird_size,player_bird_size,sling0_center[0],sling0_center[1],0)
blue_0=birds.blue(player_bird_size,player_bird_size,sling0_center[0],sling0_center[1],0)
blueA_0=birds.blue(player_bird_size,player_bird_size,sling0_center[0],sling0_center[1],0)
blueB_0=birds.blue(player_bird_size,player_bird_size,sling0_center[0],sling0_center[1],0)
big_Red_0_surf = pygame.transform.flip(big_Red_surf,flip_x=0,flip_y=False)


#player 1 birds
red_1=birds.red(player_bird_size,player_bird_size,sling1_center[0],sling1_center[1],1)
chuck_1=birds.chuck(player_bird_size,player_bird_size,sling1_center[0],sling1_center[1],1)
bomb_1=birds.bomb(player_bird_size,player_bird_size,sling1_center[0],sling1_center[1],1)
blue_1=birds.blue(player_bird_size,player_bird_size,sling1_center[0],sling1_center[1],1)
blueA_1=birds.blue(player_bird_size,player_bird_size,sling1_center[0],sling1_center[1],1)
blueB_1=birds.blue(player_bird_size,player_bird_size,sling1_center[0],sling1_center[1],1)
big_Red_1_surf = pygame.transform.flip(big_Red_surf,flip_x=1,flip_y=False)


#Menu_button_birds
font_menu = pygame.font.Font("Resources/Fonts/angrybirds-regular.ttf",int(50*factor_x))
red_m = birds.red(menu_bird_size,menu_bird_size,width/3,3*height/8,1)
chuck_m = birds.chuck(menu_bird_size,menu_bird_size,width/3,4*height/8,1)
bomb_m = birds.bomb(menu_bird_size,menu_bird_size,width/3,5*height/8,1)
blue_m = birds.blue(menu_bird_size,menu_bird_size,width/3,6*height/8,1)
red_menu = Buttons.Button("RED",(red_m.x,red_m.y),screen,red_m.surface,button_desc=red_description,des_pos=position)
bomb_menu = Buttons.Button("BOMB",(bomb_m.x,bomb_m.y),screen,bomb_m.surface,button_desc=bomb_description,des_pos=position)
blue_menu = Buttons.Button("BLUE",(blue_m.x,blue_m.y),screen,blue_m.surface,button_desc=blue_description,des_pos=position)
chuck_menu = Buttons.Button("CHUCK",(chuck_m.x,chuck_m.y),screen,chuck_m.surface,button_desc=chuck_description,des_pos=position)

#Bird booleans
bomb_ability_active = False
blast_starts = False
triplify_bool = False
max_bomb_usage = random.randint(0,5)
red_ability_active = False
can_active_triplify = True


#BUTTONs
buttons = pygame.image.load('Resources/selected-buttons.png').convert_alpha()
rect = pygame.Rect(265,0,230,230)
play_button_image = buttons.subsurface(rect).copy()
play_button = Buttons.Button("Play", (width/2,height/2.2), screen, play_button_image,factor_x,factor_y)
rect = pygame.Rect(150,112,120,120)
quit_button_image = buttons.subsurface(rect).copy()
quit_button = Buttons.Button("Quit", (width - 120, 100), screen, quit_button_image)
logo_surf = pygame.image.load("Resources/logo.png").convert_alpha()
logo_surf = pygame.transform.scale(logo_surf,(factor_x*logo_surf.get_width()/0.8,factor_y*logo_surf.get_height()/0.8))
logo_rect = logo_surf.get_rect(center = (width/2,3*height/5))
pause_button_image=pygame.image.load("Resources/pause-button.png").convert_alpha()
resume_button_image=pygame.image.load("Resources/play_button.png").convert_alpha()
retry_button_image = load_image("Resources/retry_button.png",resume_button_image.get_size())
wind_button_image = load_image("Resources/wind_button.png",(150*factor_x,100*factor_y))
newgame_button_image = load_image("Resources/new_game.png",(400*factor_x,200*factor_y))
pause_button = Buttons.Button("Pause",(width - 120, 200), screen, pause_button_image)
resume_button = Buttons.Button("resume",(width - 120, 200), screen, resume_button_image)
retry_button = Buttons.Button("retry",(width - 120, 300), screen, retry_button_image)
wind_button0 = Buttons.Button("WIND0",(width/20 ,height/2), screen, wind_button_image)
wind_button1 = Buttons.Button("WIND1",(19*width/20 ,height/2), screen, wind_button_image)
new_game_button = Buttons.Button("newgame",(width/8 ,height/8), screen, newgame_button_image)


#PLAYER_NAME_INPUT and ACTIVATION
input_player0 = pygame.Rect(width/2 - input_box_x/2, height/2 - 20*factor_y - input_box_y, input_box_x, input_box_y )
input_player1 = pygame.Rect(width/2 - input_box_x/2, height/2 + 20*factor_y + input_box_y, input_box_x, input_box_y )
input0_bool = input1_bool =True
input_box =load_image("Resources/intro_box.png",(input_box_x+70*factor_x,input_box_y+140*factor_y))
player0 = players.player("",bs0,sling0_center,0,wind_button0)
player1 = players.player("",bs1,sling1_center,1,wind_button1)
random_player_activation(player1,player0)


#bird_disappear_animation
puff_list = []
for i in range(2):
    puff_str = f"Resources/puff_Explode ({i}).png"
    puff_surf = load_image(puff_str,(player_bird_size*2,player_bird_size*2))
    puff_list.append(puff_surf)
bomb_blast_surf = pygame.image.load("Resources/bomb_blast.png")

#timers

winner_timer = 300
puff_timer = 102
loading_time = 600
