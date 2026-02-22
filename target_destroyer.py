import pygame as pg 
import random as rdm

def target_destroyer():
      pg.init()
      win = pg.display.set_mode((1000, 650))
      pg.display.set_caption("target destroyer")
      icon = pg.image.load("4/1.png")
      icon = pg.transform.scale(icon , (50,50))
      pg.display.set_icon(icon)

      hit = pg.mixer.Sound("4/hit.wav")

      target = pg.image.load("4/1.png")
      target = pg.transform.scale(target , (50,50))
      target2 = pg.image.load("4/2.png")
      target2 = pg.transform.scale(target2 , (50,50))
      target3 = pg.image.load("4/3.png")
      target3 = pg.transform.scale(target3 , (50,50))
      target4 = pg.image.load("4/4.png")
      target4 = pg.transform.scale(target4 , (50,50))
      bg = pg.transform.scale(pg.image.load("4/bg.png"), (1000, 1000))

      font = pg.font.Font("ARLRDBD.TTF", 30)
      font2 = pg.font.Font("ARLRDBD.TTF", 60)

      home_button = pg.transform.scale(pg.image.load("home_button.png"), (50, 50))

      xt = 700
      yt = -100
      xt2 = 200
      yt2 = -300
      xt3 = 700
      yt3 = -300
      xt4 = 400
      yt4 = -350
      p = 0
      pm = 0
      s = 0.01
      s2 = 0.02
      s3 = 0.05
      s4 = 0.07

      score_txt = font.render("Score : "+str(p) + " Score2 : " + str(pm), True, (255, 255, 255))
      spos = score_txt.get_rect()
      spos.center = (150, 20)

      start_txt = font2.render("Start", True, (255, 255, 255))
      stpos = start_txt.get_rect()
      stpos.center = (500, 325)
      stw = start_txt.get_width()
      sth = start_txt.get_height()

      run0 = True 
      run = False 
      go2 = False
      go3 = False
      go4 = False 

      while run0:
            win.blit(bg, (0,0))
            win.blit(start_txt,stpos)
            for event in pg.event.get() :
                        if event.type == pg.QUIT :
                              run0 = False
                        if event.type == pg.MOUSEBUTTONDOWN :
                              xm , ym = event.pos
                              if 500 - stw/2 < xm < 500 + stw/2 and 325 - sth/2 < ym < 325 + sth/2 :
                                    
                                    run = True 
                                    go2 = False
                                    go3 = False
                                    go4 = False
                                    xt = 700
                                    yt = -100
                                    xt2 = 200
                                    yt2 = -300
                                    xt3 = 700
                                    yt3 = -300
                                    xt4 = 400
                                    yt4 = -350
                                    p = 0
                                    pm = 0
                                    s = 0.7
                                    s2 = 1.2
                                    s3 = 2.2
                                    s4 = 2.7
                        if event.type == pg.MOUSEMOTION :
                              xm , ym = event.pos
                              if 500 - stw/2 < xm < 500 + stw/2 and 325 - sth/2 < ym < 325 + sth/2 :
                                    start_txt = font2.render("Start", True, (0, 0, 0))
                              else :
                                    start_txt = font2.render("Start", True, (255, 255, 255))

            pg.display.update()
            
            while run:
                  for event in pg.event.get() :
                        if event.type == pg.QUIT :
                              run = False
                              run0 = False
                        if event.type == pg.KEYDOWN :
                              if event.key == pg.K_p:
                                    pg.mixer.music.stop()
                        if event.type == pg.MOUSEBUTTONDOWN :
                              xm , ym = event.pos
                              
                              if 940 < xm < 990 and 10 < ym < 60:
                                    run = False
                                    start_txt = font2.render("Start", True, (255, 255, 255))
                              if xt < xm < xt+50 and yt < ym < yt+50 :
                                    hit.play()      
                                    yt = -100
                                    xt = rdm.randint(50,900)
                                    p += 1
                                    if p % 5 == 0 :
                                          s += 0.2
                              if xt2 < xm < xt2+50 and yt2 < ym < yt2 +50 :
                                    hit.play()
                                    yt2 = -200
                                    xt2 = rdm.randint(50,900)
                                    p += 2
                                    if p % 7 == 0 :
                                          s2 += 0.2
                              if xt3 < xm < xt3+50 and yt3 < ym < yt3 +50 :
                                    hit.play()
                                    yt3 = -300
                                    xt3 = rdm.randint(50,900)
                                    p += 3
                                    if p % 10 == 0 :
                                          s3 += 0.2
                              if xt4 < xm < xt4+50 and yt4 < ym < yt4 +50 :
                                    hit.play()
                                    yt4 = -350
                                    xt4 = rdm.randint(50,900)
                                    p += 4
                                    if p % 12 == 0 :
                                          s4 += 0.2

                  yt += s
                  if p >= 8 or go2 :
                        yt2 += s2
                        go2 = True 
                  if p >= 20 or go3 :
                        yt3 += s3
                        go3 = True
                  if p >= 35 or go4 :
                        yt4 += s4
                        go4 = True 
                  if yt>750 :
                        pm -= 5
                        yt = -100
                        xt = rdm.randint(50,900)
                  if yt2>750 :
                        pm -= 5
                        yt2 = -200
                        xt2 = rdm.randint(50,900)
                  if yt3>750 :
                        pm -= 5
                        yt3 = -300
                        xt3 = rdm.randint(50,900)
                  if yt4>750 :
                        pm -= 5
                        yt4 = -350
                        xt4 = rdm.randint(50,900)

                  if p + pm < 0 :
                        break 
                  win.blit(bg, (0,0))
                  score_txt = font.render("Score : " + str(p) + " Score2 : " + str(pm), True, (255, 0, 0))
                  win.blit(score_txt, spos)
                  win.blit(target,(xt,yt))
                  win.blit(target2,(xt2,yt2))
                  win.blit(target3,(xt3,yt3))
                  win.blit(target4,(xt4,yt4))
                  win.blit(home_button, (940, 10))
                  pg.display.update()
                  pg.time.Clock().tick(450)
            
            end_txt = font2.render("You Lost, Your Score: " + str(p), True, (255, 255, 255))
            endpos = end_txt.get_rect()
            endpos.center = (500, 325)

            while run :
                  win.blit(bg, (0,0))
                  win.blit(end_txt, endpos)
                  win.blit(home_button, (940, 10))
                  pg.display.update()
                  for event in pg.event.get() :
                        if event.type == pg.QUIT :
                              run = False
                              run0 = False
                        if event.type == pg.MOUSEBUTTONDOWN :
                              xm , ym = event.pos
                              
                              if 940 < xm < 990 and 10 < ym < 60:
                                    run = False
                                    start_txt = font2.render("Start", True, (255, 255, 255))
