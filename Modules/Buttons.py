import pygame

class Button:
    def __init__(self, buttontext: str, pos : tuple, screen : pygame.Surface, buttonImage : pygame.Surface,factor_x=1,factor_y=1,button_desc = None,des_pos = None):
        self.buttontext = buttontext
        self.pos = pos
        self.screen = screen
        self.active = False
        self.buttonImage = pygame.transform.scale(buttonImage,(buttonImage.get_width()*factor_x,buttonImage.get_height()*factor_y))
        self.buttonrect = self.buttonImage.get_rect(center = self.pos)
        self.buttonImageactive=pygame.transform.scale(self.buttonImage, (self.buttonImage.get_width() + 20*factor_x, self.buttonImage.get_height() + 20*factor_y))
        self.buttonactiverect = self.buttonImageactive.get_rect(center = self.pos)
        self.click_sound = pygame.mixer.Sound("Resources/audio/button-click.mp3")
        self.desc = button_desc
        self.des_pos = des_pos


    def display(self):
        if self.buttonrect.collidepoint(pygame.mouse.get_pos()):
            if self.desc is not None:
                self.screen.blit(self.desc,self.des_pos)
            self.screen.blit(self.buttonImageactive, self.buttonactiverect)
        else:
            self.screen.blit(self.buttonImage,self.buttonrect)
        
    def is_clicked(self):
        if (self.buttonrect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_just_pressed()[0]):
            if not self.active:
                self.click_sound.play()
            return True
        return False
    
    def play_button_sound(self):
        self.click_sound.play()


    


    



