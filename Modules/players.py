from Modules import birds,blocks

class player:
    def __init__(self,name,block_Set: blocks.block_set,sling):
        self.name = name
        self.birds = []
        self.score = 20
        self.active = False
        self.current_bird = 2
        self.bs = block_Set
        self.start = sling

    def activate_player(self):
        self.active = True
        self.current_bird = (self.current_bird+1)%3
        if (len(self.birds)==3):    
            self.birds[self.current_bird].x = self.start[0]
            self.birds[self.current_bird].y = self.start[1]

    def deactivate_player(self):
        self.active = False


