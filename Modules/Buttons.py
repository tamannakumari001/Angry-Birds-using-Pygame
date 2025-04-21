import pygame

class Button:
    def __init__(self, buttontext: str, pos : tuple, screen : pygame.Surface, buttonImage : pygame.Surface,factor_x=1,factor_y=1):
        self.buttontext = buttontext
        self.pos = pos
        self.screen = screen
        self.active = False
        self.buttonImage = pygame.transform.scale(buttonImage,(buttonImage.get_width()*factor_x,buttonImage.get_height()*factor_y))
        self.buttonrect = self.buttonImage.get_rect(center = self.pos)
        self.buttonImageactive=pygame.transform.scale(self.buttonImage, (self.buttonImage.get_width() + 20*factor_x, self.buttonImage.get_height() + 20*factor_y))
        self.buttonactiverect = self.buttonImageactive.get_rect(center = self.pos)

    def display(self):
        if self.buttonrect.collidepoint(pygame.mouse.get_pos()):
            self.screen.blit(self.buttonImageactive, self.buttonactiverect)
        else:
            self.screen.blit(self.buttonImage,self.buttonrect)
        
    def is_clicked(self):
        if (self.buttonrect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_just_pressed()[0]):
            return True
        return False
    
    class MainMenu:
        pass

    



