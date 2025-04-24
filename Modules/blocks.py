import numpy as np
import pygame

block_types=['all','wood','stone','ice'] #List of possible blocks

#load_block_images
wood100 = pygame.image.load("Resources/wood_block_100.png")
wood75 = pygame.image.load("Resources/wood_block_75.png")
wood50 = pygame.image.load("Resources/wood_block_50.png")
wood25 = pygame.image.load("Resources/wood_block_25.png")
ice100 = pygame.image.load("Resources/ice_block_100.png")
ice75 = pygame.image.load("Resources/ice_block_75.png")
ice50 = pygame.image.load("Resources/ice_block_50.png")
ice25 = pygame.image.load("Resources/ice_block_25.png")
stone100 = pygame.image.load("Resources/stone_block_100.png")
stone75 = pygame.image.load("Resources/stone_block_75.png")
stone50 = pygame.image.load("Resources/stone_block_50.png")
stone25 = pygame.image.load("Resources/stone_block_25.png")



class block:
    def __init__(self, type, pos_in_block_set, bs_pos, screen: pygame.Surface,side,health,block_side):
        self.type = block_types[type]
        self.side = block_side
        self.health = health
        self.screen = screen
        self.player = side
        self.pos = (bs_pos[0] + (block_side)*pos_in_block_set[0]*(-1)**self.player,bs_pos[1] + (block_side)*pos_in_block_set[1])
        self.rectangle = pygame.Rect(self.pos[0],self.pos[1],block_side,block_side)
        self.color = None
        
        

    # def get_image(self):
    #     if (self.type == "wood"):
    #         self.color = f""
    #     elif(self.type == "stone"):
    #         self.color = (116,117,120)
    #     elif(self.type == "ice"):
    #         self.color = (5,205,248)
    #     return self.color
    
    def create_block(self):
        if(self.health>0):
            if (self.type == "wood" and 75 < self.health <= 100):
                surf = pygame.transform.scale(wood100,(self.side,self.side))
            if (self.type == "wood" and 50 <self.health <= 75):
                surf = pygame.transform.scale(wood75,(self.side,self.side))
            if (self.type == "wood" and 25 < self.health <= 50):
                surf =pygame.transform.scale(wood50,(self.side,self.side))
            if (self.type == "wood" and 0 < self.health <= 25):
                surf =pygame.transform.scale(wood25,(self.side,self.side))
            if (self.type == "ice" and 75 <self.health <= 100):
                surf =pygame.transform.scale(ice100,(self.side,self.side))
            if (self.type == "ice" and 50 < self.health <= 75):
                surf =pygame.transform.scale(ice75,(self.side,self.side))
            if (self.type == "ice" and 25 < self.health <= 50):
                surf =pygame.transform.scale(ice50,(self.side,self.side))
            if (self.type == "ice" and 0 < self.health <= 25):
                surf =pygame.transform.scale(ice25,(self.side,self.side))
            if (self.type == "stone" and 75 < self.health <= 100):
                surf =pygame.transform.scale(stone100,(self.side,self.side))
            if (self.type == "stone" and 50<self.health <= 75):
                surf =pygame.transform.scale(stone75,(self.side,self.side))
            if (self.type == "stone" and 25 < self.health <= 50):
                surf =pygame.transform.scale(stone50,(self.side,self.side))
            if (self.type == "stone" and 0 < self.health <= 25):
                surf =pygame.transform.scale(stone25,(self.side,self.side))
            self.screen.blit(surf,self.pos)
    def reddify(self):
        if self.health>0:
            red_surf = pygame.Surface((self.side,self.side),pygame.SRCALPHA)
            red_surf.fill((255,0,0,64))
            self.screen.blit(red_surf,self.pos)






class block_set:
    def __init__(self, screen: pygame.Surface):
        self.arr = np.random.choice([1,2,3], size = (2,5))
        self.health = np.array([[100,100,100,100,100],[100,100,100,100,100]])   
        self.screen = screen
        self.cords = []

    def create_block_set(self,pos,side,block_side):
        for i in range(len(self.arr)):
            for j in range (len(self.arr[i])):
                myblock = block(self.arr[i,j],(i,j),pos,self.screen,side,self.health[i,j],block_side)
                myblock.create_block()
                if (myblock.rectangle.x,myblock.rectangle.y) not in self.cords:
                    self.cords.append((myblock.rectangle.x,myblock.rectangle.y))
    def reddify_block_set(self,pos,side,block_side):
        for i in range(len(self.arr)):
            for j in range (len(self.arr[i])):
                myblock = block(self.arr[i,j],(i,j),pos,self.screen,side,self.health[i,j],block_side)
                myblock.reddify()
    

    def copy(self):
        out = block_set(self.screen)
        out.arr = self.arr
        return out

    
    
    
    
def get_block(pos,side,bs_pos,block_side):
    x_pos = int(((pos[0]-bs_pos[0]))//block_side) *((-1)**side) 
    y_pos = int((pos[1] - bs_pos[1])/block_side)
    return x_pos,y_pos







    
                








