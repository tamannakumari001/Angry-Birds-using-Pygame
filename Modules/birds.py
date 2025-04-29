import pygame
g=561
dt = (1/300)
all_type = 0
wood_type = 1
stone_type = 2
ice_type = 3
wind_resistance = 1000




class bird():
    def __init__(self,width,height,x,y):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.isactive = False
        self.ready = False
        self.velocity = [0,0]
        self.being_dragged = False

    def update(self,factor_x,factor_y,wind_state):
        if self.isactive:
            self.velocity[1] += g*(dt*factor_y)
            if wind_state[0]:
                self.velocity[0] += (wind_resistance * dt *factor_y)*(-1)**wind_state[1]
            self.x += self.velocity[0]*(dt*factor_y)*factor_x
            self.y += (self.velocity[1]*dt*factor_y)*factor_y



 #BIRDS


class red(bird):
    def __init__(self,width,height,x,y,side):
        bird.__init__(self,width,height,x,y)
        self.side = side
        self.surface1 = pygame.image.load('Resources/red.png').convert_alpha()
        self.surface = pygame.transform.flip((pygame.transform.scale(self.surface1, (self.width,self.height))),flip_x=side,flip_y=False)
        self.type = all_type



class blue(bird):
    def __init__(self,width,height,x,y,side):
        bird.__init__(self,width,height,x,y)
        self.side = side
        self.surface1 = pygame.image.load('Resources/small_blue.png').convert_alpha()
        self.surface = pygame.transform.flip((pygame.transform.scale(self.surface1, (self.width,self.height))),flip_x=side,flip_y=False)
        self.type = ice_type


class bomb(bird):
    def __init__(self,width,height,x,y,side):
        self.side = side
        bird.__init__(self,width,height,x,y)
        self.surface1 = pygame.image.load('Resources/bomb.png').convert_alpha()
        self.surface = pygame.transform.flip((pygame.transform.scale(self.surface1, (self.width,self.height))),flip_x=side,flip_y=False)
        self.type = stone_type


class chuck(bird):
    def __init__(self,width,height,x,y,side):
        bird.__init__(self,width,height,x,y)
        self.side = side
        self.surface1 = pygame.image.load('Resources/fast_yellow.png').convert_alpha()
        self.surface = pygame.transform.flip((pygame.transform.scale(self.surface1, (self.width,self.height))),flip_x=side,flip_y=False)
        self.type = wood_type

class big_red(bird):
    def __init__(self,width,height,x,y,side):
        bird.__init__(self,width,height,x,y)
        self.side = side
        self.surface1 = pygame.image.load('Resources/big_red.png').convert_alpha()
        self.surface = pygame.transform.flip((pygame.transform.scale(self.surface1, (self.width,self.height))),flip_x=side,flip_y=False)
        self.type = all_type



