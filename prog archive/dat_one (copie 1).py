import pygame
import math
from math import *
from random import *
from sys import exit 
from pygame.locals import *
from pygame import *

#Musique et son
pygame.mixer.init()
phase1 = pygame.mixer.Sound("sound/music1.ogg")
phase2 = pygame.mixer.Sound("sound/music2.ogg")
pewsound = pygame.mixer.Sound("sound/pew_soud.ogg")
coeurd = pygame.mixer.Sound("sound/coeur_mort.ogg")
coeurh = pygame.mixer.Sound("sound/coeur_hit.ogg")
coeurb = pygame.mixer.Sound("sound/coeur_bris_.ogg")
phase3 = pygame.mixer.Sound("sound/music3.ogg")
#phase1.play(loops=-1, maxtime=0, fade_ms=0)  #A ENLEVER POUR METTRE LA MSC

#déplacement

class perso():
    def __init__(self):
        self.image_perso = pygame.image.load("sprite/perso.png").convert_alpha()
        self.position = self.image_perso.get_rect()
        self.position = self.position.move(600,400)

    def deplacement(self, direction) :   
        if direction == "RIGHT":
            self.position = self.position.move(3,0)
            if self.position.x >= 1150:
                self.position = self.position.move(-3,0)
        if direction == "LEFT":
            self.position = self.position.move(-3,0)
            if self.position.x <= 0:
                self.position = self.position.move(3,0)
        if direction == "UP":
            self.position = self.position.move(0,-3)
            if self.position.y <= 0:
                self.position = self.position.move(0,3)
        if direction == "DOWN":
            self.position = self.position.move(0,3)
            if self.position.y >= 750:
                self.position = self.position.move(0,-3)
        return self.position

class mechant():
    def __init__(self):
        global x
        self.image_mechant = pygame.image.load("sprite/mechant.png").convert_alpha()
        self.pos = self.image_mechant.get_rect()
        self.shoot=0
        self.dirshootx=0
        self.dirshooty=0
        self.vitesse=2
        self.cadre=0
        self.vie=3
        x=0
    def mouvement1(self):
        global x
        if x == 0:
            self.pos = self.pos.move(2,0)
        elif x == 1:
            self.pos = self.pos.move(-2,0)
        if self.pos.x == 0:
            self.pos = self.pos.move(0,50)
            x = 0
        elif self.pos.x == 1100:
            x = 1
            self.pos = self.pos.move(0,50)
        return self.pos
    def mouvement2(self):
        global tirl
        self.shoot+=1
        if self.shoot==100:
                tirl.append(tir())
                self.shoot=0
        if self.pos.y<400:
            self.dirshootx=self.vitesse
            self.dirshooty=self.vitesse          
            self.pos = self.pos.move(0,1)
        elif self.pos.y>=400:
            self.dirshootx=self.vitesse
            self.dirshooty=-self.vitesse
            self.pos = self.pos.move(2,1)
        if self.pos.y>=1099:
            self.dirshootx=self.vitesse
            self.dirshooty=self.vitesse
        elif self.pos.x>565:
            self.dirshootx=-self.vitesse
            self.dirshooty=-self.vitesse
            self.pos = self.pos.move(2,-1)
            self.pos = self.pos.move(-2,-1)
        return self.pos
    
    def mouvement3(self):
        global tirl
        self.shoot+=1
        if self.shoot==100:
                tirl.append(tir())
                self.shoot=0
        if self.pos.y<400:
            self.dirshootx=-self.vitesse
            self.dirshooty=-self.vitesse          
            self.pos = self.pos.move(0,1)
        elif self.pos.y>=400:
            self.dirshootx=-self.vitesse
            self.dirshooty=self.vitesse
            self.pos = self.pos.move(2,1)
        if self.pos.y>=1099:
            self.dirshootx=-self.vitesse
            self.dirshooty=-self.vitesse
        elif self.pos.x>565:
            self.dirshootx=self.vitesse
            self.dirshooty=self.vitesse
            self.pos = self.pos.move(2,-1)
            self.pos = self.pos.move(-2,-1)
        return self.pos
    def mouvement4(self):
        global tirl
        self.shoot=randint(0,100)
        self.shoot+=1
        if self.shoot==100:
                tirl.append(tir())
                self.shoot=0
        if self.pos.y>20:
            self.pos=self.pos.move(0,-3)
            self.dirshooty=0
            if self.pos.x>600:
                self.dirshootx=-self.vitesse
            elif self.pos.x<=600:
                self.dirshootx=self.vitesse
        if self.pos.y<=100:
            self.dirshooty=self.vitesse
            self.dirshootx=0
            if self.pos.x>620:
                self.pos=self.pos.move(-2,0)
            elif self.pos.x<=580:
                self.pos=self.pos.move(2,0)
            else:
                self.pos=self.pos.move(0,-2)
            
        return self.pos

