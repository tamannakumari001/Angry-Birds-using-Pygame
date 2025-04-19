import pygame
import time
from Modules import birds,blocks,players,Buttons

power_factor = 5
t = 1
crown_fact = 1



def launch_bird(object : birds.bird, rect : pygame.Rect, mouse_pos, sling_pos,side):
    if rect.collidepoint(mouse_pos):
        if(pygame.mouse.get_pressed()[0]):
            object.being_dragged = True
            object.x = mouse_pos[0]
            object.y = mouse_pos[1]
        if(pygame.mouse.get_just_released()[0]):
            object.ready = True
            object.just_launched = True
            object.velocity[0] = min(abs(sling_pos[0] - object.x)*power_factor,1500)*(-1)**(side-1)
            object.velocity[1] = min((sling_pos[1] - object.y)*power_factor,1500)
            object.being_dragged = False

def show_trajectory(object : birds.bird,sling_pos,number,screen : pygame.Surface,side,factor_x,factor_y):
    u = min(abs(sling_pos[0] - object.x)*power_factor,1500)*(-1)**(side-1)
    v = min((sling_pos[1] - object.y)*power_factor,1500)
    for i in range(number):
        i = i/5
        x = object.x + u*i*factor_x
        y = object.y + (v*i + 0.5*birds.g*i*i)*factor_y

        if ((-1)**(side-1)*x<(-1)**(side-1)*(3*screen.get_width()/5 + (side-1)*screen.get_width()/5)):
            pygame.draw.circle(screen,"Black", (x,y),10)



def collide_bird(bird: birds.bird, block_rect: pygame.Rect):
    if(block_rect.collidepoint((bird.x,bird.y))):
        return True
    else: return False

def show_bird_menu(b1 : Buttons.Button,b2:Buttons.Button,b3:Buttons.Button,b4:Buttons.Button,screen : pygame.Surface, name: str,font:pygame.font,factor_y):
    heading_surf = font.render("Choose 3 birds "+ name, True, "Black")
    heading_rect = heading_surf.get_rect(center = (b1.pos[0], b1.pos[1] - 200*factor_y))
    screen.blit(heading_surf, heading_rect)
    b1.display()
    b2.display()
    b3.display()
    b4.display()



def damage_done(bird : birds.bird, done_to_side,bs_pos,player_target: players.player, player_play:players.player,block_side):
    block_index = blocks.get_block((bird.x,bird.y),done_to_side,bs_pos,block_side)
    if (player_target.bs.health[block_index[0],block_index[1]])>0:
        bird.isactive = False
        bird.ready = False
        if (player_target.bs.arr[block_index[0],block_index[1]] == bird.type):
            dec = 50
        elif bird.type == 0:
            dec = 30
        else:
            dec = 20 
        player_target.bs.health[block_index[0],block_index[1]] -= dec
        player_target.score = player_target.score - dec
        if player_target.bs.health[block_index[0],block_index[1]] < 0:
            player_target.score -= player_target.bs.health[block_index[0],block_index[1]]

        player_play.deactivate_player()
        player_target.activate_player()


def draw_input(screen: pygame.Surface,input_rect : pygame.Rect, color, player : str,font : pygame.font,player_name,border,factor_x,factor_y):
    pygame.draw.rect(screen,color,input_rect,border_radius=int(10*factor_y))
    screen.blit(border,(input_rect.x-5*factor_x,input_rect.y-input_rect.height+20*factor_y))
    text_surface = font.render("Enter " + player, True, "White")
    screen.blit(text_surface,(input_rect.x + 130*factor_x, input_rect.y + 10*factor_y))
    text_surface = font.render(player_name,True,"White")
    screen.blit(text_surface,(input_rect.x + 130*factor_x, input_rect.y + 60*factor_y))

def select_birds(player: players.player, b1:Buttons.Button,b2:Buttons.Button,b3:Buttons.Button,b4:Buttons.Button,screen : pygame.Surface,font,B1,B2,B3,B4,factor_y):
    show_bird_menu(b1,b2,b3,b4,screen,player.name,font,factor_y)
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
    crown_surf = pygame.transform.scale(pygame.image.load('Resources/crown.png'),(300,300))
    crown_rect = crown_surf.get_rect(center = (screen.get_width()/2,screen.get_height()/2 - 200 + (crown_fact**2)*10 - 640))
    screen.blit(winner_surf,winner_rect)
    screen.blit(crown_surf, crown_rect)
    if (t<4): t += 0.5
    if (crown_fact < 8): crown_fact+=0.5
    winner_name_surf = font.render(winner.name, True, "Black")
    winner_name_rect = winner_name_surf.get_rect(center = (screen.get_width()/2,5*screen.get_height()/6))
    screen.blit(winner_name_surf,winner_name_rect)
    screen.blit(crown_surf,crown_rect)

    





    

    





