import pygame
from math import *
from random import *
from sys import exit 
from pygame.locals import *
from pygame import *
from classe import *
from GIFImage import GIFImage

######volume de base de la musique######
zik=100
sfx=100

##############################
##############################
#########   MENU   ###########
##############################
##############################

######boucle infini######
while True:

######definition de la fenetre######
    pygame.init()
    pygame.mouse.set_visible(False)
    fenetre = pygame.display.set_mode((500,300))
#icon+nom
    icon_32x32 = pygame.image.load("sprite/perso.png").convert_alpha()
    pygame.display.set_icon(icon_32x32)
    pygame.display.set_caption("ShooterTale")
#fond d'ecran
    fond = GIFImage("gif/082.gif")
    
######musique du menu######
    menusound = pygame.mixer.Sound("sound/menu.ogg")
    select = pygame.mixer.Sound("sound/menuselect.wav")
    menusound.set_volume(zik/100)
    select.set_volume(sfx/100)
    menusound.play(loops=-1, maxtime=0, fade_ms=0)

######police d'ecriture + definition des éléments du menu######

    font=pygame.font.Font("font/DTM-Sans.otf", 36)
    
    jouer=font.render("Jouer",1,(255,255,255))
    audio=font.render("Audio",1,(255,255,255))
    quitter=font.render("Quitter",1,(255,255,255))
    musique=font.render("Musique",1,(255,255,255))
    effet=font.render("Effet",1,(255,255,255))
    retour=font.render("Retour",1,(255,255,255))
    musiqueplus=font.render("+",1,(255,255,255))
    effetplus=font.render("+",1,(255,255,255))
    musiquemoins=font.render("-",1,(255,255,255))
    effetmoins=font.render("-",1,(255,255,255))

######variable de base du menu######

    hearth=Perso()  #curseur
    hearth.position.x=370
    hearth.position.y=220   #position curseur
    audiomenu=0    #menu aadio désactivé
    menu_jeu=True    #menu actif

######boucle du menu######
    while menu_jeu==True:
######definiton des evenements######
        ev=event.poll()

        hearth_rect=pygame.Rect(hearth.position.x+22,hearth.position.y,6,2)

######deplacement curseur######
        if key.get_pressed()[K_RIGHT] and hearth.position.x < 448:
            hearth.position = hearth.deplacement("RIGHT")
        if key.get_pressed()[K_LEFT]:
            hearth.position = hearth.deplacement("LEFT")
        if key.get_pressed()[K_UP]:
            hearth.position = hearth.deplacement("UP")
        if key.get_pressed()[K_DOWN] and hearth.position.y < 248:
            hearth.position = hearth.deplacement("DOWN")

#######interactions element du menu#######
        if audiomenu==0:
            if hearth_rect.colliderect(pygame.Rect(330,50,100,36)):
                jouer=font.render("Jouer",1,(255,255,0))
                j=1
            else:
                jouer=font.render("Jouer",1,(255,255,255))
                j=0
            if hearth_rect.colliderect(pygame.Rect(330,100,100,36)):
                audio=font.render("Audio",1,(255,255,0))
                k=1
            else:
                audio=font.render("Audio",1,(255,255,255))
                k=0
            if hearth_rect.colliderect(pygame.Rect(330,150,130,36)):
                quitter=font.render("Quitter",1,(255,255,0))
                q=1
            else:
                quitter=font.render("Quitter",1,(255,255,255))
                q=0
            if key.get_pressed()[K_a]:
                if q==1:
                    select.play()
                    pygame.quit()
                    exit()
                    raise SystemExit
                if k==1:
                    select.play()
                    audiomenu=1
                    hearth.position.x=370
                    hearth.position.y=220
                if j==1:
                    select.play()
                    menusound.set_volume(0)
                    menu_jeu=False

