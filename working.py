import pygame
import math
from Modules import birds,blocks,players,Buttons

power_factor = 5*2.25
t = 1
crown_fact = 1
pygame.mixer.init()
wood_crack = pygame.mixer.Sound("Resources/audio/wood-crack.mp3")
stone_crack = pygame.mixer.Sound("Resources/audio/stone-crack.mp3")
ice_crack = pygame.mixer.Sound("Resources/audio/ice-crack.mp3")
bir_scream = pygame.mixer.Sound("Resources/audio/bird_scream.mp3")
block_crack_sound_list = [None,wood_crack,stone_crack,ice_crack]
current_bg = 0



def launch_bird(object : birds.bird, rect : pygame.Rect, mouse_pos, sling_pos,factor):
    if rect.collidepoint(mouse_pos):
        if(pygame.mouse.get_pressed()[0]):
            object.being_dragged = True
    if object.being_dragged:
        if(pygame.mouse.get_just_released()[0]):
            bir_scream.play()
            object.ready = True
            object.velocity[0] = (sling_pos[0] - object.x)*power_factor/factor
            object.velocity[1] = (sling_pos[1] - object.y)*power_factor/factor
            object.being_dragged = False

def show_trajectory(object : birds.bird,sling_pos,number,screen : pygame.Surface,side,factor_x,factor_y):
    u = (sling_pos[0] - object.x)*power_factor/factor_x
    v = (sling_pos[1] - object.y)*power_factor/factor_x
    for i in range(number):
        i = 2*i/number
        x = object.x + u*i*factor_x
        y = object.y + (v*i + 0.5*birds.g*i*i)*factor_y

        if ((-1)**(side-1)*x<(-1)**(side-1)*(3*screen.get_width()/4 + (side-1)*screen.get_width()/2)):
            pygame.draw.circle(screen,"Black", (x,y),10)

def show_stretch(b : birds.bird, start,screen : pygame.Surface,factor,color):
    pygame.draw.line(screen,color,(start[0]-20*factor,start[1]),(b.x,b.y),int(10*factor))
    pygame.draw.line(screen,color,(start[0]+20*factor,start[1]),(b.x,b.y),int(10*factor))

def collide_bird(bird: birds.bird, block_rect: pygame.Rect):
    if(block_rect.collidepoint((bird.x,bird.y))):
        return True
    else: return False

def show_bird_menu(b1 : Buttons.Button,b2:Buttons.Button,b3:Buttons.Button,b4:Buttons.Button,screen : pygame.Surface, name: str,font:pygame.font,factor_y,intro):
    heading_surf = font.render("Choose 3 birds "+ name, True, "Black")
    heading_rect = heading_surf.get_rect(center = (b1.pos[0], b1.pos[1] - 200*factor_y))
    screen.blit(heading_surf, heading_rect)
    screen.blit(intro,(b1.des_pos[0] + 10, b1.des_pos[1] + 10))
    b1.display()
    b2.display()
    b3.display()
    b4.display()

def score_update(player_target : players.player, dec , i, j):
    if player_target.bs.health[i,j] > 0:
        player_target.bs.health[i,j] -= dec
        player_target.score = player_target.score - dec
        if player_target.bs.health[i,j] < 0:
            player_target.score -= player_target.bs.health[i,j]


def bounce_back(bird : birds.bird , x1,x2,y1,y2,inside,outside,block_side):
    poc = point_of_contact(x1,x2,y1,y2,inside,outside)
    # sign = (-1)**target_side
    # i = block_index[0]
    # j = block_index[1]
    # if block_index[1]>0 and player_target.bs.health[i,j-1] >0 and poc[1] == y1:

    bird.x = poc[0]
    bird.y = poc[1]
    if poc[0] == x1 or poc[0]==x2 :
        bird.velocity[0] *= -0.5
    if poc[1] == y1 or poc[1]==y2 :
        bird.velocity[1] *= -0.5
        


