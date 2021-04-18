import pygame
from math import *
from random import *
from sys import exit 
from pygame.locals import *
from pygame import *
from GIFImage import GIFImage



pygame.init()

######personnage######
class Perso():
    def __init__(self):
        self.image_perso = pygame.image.load("sprite/perso.png").convert_alpha()
        self.position = self.image_perso.get_rect()
        self.position = self.position.move(600,400)

#déplacement#
    def deplacement(self, direction) :   
        if direction == "RIGHT":
            self.position = self.position.move(4,0)
            if self.position.x >= 1150:
                self.position = self.position.move(-4,0)
        if direction == "LEFT":
            self.position = self.position.move(-4,0)
            if self.position.x <= 0:
                self.position = self.position.move(4,0)
        if direction == "UP":
            self.position = self.position.move(0,-4)
            if self.position.y <= 0:
                self.position = self.position.move(0,4)
        if direction == "DOWN":
            self.position = self.position.move(0,4)
            if self.position.y >= 750:
                self.position = self.position.move(0,-4)
        return self.position


######mechant1######    
class Mechant():
    def __init__(self):
        global x
        self.image_mechant = pygame.image.load("sprite/mechant.png").convert_alpha()
        self.pos = self.image_mechant.get_rect()
        self.shoot=0
        self.dirshootx=0
        self.dirshooty=0
        self.vitesse=3
        self.cadre=0
        self.vie=3
        self.tag=1
        x=0
        self.vmov=randint(1,2)

#Space invader ? buggé???
    def mouvement1(self,tirl,mechantl,i,hearthx,hearthy):
        global x
        self.shoot+=1
        if self.shoot==100:
            tirl.append(Tir(mechantl,i,hearthx,hearthy,self.tag))
            self.shoot=0
        if x == 0:
            self.pos = self.pos.move(2,0)
            self.dirshootx=self.vitesse
            self.dirshooty=self.vitesse   
        elif x == 1:
            self.pos = self.pos.move(-2,0)
            self.dirshootx=self.vitesse
            self.dirshooty=self.vitesse   
        if self.pos.x == 0:
            self.pos = self.pos.move(0,50)
            x = 0
        elif self.pos.x == 1100:
            x = 1
            self.pos = self.pos.move(0,50)
        return self.pos

#déplacement coupe
    def mouvement2(self,tirl,mechantl,i,hearthx,hearthy):
        self.shoot=randint(0,100)
        self.shoot+=1
        if self.shoot==100:
                tirl.append(Tir(mechantl,i,hearthx,hearthy,self.tag))
                self.shoot=0
        if self.pos.y<400:
            self.dirshootx=self.vitesse
            self.dirshooty=self.vitesse          
            self.pos = self.pos.move(0,3)
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
    
#déplacement coupe    !!!! à inverser
    def mouvement3(self,tirl,mechantl,i,hearthx,hearthy):
        self.shoot=randint(0,100)
        self.shoot+=1
        if self.shoot==100:
                tirl.append(Tir(mechantl,i,hearthx,hearthy,self.tag))
                self.shoot=0
        if self.pos.y<400:
            self.dirshootx=-self.vitesse
            self.dirshooty=-self.vitesse          
            self.pos = self.pos.move(0,3)
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

#déplacement monté centrale
    def mouvement4(self,tirl,mechantl,i,hearthx,hearthy):
        self.shoot=randint(0,100)
        self.shoot+=1
        if self.shoot==100:
                tirl.append(Tir(mechantl,i,hearthx,hearthy,self.tag))
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
    
#déplacement chandelier
    def mouvement6(self,tirl,mechantl,i,hearthx,hearthy):
        self.shoot=randint(0,50)
        self.shoot+=1
        if self.shoot==50:
                tirl.append(Tir(mechantl,i,hearthx,hearthy,self.tag))
                self.shoot=0
        if self.pos.y<20:
            self.pos=self.pos.move(0,3)
            self.dirshooty=self.vitesse
            if self.pos.x>600:
                self.dirshootx=-self.vitesse
            elif self.pos.x<=600:
                self.dirshootx=self.vitesse
        if self.pos.y>=20:
            self.dirshooty=self.vitesse
            self.dirshootx=0
            if self.pos.x>620:
                self.pos=self.pos.move(-2,0)
            elif self.pos.x<=580:
                self.pos=self.pos.move(2,0)
            else:
                self.pos=self.pos.move(0,2)
        return self.pos