#######interactions du menu audio#######
        if audiomenu==1:
            if hearth_rect.colliderect(pygame.Rect(460,50,36,36)):
                musiqueplus=font.render("+",1,(255,255,0))
                j=1
            elif hearth_rect.colliderect(pygame.Rect(280,50,36,36)):
                musiquemoins=font.render("-",1,(255,255,0))
                j=2
            else:
                musiqueplus=font.render("+",1,(255,255,255))
                musiquemoins=font.render("-",1,(255,255,255))
                j=0
            if hearth_rect.colliderect(pygame.Rect(460,100,36,36)):
                effetplus=font.render("+",1,(255,255,0))
                k=1
            elif hearth_rect.colliderect(pygame.Rect(280,100,36,36)):
                effetmoins=font.render("-",1,(255,255,0))
                k=2
            else:
                effetplus=font.render("+",1,(255,255,255))
                effetmoins=font.render("-",1,(255,255,255))
                k=0
            if hearth_rect.colliderect(pygame.Rect(300,150,130,36)):
                retour=font.render("Retour",1,(255,255,0))
                q=1
            else:
                retour=font.render("Retour",1,(255,255,255))
                q=0
            if key.get_pressed()[K_a]:
                if j==1:
                    if zik<100:
                        zik=zik+1
                        menusound.set_volume(zik/100)
                if j==2:
                    if zik>0:
                        zik=zik-1
                        menusound.set_volume(zik/100)
                if k==1:
                    if sfx<100:
                        sfx=sfx+1
                        select.set_volume(sfx/100)
                        select.play()
                if k==2:
                    if sfx>0:
                        sfx=sfx-1
                        select.set_volume(sfx/100)
                        select.play()
                if q==1:
                    hearth.position.x=370
                    hearth.position.y=220
                    select.play()
                    audiomenu=0

#######quitter#######
        if key.get_pressed()[K_ESCAPE]:    
            pygame.quit()
            exit()
            raise SystemExit
#######gif de fond du menu#######
        fond.render(fenetre, (0 , 0))
        
#######rafraichissement des elements du menu#######
        if audiomenu==0:
            fenetre.blit(jouer,(330, 50))
            fenetre.blit(audio,(330, 100))
            fenetre.blit(quitter,(330, 150))
        if audiomenu==1:
            fenetre.blit(musique,(300, 50))
            fenetre.blit(effet,(300, 100))
            fenetre.blit(musiqueplus,(460, 50))
            fenetre.blit(musiquemoins,(280, 50))
            fenetre.blit(effetplus,(460, 100))
            fenetre.blit(effetmoins,(280, 100))
            fenetre.blit(retour,(300, 150))
            pygame.draw.rect(fenetre,(255,255,0),(280,100,2*zik,3))
            pygame.draw.rect(fenetre,(255,255,0),(280,150,2*sfx,3))
        fenetre.blit(hearth.image_perso, hearth.position)
#update ecran
        pygame.display.flip()
#delay
        pygame.time.delay(10)

##############################
##############################
#########   JEU   ############
##############################
##############################

#######Musique et son du jeu#######
    pygame.mixer.init()
    phase1 = pygame.mixer.Sound("sound/music1.ogg")
    phase2 = pygame.mixer.Sound("sound/music2.ogg")
    phase3 = pygame.mixer.Sound("sound/music3.ogg")
    pewsound = pygame.mixer.Sound("sound/pew_soud.ogg")
    coeurd = pygame.mixer.Sound("sound/coeur_mort.ogg")
    coeurh = pygame.mixer.Sound("sound/coeur_hit.ogg")
    coeurb = pygame.mixer.Sound("sound/coeur_bris_.ogg")
    healsound=pygame.mixer.Sound("sound/heal.wav")
    charge = pygame.mixer.Sound("sound/blasterCharge.wav")
    fire = pygame.mixer.Sound("sound/blasterfire.wav")
    badass = pygame.mixer.Sound("sound/badass.wav")
    phase1.set_volume(zik/100)
    phase2.set_volume(zik/100)
    phase3.set_volume(zik/100)
    pewsound.set_volume(sfx/400)
    healsound.set_volume(sfx/100)
    badass.set_volume(sfx/200)
    coeurd.set_volume(sfx/100)
    coeurh.set_volume(sfx/100)
    coeurb.set_volume(sfx/100)
    charge.set_volume(sfx/100)
    fire.set_volume(sfx/100)
    phase1.play(loops=-1, maxtime=0, fade_ms=0)

#######Ouverture de la fenêtre Pygame du jeu#######
    pygame.init()
    fenetre = pygame.display.set_mode((1200 , 800))
    pygame.display.set_caption("ShooterTale")
    fond2 = GIFImage("gif/test7.gif")

#######creation des listes#######
    mechantl=[]
    tirl=[]
    pewl=[]
    pew_rect=[]
    laserlist=[]
    bosstirl=[]

#######variable=classe()#######
    hearth = Perso()
    asriel=Asriel()

