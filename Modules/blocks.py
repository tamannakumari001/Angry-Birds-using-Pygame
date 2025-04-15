import numpy as np
import pygame

block_types=['all','wood','stone','ice'] #List of possible blocks
block_side=60

class block:
    def __init__(self, type, pos_in_block_set, bs_pos, screen: pygame.Surface,side,health):
        self.type = block_types[type]
        self.side = block_side
        self.health = health
        self.screen = screen
        self.side = side
        self.pos = (bs_pos[0] + block_side*pos_in_block_set[0]*(-1)**self.side,bs_pos[1] + block_side*pos_in_block_set[1])
        self.rectangle = pygame.Rect(self.pos[0],self.pos[1],block_side,block_side)
        self.color = None
        
        

    def get_color(self):
        if (self.type == "wood"):
            self.color = (151,95,79)
        elif(self.type == "stone"):
            self.color = (116,117,120)
        elif(self.type == "ice"):
            self.color = (5,205,248)
        return self.color
    
    def create_block(self):
        self.get_color()
        if(self.health>0):
            rect_surf = pygame.Surface((block_side,block_side), pygame.SRCALPHA) #the pixel format will include per pixel alpha to induce transparency based on health
            rect_surf.fill((self.color[0],self.color[1],self.color[2],255*self.health/100))
            self.screen.blit(rect_surf,self.pos)



class block_set:
    def __init__(self, screen: pygame.Surface):
        self.arr = np.random.choice([1,2,3], size = (2,5))
        self.health = np.array([[100,100,100,100,100],[100,100,100,100,100]])   
        self.screen = screen

    def create_block_set(self,pos,side):
        for i in range(len(self.arr)):
            for j in range (len(self.arr[i])):
                myblock = block(self.arr[i,j],(i,j),pos,self.screen,side,self.health[i,j])
                myblock.create_block()

    def copy(self):
        out = block_set(self.screen)
        out.arr = self.arr
        return out

    
    
    
    
def get_block(pos,side,bs_pos):
    x_pos = (((pos[0]-bs_pos[0]))//block_side) *((-1)**side) 
    y_pos = (pos[1] - bs_pos[1])//block_side
    return (int(x_pos),int(y_pos))




    
                








