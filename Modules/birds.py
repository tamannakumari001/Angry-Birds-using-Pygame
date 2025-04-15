import pygame
dt = 1/600
g=561
power_Factor = 10
all_type = 0
wood_type = 1
stone_type = 2
ice_type = 3


class bird():
    def __init__(self,width,height,x,y):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.isactive = False
        self.ready = False
        self.velocity = [0,0]

    def update(self):
        if self.isactive:
            self.velocity[1] = self.velocity[1] + g*dt
            self.x += self.velocity[0]*dt
            self.y += self.velocity[1]*dt + 0.5*g*dt*dt
        





    


 #BIRDS


class red(bird):
    def __init__(self,width,height,x,y,side):
        bird.__init__(self,width,height,x,y)
        self.surface1 = pygame.image.load('Resources/red.png').convert_alpha()
        self.surface = pygame.transform.flip((pygame.transform.scale(self.surface1, (self.width,self.height))),flip_x=side,flip_y=False)
        self.type = all_type


class blue(bird):
    def __init__(self,width,height,x,y,side):
        bird.__init__(self,width,height,x,y)
        self.surface1 = pygame.image.load('Resources/small_blue.png').convert_alpha()
        self.surface = pygame.transform.flip((pygame.transform.scale(self.surface1, (self.width,self.height))),flip_x=side,flip_y=False)
        self.type = ice_type


class bomb(bird):
    def __init__(self,width,height,x,y,side):
        bird.__init__(self,width,height,x,y)
        self.surface1 = pygame.image.load('Resources/bomb.png').convert_alpha()
        self.surface = pygame.transform.flip((pygame.transform.scale(self.surface1, (self.width,self.height))),flip_x=side,flip_y=False)
        self.type = stone_type


class chuck(bird):
    def __init__(self,width,height,x,y,side):
        bird.__init__(self,width,height,x,y)
        self.surface1 = pygame.image.load('Resources/fast_yellow.png').convert_alpha()
        self.surface = pygame.transform.flip((pygame.transform.scale(self.surface1, (self.width,self.height))),flip_x=side,flip_y=False)
        self.type = wood_type