#######Chargement et collage du fond#######
    fond = pygame.image.load("sprite/background.jpg").convert()
    fenetre.blit(fond, (0,0))
    fond2 = GIFImage("gif/test7.gif")
    fond3 = GIFImage("gif/test6.gif")
    gameover1 = GIFImage("gif/test4.gif")
    gameover2 = GIFImage("gif/082.gif")

#######variable utile#######
    maxlife=20#pv, on aurait du les mettres dans la classe
    life=maxlife
    cooldown=0#vitesse de tir
    coolpew=0
    boss=False#boss n'existe pas
    deathc=0#mort
    temps=0#chrono
    jeuu=1#lance le jeu
    heal=False#pas de soin

#######definition de la barre de vie#######
    font=pygame.font.Font("font/DTM-Sans.otf", 36)
    lifescore20=font.render("/ 20",1,(255,255,255))
    lifescore=font.render(str(life),1,(255,255,255))

#######lacement du jeu#######
    while jeuu==1:
#definition des evenements
        ev=event.poll()
#mise à jour chrono à chaque boucle
        temps+=1

######cooldown du tir du personnage######
        if coolpew!=0:
            coolpew-=1
        if coolpew==10:
            coolpew=0

######heal ki tombe######
        if heal !=False:
            heal.healkitombe()
            if heal.pos.y>900 or temps==2:
                heal=False
        if temps%2000==1:
            heal=Heal()
        
#######hitbox#######
            
#defintion de l'hitbox du tir
        for i in range(len(pewl)):
            pewl[i].pos = pewl[i].pos.move(0,-25)
            pew_rect[i]=pygame.Rect(pewl[i].pos.x+20,pewl[i].pos.y,10,50)
#defintion de l'hitbox du personnage            
        hearth_rect=pygame.Rect(hearth.position.x+5,hearth.position.y+25,40,20)
        hearth_rect2=pygame.Rect(hearth.position.x+15,hearth.position.y+15,20,10)
        hearth_rect3=pygame.Rect(hearth.position.x+20,hearth.position.y+10,10,10)

#######collision#######

#colision heal
        if heal!=False:
            if hearth_rect.colliderect(pygame.Rect(heal.pos.x,heal.pos.y,28,26)) or hearth_rect2.colliderect(pygame.Rect(heal.pos.x,heal.pos.y,28,26)) or hearth_rect3.colliderect(pygame.Rect(heal.pos.x,heal.pos.y,28,26)):
                if life>0:                 
                    life = maxlife
                    lifescore=font.render(str(life),1,(255,255,255))
                    healsound.play()
                    heal=False
#colision mechant/personnage
        for i in range(len(mechantl)):
            if mechantl[i] != False and life>0:
                if hearth_rect.colliderect(pygame.Rect(mechantl[i].pos.x+10,mechantl[i].pos.y+10,55,80)) or hearth_rect2.colliderect(pygame.Rect(mechantl[i].pos.x+10,mechantl[i].pos.y+10,55,80)) or hearth_rect3.colliderect(pygame.Rect(mechantl[i].pos.x+10,mechantl[i].pos.y+10,55,80)):
                    if cooldown==0:
                        life=life-6
                        lifescore=font.render(str(life),1,(255,255,255))
                        cooldown=100
                        coeurh.play()
#destruction des mechant hors de l'ecran
                if mechantl[i].pos.x<-200 or mechantl[i].pos.y<-200 or mechantl[i].pos.x>1400 or mechantl[i].pos.y>1000:
                    if mechantl[i].cadre==1:
                        mechantl[i]=False
                        break
                if mechantl[i].cadre==0:
                    if mechantl[i].pos.x>-199 and mechantl[i].pos.y>-199 and mechantl[i].pos.x<1399 and mechantl[i].pos.y<999:
                        mechantl[i].cadre=1
#colision tir du personnage/mechant
                for j in range(len(pewl)):
                    if pew_rect[j].colliderect(pygame.Rect(mechantl[i].pos.x,mechantl[i].pos.y,100,100)):
                        del pewl[j]
                        mechantl[i].vie-=1
                        if mechantl[i].vie==0:
                            coeurb.play()
                            mechantl[i]=False
                        break
#colision tir des mechant /personnage
        for i in range(len(tirl)):
            if hearth_rect.colliderect(pygame.Rect(tirl[i].pos.x+5,tirl[i].pos.y+5,40,40)) or hearth_rect2.colliderect(pygame.Rect(tirl[i].pos.x+5,tirl[i].pos.y+5,40,40)) or hearth_rect3.colliderect(pygame.Rect(tirl[i].pos.x+5,tirl[i].pos.y+5,40,40)):
                if cooldown==0 and life>0:
                    life = life - 4
                    lifescore=font.render(str(life),1,(255,255,255))
                    cooldown=100
                    coeurh.play()