class tir():
    def __init__(self):
        self.image_tir = pygame.image.load("sprite/orb2.png").convert_alpha()
        self.pos = self.image_tir.get_rect()
        self.pos = mechantl[i].pos
        self.pos = self.pos.move(0,24)
        self.zox=mechantl[i].dirshootx
        self.zoy=mechantl[i].dirshooty
        self.speed=1
        self.v=1
 
    def autoshoot(self):
        self.v += self.speed
        x = float(self.v) 
        self.pos = self.pos.move(0-(9.8*self.zox**2)/(2*(81**2)*cos(1.05)**2)+(tan(1.05)*self.zox),0-(9.8*self.zoy**2)/(2*(81**2)*cos(1.05)**2)+(tan(1.05)*self.zoy))
        return self.pos

class pew():
    def __init__(self):
        pew = pygame.image.load("sprite/fire.png").convert_alpha()
        position_pew = pew.get_rect()
        position_pew = position_pew.move(-10000,-10000)
    def brata(self):
        position_pew = position_pew.move(0,-25)


        
#Ouverture de la fenêtre Pygame

pygame.init()
fenetre = pygame.display.set_mode((1200,800))

#pew

##pew = pygame.image.load("sprite/fire.png").convert_alpha()
##position_pew = pew.get_rect()
##position_pew = position_pew.move(-10000,-10000)


#class atribut
###############################################################
hearth=perso()
mechantl=[]
tirl=[]

for i in range(100):
    mechantl.append(mechant())
    mechantl[i].pos=mechantl[i].pos.move(20,400+20*10*i)
for i in range(100,200):
    mechantl.append(mechant())
    mechantl[i].pos=mechantl[i].pos.move(1100,400+20*10*(i-100))
###############################################################
#Chargement et collage du fond

fond = pygame.image.load("sprite/background.jpg").convert()
fenetre.blit(fond, (0,0))

#variable utile

continuer = 1
#j=0
maxlife=20
life=maxlife
cooldown=0

#lifebar
pygame.draw.rect(fond,(255,255,0),(550,770,5*life,25))

font=pygame.font.Font("font/DTM-Sans.otf", 36)
lifescore20=font.render("/ 20",1,(255,255,255))
lifescore=font.render(str(life),1,(255,255,255))

#BOUCLE INFINIE

while continuer == 1:
    ev=event.poll()

##    #pew slow down
##    if j!=0:
##        j=j+1
##    if j==42:
##        j=0
##        position_pew = position_pew.move(-10000,-10000)
##    position_pew = position_pew.move(0,-25)
##
    #pew hitbox
    for i in range(len(pewl)):    
        pew_rect[i]=pygame.Rect(position_pew.x[i]+20,position_pew.y[i],10,50)

    
    hearth_rect=pygame.Rect(hearth.position.x+13,hearth.position.y+13,24,24)