def damage_done(bird : birds.bird, done_to_side,bs_pos,player_target: players.player, player_play:players.player,block_side,prev_cords,bool):
    # damage_done_by_dupli(bird,done_to_side,bs_pos,player_target,block_side)
    block_index = blocks.get_block((bird.x,bird.y),done_to_side,bs_pos,block_side)
    if (player_target.bs.health[block_index[0],block_index[1]])>0:
        type_block =player_target.bs.arr[block_index[0],block_index[1]]
        block_crack_sound_list[type_block].play()

        # bird.isactive = False
        # bird.ready = False
        speed = (bird.velocity[0]**2 + bird.velocity[1]**2)**0.5
        if (type_block == bird.type):
            dec = int(100*speed/1500)
        elif bird.type == 0:
            dec = int(60*speed/1500)
        else:
            dec = int(30*speed/1500)

        if not bool:
            x1 = player_target.bs.cords[5*block_index[0] + block_index[1]][0]
            y1 = player_target.bs.cords[5*block_index[0] + block_index[1]][1]
            x2 = x1+block_side
            y2 = y1+block_side
            # print(x1,x2,y1,y2,prev_cords,bird.x,bird.y)

            bounce_back(bird,x1,x2,y1,y2,(bird.x,bird.y),prev_cords,block_side)
        else:
            dec = 100
            if block_index[1]!=0 and block_index[1]!=4:
                score_update(player_target,50,block_index[0],block_index[1]-1)
                score_update(player_target,50,block_index[0],block_index[1]+1)

        score_update(player_target,dec,block_index[0],block_index[1])
        print(player_target.bs.health)


        # player_target.bs.health[block_index[0],block_index[1]] -= dec
        # player_target.score = player_target.score - dec
        # if player_target.bs.health[block_index[0],block_index[1]] < 0:
        #     player_target.score -= player_target.bs.health[block_index[0],block_index[1]]


        
        # if blocks.get_block((bird.x-(block_side)*(-1)**done_to_side,bird.y),done_to_side,bs_pos,block_side)[0] == block_index[0]-1:
        #     bird.velocity[0] *= -1
        # if blocks.get_block((bird.x,bird.y-block_side),done_to_side,bs_pos,block_side)[1] == block_index[1]-1:
        #      bird.velocity[1] *= -1
        # if blocks.get_block((bird.x,bird.y+block_side),done_to_side,bs_pos,block_side)[1] == block_index[1]+1:
        #     bird.velocity[1] *= -1
        # player_play.deactivate_player()
        # player_target.activate_player()


def draw_input(screen: pygame.Surface,input_rect : pygame.Rect, color, player : str,font : pygame.font,player_name,border,factor_x,factor_y):
    pygame.draw.rect(screen,color,input_rect,border_radius=int(10*factor_y))
    screen.blit(border,(input_rect.x-5*factor_x,input_rect.y-input_rect.height+20*factor_y))
    text_surface = font.render("Enter " + player, True, "White")
    screen.blit(text_surface,(input_rect.x + 130*factor_x, input_rect.y + 10*factor_y))
    text_surface = font.render(player_name,True,"White")
    screen.blit(text_surface,(input_rect.x + 130*factor_x, input_rect.y + 60*factor_y))

def select_birds(player: players.player, b1:Buttons.Button,b2:Buttons.Button,b3:Buttons.Button,b4:Buttons.Button,screen : pygame.Surface,font,B1,B2,B3,B4,factor_y,intro):
    show_bird_menu(b1,b2,b3,b4,screen,player.name,font,factor_y,intro)
    if b1.is_clicked():
        player.birds.append(B1)
    if b2.is_clicked():
        player.birds.append(B2)
    if b3.is_clicked():
        player.birds.append(B3)
    if b4.is_clicked():
        player.birds.append(B4)

def winner_display(winner : players.player, screen : pygame.Surface,font : pygame.font,factor):
    global t,crown_fact
    winner_surf = pygame.transform.scale(winner.birds[0].surface1,(1500/t * factor,1500/t*factor))
    winner_rect = winner_surf.get_rect(center = (screen.get_width()/2, screen.get_height()/2))
    crown_surf = pygame.transform.scale(pygame.image.load('Resources/crown.png'),(300*factor,300*factor))
    crown_rect = crown_surf.get_rect(center = (screen.get_width()/2,screen.get_height()/2 - 200*factor + (crown_fact**2)*factor*10 - 640*factor))
    screen.blit(winner_surf,winner_rect)
    screen.blit(crown_surf, crown_rect)
    if (t<4): t += 0.5
    if (crown_fact < 8): crown_fact+=0.5
    winner_name_surf = font.render(winner.name, True, "Black")
    winner_name_rect = winner_name_surf.get_rect(center = (screen.get_width()/2,5*screen.get_height()/6))
    screen.blit(winner_name_surf,winner_name_rect)
    screen.blit(crown_surf,crown_rect)

def speed_ability (bird: birds.bird):
    theta = math.atan2(bird.velocity[1],bird.velocity[0])
    bird.velocity[0] = 2500*math.cos(theta)
    bird.velocity[1] = 2500*math.sin(theta)

