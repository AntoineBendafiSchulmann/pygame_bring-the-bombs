import pygame

class Mine:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.sprite = 0
        self.taille = 10
    def Draw(self,ecran):
        self.sprite  = pygame.draw.circle(ecran, (0, 0, 255), (self.x  , self.y), self.taille)
        #self.sprite = pygame.image.load("images/bomb.png").convert_alpha()
        #self.sprite = pygame.transform.scale(self.sprite, (self.taille, self.taille ))
        #ecran.blit(self.sprite, (self.x, self.y))
    

    