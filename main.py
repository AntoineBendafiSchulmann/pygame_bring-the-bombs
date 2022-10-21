import pygame
import random
from classes.player import Player
from classes.mine import Mine

from math import sqrt

module_charge = pygame.init()
print(module_charge)

ecran = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

loop = True 
generate_mines = True
finded_mine = False 
mines_trouvees = 0

player = Player()



pygame.key.set_repeat(1, 100)

while loop:
    ecran.fill((0, 0, 0))
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                couleur = (107,142,35)
            else:
                couleur = (85,107,47)
            pygame.draw.rect(ecran, couleur, (i * 100, j * 100, 100, 100))

    player.Draw(ecran)

    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            pygame.key.get_repeat() 
            player.Move(event)
            if event.key == pygame.K_ESCAPE:
                loop = False
            if event.type == pygame.QUIT:    
                loop = False
            
            player.Limit()
    
    # MINES
    if generate_mines:
        mines = []
        for m in range(random.randint(1, 3)):#on génère un nombre aléatoire de mines entre deux valeurs au choix 
            mines.append(Mine(random.randint(0, 700), random.randint(0, 700)))
        generate_mines = False

    for mine in mines:
        mine.Draw(ecran)
        # si la distance entre les deux points est inférieure à la somme des rayons des deux cercles on a trouvé une mine 
        d = sqrt((player.x - mine.x)**2 + (player.y - mine.y)**2)
        if d < (player.taille+mine.taille):
            finded_mine = True
            mines.remove(mine)
            mines_trouvees += 1
            print(len(mines))#on print le nombre de mines restantes
            # si on a trouvé toutes les mines  on gagne
            if  len(mines) == 0:
                ecran.fill((0, 0, 0))
                text = font.render("Vous avez gagné !", 1, (255, 255, 255))
                ecran.blit(text, (650, 350))
                pygame.display.flip()
                pygame.time.wait(2000)
                loop = False 

        # afficher le score
        font = pygame.font.Font(None, 36)
        text = font.render("Mines trouvées : " + str(mines_trouvees), 1, (255, 255, 255))
        # on affiche le texte en haut à droite de l'écran
        ecran.blit(text, (1250, 0))

        #timer affiché en haut à droite de l'écran
        temps = pygame.time.get_ticks() / 1000 # get tick renvoie le temps en milisecondes , on divise par 1000 pour avoir le temps en secondes
        text = font.render("Temps écoulé : " + str(temps), 1, (255, 255, 255))
        ecran.blit(text, (1250, 50))

        # défaite
        if temps > 30:
            ecran.fill((0, 0, 0))
            text = font.render("Temps écoulé !", 1, (255, 255, 255))
            ecran.blit(text, (650, 350))
            ecran.blit(pygame.image.load("images/david.png").convert(), (450, 400))
            pygame.display.flip()
            #son
            pygame.mixer.init() 
            pygame.mixer.music.load("sounds/defeat.mp3")
            pygame.mixer.music.play()
            pygame.time.wait(3900)
            loop = False

    # on met à jour l'écran
    pygame.display.flip()

# on vide le cache
pygame.quit()