#colision si le boss existe
        if boss==True:
#colision attaque du boss/personnage
            for i in range(len(bosstirl)):
                if hearth_rect.colliderect(pygame.Rect(bosstirl[i].pos.x+5,bosstirl[i].pos.y+5,40,40)) or hearth_rect2.colliderect(pygame.Rect(bosstirl[i].pos.x+5,bosstirl[i].pos.y+5,40,40)) or hearth_rect3.colliderect(pygame.Rect(bosstirl[i].pos.x+5,bosstirl[i].pos.y+5,40,40)):
                    if cooldown==0 and life>0:
                        life = life - 4
                        lifescore=font.render(str(life),1,(255,255,255))
                        cooldown=100
                        coeurh.play()
#colision laser/personnage
            for i in range(len(laserlist)):
                if hearth_rect.colliderect(pygame.Rect(laserlist[i].pos.x+5,laserlist[i].pos.y+10,250,40)) or hearth_rect2.colliderect(pygame.Rect(laserlist[i].pos.x+5,laserlist[i].pos.y+10,250,40)) or hearth_rect3.colliderect(pygame.Rect(laserlist[i].pos.x+5,laserlist[i].pos.y+10,250,40)):
                    if cooldown==0 and life>0:
                        life = life - 10
                        lifescore=font.render(str(life),1,(255,255,255))
                        cooldown=100
                        coeurh.play()

                    
######destruction des tirs hors de l'ecran######
        for i in range(len(tirl)):
            if tirl[i].pos.x<-200 or tirl[i].pos.y<-200 or tirl[i].pos.x>1400 or tirl[i].pos.y>1000:
#mod armagedon#
                #tirl[i].pos.x=randint(-199,1200)
                #tirl[i].pos.y=randint(-199,800)
                del tirl[i]
                break
        for i in range(len(pewl)):
            if pewl[i].pos.x<-200 or pewl[i].pos.y<-200 or pewl[i].pos.x>1400 or pewl[i].pos.y>1000:
#mod facile#
                #pewl[i].pos.x=randint(-199,1200)
                #pewl[i].pos.y=randint(-199,800)
                del pewl[i]
                break
            
######déplacement des tirs du personnage######
        for i in range(len(tirl)):
            tirl[i].pos=tirl[i].autoshoot()


######mort du personnage######
        if life<=0:
            deathc+=1
            if deathc==1:
                phase1.set_volume(0)
                phase2.set_volume(0)
                phase3.set_volume(0)
                pewsound.set_volume(0)
                coeurd.set_volume(0)
                coeurh.set_volume(0)
                coeurb.set_volume(sfx/100)
            if deathc==40:
                time.delay(50)
            if deathc==128:
                coeurb.play()
            fenetre.fill([0,0,0])
            pygame.time.delay(5)
            if deathc<220:
                gameover1.render(fenetre, (hearth.position.x-275, hearth.position.y-200))
            if deathc>=300:
                jeuu=0
                menuu=1

######temps d'invincibilite######
        if cooldown>0:
            cooldown-=1
            if cooldown % 5:
                hearth.image_perso = pygame.image.load("sprite/perso2.png").convert_alpha()
                pygame.display.update()
            if cooldown % 4:
                hearth.image_perso = pygame.image.load("sprite/perso.png").convert_alpha()

######execution des actions du boss si le boss existe######
        if boss==True:
            asriel.pos=asriel.mouvasriel()
            asriel.tirprincipale(bosstirl,asriel)
            asriel.tirsecondaire(bosstirl,asriel,hearth.position.x,hearth.position.y)
            for j in range(len(pewl)):
                if pew_rect[j].colliderect(pygame.Rect(asriel.asrielx+240,10,165,237)):
                    del pewl[j]
                    asriel.life-=1
                    break
            for i in range(len(bosstirl)):
                bosstirl[i].couloirG()
                if bosstirl[i].pos.x<-200 or bosstirl[i].pos.y<-200 or bosstirl[i].pos.x>1400 or bosstirl[i].pos.y>1000:
                    del bosstirl[i]
                    break

######INTERACTION######
        if life>0:
#tir du personnage
            if key.get_pressed()[K_a]:
                if coolpew==0:
                    coolpew=20
                    pewsound.play()
                    pewl.append(pew(hearth))
                    pew_rect.append(True)

#deplacement du personnage
            if key.get_pressed()[K_RIGHT]:
                hearth.position = hearth.deplacement("RIGHT")
            if key.get_pressed()[K_LEFT]:
                hearth.position = hearth.deplacement("LEFT")
            if key.get_pressed()[K_UP]:
                hearth.position = hearth.deplacement("UP")
                if hearth.position.y <=270 and boss == True:
                    hearth.position = hearth.deplacement("DOWN")
            if key.get_pressed()[K_DOWN]:
                hearth.position = hearth.deplacement("DOWN")

######menu pause######
            if key.get_pressed()[K_ESCAPE]:
                pygame.mixer.pause()
                quiit=0           
                while quiit==0:
#affichage menu pause
                    ev=event.poll()
                    fenetre.blit(font.render("Quitter?",1,(255,255,255)), (520, 200))
                    fenetre.blit(font.render("[Y] Oui",1,(255,255,255)), (365, 400))
                    fenetre.blit(font.render("[N] Non",1,(255,255,255)), (520, 400))
                    fenetre.blit(font.render("[R] Menu" , 1 , (255 , 255 , 255)) , (675 , 400))
                    pygame.display.update()
#interaction menu pause
                    if key.get_pressed()[K_y]:
                        select.play()
                        pygame.quit()
                        exit()
                        raise SystemExit
                    if key.get_pressed()[K_n]:
                        select.play()
                        if boss==False:
                            pygame.mixer.unpause()
                            quiit=1
                        if boss==True:
                            phase3.play(loops=-1, maxtime=0, fade_ms=0)
                            quiit=1
                    if key.get_pressed()[K_r]:
                        quiit=1
                        select.play()
                        jeuu=0
                        menu_jeu=1

######LEVEL######
        if boss == False:
            if temps>100 and temps%30==1 and temps <20000: 
                mechantl.append(Mechant())
                mechantl[len(mechantl)-1].pos=mechantl[len(mechantl)-1].pos.move(randint(0,1100),-100)
            if temps>100 and temps%50==1 and temps%100!=1 and temps <20000:
                mechantl.append(Mechant2())
                mechantl[len(mechantl)-1].pos=mechantl[len(mechantl)-1].pos.move(-100,randint(0,300))
                mechantl[len(mechantl)-1].varfdude()
            if temps>100 and (temps+25)%100==1 and temps <20000:
                mechantl.append(Mechant2())
                mechantl[len(mechantl)-1].pos=mechantl[len(mechantl)-1].pos.move(1300,randint(0,300))
                mechantl[len(mechantl)-1].varfdude()
            if temps>100:
                for i in range(len(mechantl)):
                    if mechantl[i] != False:
                        if mechantl[i].tag == 1:
                            mechantl[i].pos=mechantl[i].mouvement7(tirl,mechantl,i,hearth.position.x,hearth.position.y)
                        if mechantl[i].tag == 2:
                            mechantl[i].pos=mechantl[i].mouvement5(tirl,mechantl,i,hearth.position.x,hearth.position.y)