###############################################################
    for i in range(len(mechantl)):
        if mechantl[i] != False:        
            if hearth_rect.colliderect(pygame.Rect(mechantl[i].pos.x,mechantl[i].pos.y,100,100)):
                if cooldown==0:
                    life=life-8
                    pygame.draw.rect(fond,(255,0,0),(550,770,5*(maxlife-life),25))
                    lifescore=font.render(str(life),1,(255,255,255))
                    cooldown=100
                    coeurh.play()
            if mechantl[i].pos.x<-200 or mechantl[i].pos.y<-200 or mechantl[i].pos.x>1400 or mechantl[i].pos.y>1000:
                if mechantl[i].cadre==1:
                    mechantl[i]=False
                    break
            if mechantl[i].cadre==0:
                if mechantl[i].pos.x>-199 and mechantl[i].pos.y>-199 and mechantl[i].pos.x<1399 and mechantl[i].pos.y<999:
                    mechantl[i].cadre=1
            if pew_rect.colliderect(pygame.Rect(mechantl[i].pos.x,mechantl[i].pos.y,100,100)):
                position_pew = position_pew.move(-10000,-10000)
                mechantl[i].vie-=1
                if mechantl[i].vie==0:
                    mechantl[i]=False
                    break
###############################################################
    for i in range(len(tirl)):
        if tirl[i].pos.x<-200 or tirl[i].pos.y<-200 or tirl[i].pos.x>1400 or tirl[i].pos.y>1000:
            #tirl[i].pos.x=randint(-199,1200)
            #tirl[i].pos.y=randint(-199,800)
            del tirl[i]
            break
    for i in range(len(tirl)):
        if hearth_rect.colliderect(pygame.Rect(tirl[i].pos.x,tirl[i].pos.y,50,50)):
            if cooldown==0:
                life=life-4
                pygame.draw.rect(fond,(255,0,0),(550,770,5*(maxlife-life),25))
                lifescore=font.render(str(life),1,(255,255,255))
                cooldown=100
                coeurh.play()
    if life<=0:
        print("You died !")
        coeurb.play()
        time.delay(1000)
        pygame.quit()
        exit()
        raise SystemExit
    if cooldown>0:
        cooldown-=1
        if cooldown % 3:
            hearth.image_perso = pygame.image.load("sprite/perso2.png").convert_alpha()
            pygame.display.update()
        if cooldown % 2:
            hearth.image_perso = pygame.image.load("sprite/perso.png").convert_alpha()
    #interactions
        
    if key.get_pressed()[K_a]:
        if j==0:
            position_pew = hearth.position
            position_pew = position_pew.move(0,-24)
            pewsound.play()
            j+=1
    if key.get_pressed()[K_RIGHT]:
        hearth.position = hearth.deplacement("RIGHT")
    if key.get_pressed()[K_LEFT]:
        hearth.position = hearth.deplacement("LEFT")
    if key.get_pressed()[K_UP]:
        hearth.position = hearth.deplacement("UP")
    if key.get_pressed()[K_DOWN]:
        hearth.position = hearth.deplacement("DOWN")
    if key.get_pressed()[K_ESCAPE]:    
        pygame.quit()
        exit()
        raise SystemExit
    
    #déplacement méchant patern x
###############################################################
    for i in range(100):
        if mechantl[i] != False:
            mechantl[i].pos=mechantl[i].mouvement4()
    for i in range(100,200):
        if mechantl[i] != False:
            mechantl[i].pos=mechantl[i].mouvement4()
###############################################################

    #déplacement tir
    for i in range(len(tirl)):
        tirl[i].pos=tirl[i].autoshoot()
    
    #Re-collage

    fenetre.blit(fond, (0,0))   
    fenetre.blit(hearth.image_perso, hearth.position)
###############################################################
    for i in range(len(mechantl)):
        if mechantl[i] != False:
            fenetre.blit(mechantl[i].image_mechant, mechantl[i].pos)
###############################################################
    for i in range(len(tirl)):
        fenetre.blit(tirl[i].image_tir, tirl[i].pos)
    fenetre.blit(pew, position_pew)
    fenetre.blit(lifescore20, (700+life, 759))
    fenetre.blit(lifescore, (680, 759))
    pygame.display.update()

    #Rafraichissement
    pygame.display.flip()
    pygame.time.delay(5)
    
    if ev.type == pygame.QUIT:
        pygame.quit()
        exit()
        raise SystemExit