#déplacement vertical
    def mouvement7(self,tirl,mechantl,i,hearthx,hearthy):
        #self.shoot=randint(0,200)
        self.shoot+=1
        if self.shoot==100:
                tirl.append(Tir(mechantl,i,hearthx,hearthy,self.tag))
                self.shoot=0
        self.pos=self.pos.move(0,self.vmov)
        self.dirshootx=0
        self.dirshooty=self.vitesse
        return self.pos

######second mechant de base######
class Mechant2():
    def __init__(self):
        self.image_mechant = pygame.image.load("sprite/mechant3.png").convert_alpha()
        self.pos = self.image_mechant.get_rect()
        self.shoot=0
        self.dirshootx=0
        self.dirshooty=0
        self.vitesse=3
        self.cadre=0
        self.vie=2
        self.tag=2
        self.dude=1

#bricolage#
    def varfdude(self):
        if self.pos.x>600:
            self.dude=1
        else:
            self.dude=0

#déplacement horizontal
    def mouvement5(self,tirl,mechantl,i,hearthx,hearthy):
        self.shoot=randint(0,100)
        self.shoot+=1
        self.dirshootx=0
        self.dirshooty=self.vitesse
        if self.shoot==100:
            tirl.append(Tir(mechantl,i,hearthx,hearthy,self.tag))
            self.shoot=0
        if self.dude==0:
            self.pos=self.pos.move(2,0)
        if self.dude==1:
            self.pos=self.pos.move(-2,0)
        return self.pos

######troisieme mechant######
class Mechant3():
    def __init__(self):
        self.dg= randint(0,1)
        self.image_mechant=pygame.image.load("sprite/mechant2.png").convert_alpha()
        self.pos=self.image_mechant.get_rect()
        self.pos=self.pos.move(self.dg*1100,-100)
        self.cadre=0
        self.vie=2
        self.tag=3
        self.timer=0
        self.x=1
        if self.dg == 1:
            self.x= -self.x
        if self.dg == 1:
            self.image_mechant=pygame.transform.rotate(self.image_mechant,270)
        else:
            self.image_mechant=pygame.transform.rotate(self.image_mechant,90)

#deplacement du troisieme mechant        
    def mouvementX(self,tirl,mechantl,i,hearthx,hearthy,laserlist):
        self.timer+=1
        if self.timer<400:
            if self.pos.y < hearthy:
                self.pos=self.pos.move(0,4)
            if self.pos.y > hearthy:
                self.pos=self.pos.move(0,-4)
        if self.timer>455 and self.timer<500:
            laserlist.append(Laser(self.x,self.pos,laserlist))
        if self.timer>500 and self.timer<545:
            for i in range(len(laserlist)):
                del laserlist[i]
                break
        if self.timer>=505: 
            if self.dg==1:
                self.pos=self.pos.move(4,0)
                self.x=1
            if self.dg==0:
                self.pos=self.pos.move(-4,0)
                self.x=-1
        return self.pos
        
######laser du troisieme mechant######
class Laser():
    def __init__(self,x,m,laserlist):
        self.image = pygame.image.load("sprite/laser.png").convert_alpha()
        self.pos= self.image.get_rect()
        self.pos = m
        if x ==1:
            self.pos = self.pos.move(110,4)
        if x ==-1:
            self.pos = self.pos.move(-290,4)
        self.pos = self.pos.move(x*60*len(laserlist),0)
        
        
######tir des mechant de base######
class Tir():
    def __init__(self,mechantl,i,hearthx,hearthy,tag):
        self.image_tir = pygame.image.load("sprite/orb3.png").convert_alpha()
        self.pos = self.image_tir.get_rect()
        self.pos = mechantl[i].pos
        self.pos = self.pos.move(0,24)
        self.zox=mechantl[i].dirshootx
        self.zoy=mechantl[i].dirshooty
        self.zorandomx=randint(-1,1)*3
        self.zorandomy=randint(-1,1)*3
        if self.zorandomx==0 and self.zorandomy==0:
            self.zorandomy=3
        self.tig=tag

#tir dans une direction donné par la fonction mouvement 
    def autoshoot(self):
        if self.tig==2:
            self.pos = self.pos.move(self.zox,self.zoy)
        if self.tig==1:
            self.pos = self.pos.move(self.zorandomx,self.zorandomy)            
        return self.pos

#tir au hasard
    def shootrandom(self):
        self.pos = self.pos.move(self.zorandomx,self.zorandomy)
        return self.pos

#tete chercheuse buggé    
    def teteChercheuse(self,hearth):
        if self.pos.x < hearth.position.x:
            self.pos = self.pos.move(1,0)
        elif self.pos.x > hearth.position.x:
            self.pos = self.pos.move(-1,0)
        if self.pos.y < hearth.position.y:
            self.pos = self.pos.move(0,1)
        elif self.pos.y > hearth.position.y:
            self.pos = self.pos.move(0,-1)
        return self.pos