######BOSS######
        if temps==1000 and boss == False and life>0:
            pygame.mixer.pause()
            ######Animation d'apparition#####
            Nani=0
            while Nani<2000:
                Nani+=1
                if Nani>1 and Nani <20:
                    fenetre.fill((255,255,255))
                if Nani==20:
                    fenetre.fill((0,0,0))
                    asriel.image_asriel.render(fenetre, (asriel.asrielx,10))
                    fond3.render(fenetre, (0, 270))
                    fond3.render(fenetre, (480, 270))
                    fond3.render(fenetre, (960, 270))
                    fenetre.blit(hearth.image_perso,hearth.position)
                if Nani>100:
                    fenetre.blit(font.render("B",1,(255,255,255)), ( 500,500))
                if Nani==100:
                    badass.stop()
                    badass.play()
                if Nani>180:
                    fenetre.blit(font.render("o",1,(255,255,255)), ( 520,500))
                if Nani==180:
                    badass.stop()
                    badass.play()
                if Nani>260:
                    fenetre.blit(font.render("s",1,(255,255,255)), ( 540,500))
                if Nani==260:
                    badass.stop()
                    badass.play()
                if Nani>340:
                    fenetre.blit(font.render("s",1,(255,255,255)), ( 560,500))
                if Nani==340:
                    badass.stop()
                    badass.play()
                if Nani>420:
                    fenetre.blit(font.render(":",1,(255,255,255)), ( 580,500))
                if Nani==420:
                    badass.stop()
                    badass.play()
                if Nani>700:
                    fenetre.blit(font.render("A",1,(255,255,255)), ( 600,500))
                if Nani==700:
                    badass.stop()
                    badass.play()
                if Nani>780:
                    fenetre.blit(font.render("S",1,(255,255,255)), (620,500))
                if Nani==780:
                    badass.stop()
                    badass.play()
                if Nani>860:
                    fenetre.blit(font.render("R",1,(255,255,255)), ( 640,500))
                if Nani==860:
                    badass.stop()
                    badass.play()
                if Nani>940:
                    fenetre.blit(font.render("I",1,(255,255,255)), ( 660,500))
                if Nani==940:
                    badass.stop()
                    badass.play()
                if Nani>1020:
                    fenetre.blit(font.render("E",1,(255,255,255)), ( 680,500))
                if Nani==1020:
                    badass.stop()
                    badass.play()
                if Nani>1100:
                    fenetre.blit(font.render("L",1,(255,255,255)), ( 700,500))
                if Nani==1000:
                    badass.stop()
                    badass.play()
                pygame.display.update()
            phase3.play(loops=-1, maxtime=0, fade_ms=0)
            tirl=[]
            mechantl=[]
            boss=True
            if hearth.position.y <= 270:
                hearth.position = hearth.position.move(0,270)
            fond=pygame.image.load("sprite/background2.jpg").convert()
        if boss==True and temps%400==1:
            mechantl.append(Mechant3())
        if boss==True:
            for i in range(len(mechantl)):
                if mechantl[i]!=False:
                    mechantl[i].mouvementX(tirl,mechantl,i,hearth.position.x,hearth.position.y,laserlist)
                    if mechantl[i].timer==350:
                        charge.play()
                    if mechantl[i].timer==410:
                        fire.play()
######Re-collage######
        if life>0:
            fenetre.blit(fond, (0,0))
#si boss n'existe pas
            if boss==False:
                fond2.render(fenetre, (0, 0))
                fond2.render(fenetre, (0,200))
                fond2.render(fenetre, (200, 0))
                fond2.render(fenetre, (300, 300))
                fond2.render(fenetre, (600, 0))
                fond2.render(fenetre, (600, 300))
#si boss existe
            if boss==True:
                asriel.image_asriel.render(fenetre, (asriel.asrielx,10))
                fond3.render(fenetre, (0, 270))
                fond3.render(fenetre, (480, 270))
                fond3.render(fenetre, (960, 270))
                lifescore2=font.render(str(life),1,(255,255,255))
                pygame.draw.rect(fenetre,(255,255,255),(1100,10,25,0.2*asriel.maxlife))
                pygame.draw.rect(fenetre,(255,0,0),(1100,10,25,0.2*(asriel.maxlife-asriel.life)))
                for i in range(len(laserlist)):
                    fenetre.blit(laserlist[i].image,laserlist[i].pos)
                for i in range(len(bosstirl)):
                    fenetre.blit(bosstirl[i].image_tir,bosstirl[i].pos)
#independant
            if heal !=False:
                fenetre.blit(heal.image,heal.pos)
            fenetre.blit(hearth.image_perso, hearth.position)
            for i in range(len(pewl)):
                fenetre.blit(pewl[i].pew_image, pewl[i].pos)
            for i in range(len(tirl)):
                fenetre.blit(tirl[i].image_tir, tirl[i].pos)
            for i in range(len(mechantl)):
                if mechantl[i] != False:
                    fenetre.blit(mechantl[i].image_mechant, mechantl[i].pos)
            pygame.draw.rect(fenetre,(255,255,0),(550,770,5*maxlife,25))
            pygame.draw.rect(fenetre,(255,0,0),(550,770,5*(maxlife-life),25))
            fenetre.blit(lifescore20, (720, 759))
            fenetre.blit(lifescore, (680, 759))
            fenetre.blit(font.render(str(temps),1,(255,255,255)), (175, 759))
            fenetre.blit(font.render("score:",1,(255,255,255)), (50, 759))
            pygame.display.update()

#Rafraichissement    
        pygame.display.flip()
        pygame.time.delay(5)

######bouton quitter######
        if ev.type == pygame.QUIT:
            pygame.quit()
            exit()
            raise SystemExit
        #print(temps)
