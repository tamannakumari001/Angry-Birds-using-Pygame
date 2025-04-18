import pygame

class Button:
    def __init__(self, buttontext: str, pos : tuple, screen : pygame.Surface, buttonImage : pygame.Surface):
        self.buttontext = buttontext
        self.pos = pos
        self.screen = screen
        self.active = False
        self.buttonrect = buttonImage.get_rect(center = self.pos)
        self.buttonImage = buttonImage
        self.buttonImageactive=pygame.transform.scale(self.buttonImage, (self.buttonImage.get_width() + 20, self.buttonImage.get_height() + 20))
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

    



