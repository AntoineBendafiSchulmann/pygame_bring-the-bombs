from operator import ge
import pygame

class Player:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.sprite = 0
        self.taille = 10
    def Draw(self,ecran):
        self.sprite  = pygame.draw.circle(ecran, (255, 0, 0), (self.x  , self.y), self.taille)
        #self.sprite = pygame.image.load("images/goomba.png").convert_alpha()
        #self.sprite = pygame.transform.scale(self.sprite, (self.taille, self.taille))
        #ecran.blit(self.sprite, (self.x, self.y))

            
    #deplacement du joueur en fonction des touches
    def Move(self, event):
        if event.key == pygame.K_LEFT:
            self.x -= 10
        if event.key == pygame.K_RIGHT:
            self.x += 10
        if event.key == pygame.K_UP:
            self.y -= 10
        if event.key == pygame.K_DOWN:
            self.y += 10

    #limiter le joueur dans le damier
    def Limit(self):
        if self.x < 0:
            self.x = 0
        if self.x > 800:
            self.x = 800
        if self.y < 0:
            self.y = 0
        if self.y > 800:
            self.y = 800
