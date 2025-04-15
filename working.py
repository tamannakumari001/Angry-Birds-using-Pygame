import pygame
from Modules import birds,blocks

power_factor = 10

def launch_bird(object : birds.bird, rect : pygame.Rect, mouse_pos, sling_pos):
    if rect.collidepoint(mouse_pos):
        if(pygame.mouse.get_pressed()[0]):
            object.ready = True
            object.x = mouse_pos[0]
            object.y = mouse_pos[1]
        if(pygame.mouse.get_just_released()[0]):
            object.velocity[0] = (sling_pos[0] - object.x)*power_factor
            object.velocity[1] = (sling_pos[1] - object.y)*power_factor

def collide_bird(bird: birds.bird, block_rect: pygame.Rect):
    if(block_rect.collidepoint((bird.x,bird.y))):
        return True
    else: return False

def damage_done(bird : birds.bird, block_rect: pygame.Rect,done_to_side,bs_pos,block_set : blocks.block_set):
    block_index = blocks.get_block((bird.x,bird.y),done_to_side,bs_pos)
    print(block_index)
    if (block_set.health[block_index[0],block_index[1]])>0:
        bird.isactive = False
        bird.ready = False
        if (block_set.arr[block_index[0],block_index[1]] == bird.type):
            dec = 50
        else:
            dec = 25
            
            
        block_set.health[block_index[0],block_index[1]] -= dec




