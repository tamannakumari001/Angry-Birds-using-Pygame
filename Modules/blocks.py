import numpy as np
import pygame

block_types=[None,'wood','stone','ice'] #List of possible blocks


class block:
    def __init__(self, type, pos_in_block_set, bs_pos, screen: pygame.Surface,side):
        self.type = block_types[type]
        self.side = 40
        self.health = 100
        self.screen = screen
        self.side = side
        self.pos = (bs_pos[0] + 40*pos_in_block_set[0]*(-1)**self.side,bs_pos[1] + 40*pos_in_block_set[1])
        self.rectangle = pygame.Rect(self.pos[0],self.pos[1],40,40)
        

    def get_color(self):
        if (self.type == "wood"):
            self.color = "Brown"
        elif(self.type == "stone"):
            self.color = "Grey"
        elif(self.type == "ice"):
            self.color = "Blue"
        return self.color
    
    def create_block(self):
        print(self.pos)
        self.get_color()
        pygame.draw.rect(self.screen, self.color, (self.pos[0],self.pos[1],40,40))
        print(self.color)



class block_set:
    def __init__(self, screen: pygame.Surface):
        self.arr = np.random.choice([1,2,3], size = (2,5))   
        self.screen = screen

    def create_block_set(self,pos,side):
        for i in range(len(self.arr)):
            for j in range (len(self.arr[i])):
                myblock = block(self.arr[i,j],(i,j),pos,self.screen,side)
                myblock.create_block()
                








