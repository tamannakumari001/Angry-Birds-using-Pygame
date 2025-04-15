import pygame

class Button:
    def __init__(self, buttontext: str, pos : tuple, screen : pygame.Surface, buttonImage : pygame.Surface):
        self.buttontext = buttontext
        self.pos = pos
        self.screen = screen
        self.active = False
        self.buttonrect = buttonImage.get_rect(center = self.pos)
        self.buttonImage = buttonImage

    def display(self):
        self.screen.blit(self.buttonImage, self.buttonrect)
        
    def is_clicked(self):
        if (self.buttonrect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]):
            return True
        return False
    