######arme du personnage######
class pew():
    def __init__(self,hearth):
        self.pew_image = pygame.image.load("sprite/fire.png").convert_alpha()
        self.pos = self.pew_image.get_rect()
        self.pos = hearth.position
        self.pos = self.pos.move(0,-50)

######BOSS######
class Asriel():
    def __init__(self):
        self.image_asriel=GIFImage("gif/test3.gif")
        self.pos=self.image_asriel.get_rect()
        self.asrielx=270
        self.pos=self.pos.move(self.asrielx,10)
        self.maxlife=1000
        self.life=self.maxlife
        self.timerC=0
        self.dg=randint(0,1)

#mouvement du boss
    def mouvasriel(self):
        self.timerC+=1       
        if self.dg==1:
            if self.timerC>200 and self.timerC<500:
                self.pos=self.pos.move(1,0)
                self.asrielx=self.asrielx+1
            if self.timerC>600 and self.timerC<900:
                self.pos=self.pos.move(-1,0)
                self.asrielx=self.asrielx-1                
        if self.dg==0:
            if self.timerC>200 and self.timerC<500:
                self.pos=self.pos.move(-1,0)
                self.asrielx=self.asrielx-1
            if self.timerC>600 and self.timerC<900:
                self.pos=self.pos.move(1,0)
                self.asrielx=self.asrielx+1
        if self.timerC==1100:
                self.dg=randint(0,1)
                self.timerC=200
        return self.pos

#tir aléatoire du boss
    def tirprincipale(self,bosstirl,asriel):
        x=randint(-3,3)
        y=randint(1,3)
        xx=False
        yy=False    
        if self.timerC%5==1:
            bosstirl.append(couloirtir(x,y,xx,yy,asriel))

 ############################################################à finir
    def tirsecondaire(self,bosstirl,asriel,hx,hy):
        if self.timerC>0:
            x=0
            y=4
            xx=0
            yy=4 
        if self.timerC>=200 and self.timerC<450:     
            x=1
            y=4
            xx=1
            yy=4
        if self.timerC>=450 and self.timerC<700:
            x=0
            y=4
            xx=0
            yy=4
        if self.timerC>=700 and self.timerC<950:
            x=-1
            y=4
            xx=-1
            yy=4
        if self.timerC>=950 and self.timerC<1200:
            x=0
            y=4
            xx=0
            yy=4
##        x=0
##        y=4
##        xx=0
##        yy=4           
        if self.timerC%10==1:
            bosstirl.append(couloirtir(x,y,xx,yy,asriel))
############################################################à finir

############################################################
class couloirtir():
    def __init__(self,x,y,xx,yy,asriel):
        if xx==False and yy==False:
            self.image_tir=pygame.image.load("sprite/AsrielOrb.png").convert_alpha()        
            self.pos=self.image_tir.get_rect()
            self.pos=asriel.pos
            self.dirx=x
            self.diry=y
            self.pos=self.pos.move(300,100)            
        else:
            self.image_tir=pygame.image.load("sprite/orb3.png").convert_alpha()        
            self.pos=self.image_tir.get_rect()
            self.pos=asriel.pos
            if asriel.timerC%20==1:
                self.dirx=x
                self.diry=y
                self.pos=self.pos.move(100,100)
            elif asriel.timerC%10==1:
                self.dirx=xx
                self.diry=yy
                self.pos=self.pos.move(500,100)

##        if asriel.timerC%10==1 and xx!=False:
##            self.dirx=x
##            self.diry=y
##            self.pos=self.pos.move(100,100)
##        elif asriel.timerC%5==1 and xx!=False:
##            self.dirx=xx
##            self.diry=yy
##            self.pos=self.pos.move(100,100)
##
##        if asriel.timerB%10==1 and xx!=False:
##            self.dirx=x
##            self.diry=y
##            self.pos=self.pos.move(500,100)
##        elif asriel.timerB%5==1 and xx!=False:
##            self.dirx=xx
##            self.diry=yy
##            self.pos=self.pos.move(500,100)
        
    def couloirG(self):
        self.pos=self.pos.move(self.dirx,self.diry)
############################################################


######heal######
class Heal():
    def __init__(self):
        self.image = pygame.image.load("sprite/heal.png").convert_alpha()
        self.pos= self.image.get_rect()
        self.pos= self.pos.move(randint(200,800),-100)
    def healkitombe(self):
        self.pos=self.pos.move(0,2)
        return self.pos