def bomb_ability(bird : birds.bird, target: players.player, active_player : players.player,done_to_side,bs_pos,block_side,player_target,audio):
    block_index = blocks.get_block((bird.x,bird.y),done_to_side,bs_pos,block_side)
    if (player_target.bs.health[block_index[0],block_index[1]])>0:
        audio.play()

        for i in range(2):
            for j in range (5):
                if target.bs.health[i,j] > 0:
                    target.bs.health[i,j] -= 25
                    target.score -= 25
                    if (target.bs.health[i,j]<0):
                        target.score -= target.bs.health[i,j]
        # bird.isactive = False
        bird.ready = False
        return True
    return False
        # bird.being_dragged = False
        # active_player.deactivate_player()
        # target.activate_player()

# def damage_done_by_dupli(bird : birds.bird, done_to_side,bs_pos,player_target: players.player, block_side):
#     block_index = blocks.get_block((bird.x,bird.y),done_to_side,bs_pos,block_side)
#     if (player_target.bs.health[block_index[0],block_index[1]])>0:
#         bird.isactive = False
#         speed = (bird.velocity[0]**2 + bird.velocity[1]**2)**0.5
#         if (player_target.bs.arr[block_index[0],block_index[1]] == bird.type):
#             dec = int(50*speed/1500)
#         elif bird.type == 0:
#             dec = int(30*speed/1500)
#         else:
#             dec = int(15*speed/1500)
#         player_target.bs.health[block_index[0],block_index[1]] -= dec
#         player_target.score = player_target.score - dec
#         if player_target.bs.health[block_index[0],block_index[1]] < 0:
#             player_target.score -= player_target.bs.health[block_index[0],block_index[1]]




# def playing(font,block_side,b,b_Rect,screen,mouse,active_player,target_side,factor_x,factor_y,target_bs,height,width,bomb_ability_active,max_bomb_usage,target,target_pos,player1,player0,text_surface_1,text_surface_0):
#     if (b.isactive):
#         b_Rect.center = (b.x,b.y)
#         screen.blit(b.surface,b_Rect)
#         launch_bird(b,b_Rect,mouse,active_player.start,target_side)
#         if (b.being_dragged):
#             show_trajectory(b,active_player.start,10,screen,target_side,factor_x,factor_y)

#         if collide_bird(b,target_bs):
#             if not bomb_ability_active:
#                 damage_done(b,target_side,target_pos,target,active_player,block_side)
#             else:
#                 bomb_ability(b,target,active_player)
#                 max_bomb_usage -= 1
#                 bomb_ability_active = False
#         if b.y > height or b.x < 0 or b.x > width : 
#             b.isactive = False
#             b.ready = False
#             b.being_dragged = False
#             active_player.deactivate_player()
#             target.activate_player()

#         score_1 = font.render(str(player1.score), True, "Black")
#         score_1_Rect = text_surface_1.get_rect(center = (3*width/4,height/4+50*factor_y))
#         score_0 = font.render(str(player0.score), True, "Black")
#         score_0_Rect = text_surface_0.get_rect(center = (width/4,height/4+50*factor_y))
#         if b.ready:
#             b.update(factor_x,factor_y)
#             if pygame.mouse.get_pressed()[2]:
#                 if b.type == 2 and max_bomb_usage>0:
#                     bomb_ability_active = True
#                 if b.type==1:    
#                     speed_ability(b)


#         screen.blit(score_1, score_1_Rect)  
#         screen.blit(score_0, score_0_Rect)

def in_between(x,bound1, bound2):
    return bound1 <= x <= bound2 or bound2 <= x <= bound1

def point_of_contact(x1,x2,y1,y2,inside,outside):
    if inside[0] != outside[0]:
        slope = (outside[1] - inside[1])/(outside[0] - inside[0])
    else:
        slope = 1e7
    constant = inside[1] - slope*inside[0]
    if abs(outside[0] - x1) < abs(outside[0] - x2):
        closer_x = x1
    else:
        closer_x = x2
    if abs(outside[1] - y1) < abs(outside[1] - y2):
        closer_y = y1
    else:
        closer_y = y2

    Y = slope*closer_x + constant
    X = (closer_y - constant)/slope

    if in_between(Y,inside[1],outside[1]):
        return (closer_x,Y)

    if in_between(X,inside[0],outside[0]):
        return (X,closer_y)
    return (closer_x,closer_y)

def ground_collision():
    pass





    





    

    





