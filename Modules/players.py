from Modules import birds,blocks

class player:
    def __init__(self,name,block_Set: blocks.block_set,sling,side,wind_button):
        self.name = name
        self.birds = []
        self.score = 1000
        self.active = False
        self.current_bird = 2
        self.bs = block_Set
        self.start = sling
        self.max_big_red_active = 1
        self.side = side
        self.wind_activated = False
        self.wind_button = wind_button

    def activate_player(self):
        self.active = True
        self.current_bird = (self.current_bird+1)%3
        if (len(self.birds)==3):    
            self.birds[self.current_bird].x = self.start[0]
            self.birds[self.current_bird].y = self.start[1]

    def deactivate_player(self):
        self.active = False
    
    def reset(self):

        self.score = 1000
        self.active = False
        self.current_bird = 2
        self.max_big_red_active = 1
        self.bs.reset()
        for bird in self.birds:
            bird.isactive = False
            bird.being_dragged = False
            bird.ready = False
            bird.velocity = [0,0]
        self.wind_activated = False

    def show_birds(self,screen,width,factor_x,factor_y):
        for index in range(len(self.birds)):                         
            screen.blit(self.birds[index].surface, (width/2 - (-1)**self.side*(200 - 40*self.side + 100*index)*factor_x,100*factor_y))
   
    def show_wind_button(self,wind_state):
        if not self.wind_activated:
                    self.wind_button.display()
                    if self.wind_button.is_clicked():
                         self.wind_activated = True
                         wind_state[0] = True
                         wind_state[1] = self.side


