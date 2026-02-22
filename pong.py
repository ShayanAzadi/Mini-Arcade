import pygame as pg
pg.init()

def pong():
      win = pg.display.set_mode((1000,700))
      pg.display.set_caption("pong")
      icon = pg.image.load("1/ball.png")

      home_button = pg.transform.scale(pg.image.load("home_button.png"), (50, 50))

      pg.mixer.init()
      hit = pg.mixer.Sound("1/hit.wav")
      scoring = pg.mixer.Sound("1/scoring.wav")

      pg.display.set_icon(icon)
      bg = pg.image.load("1/field.png")
      bg = pg.transform.scale(bg , (1000,700))

      ball = pg.transform.scale(icon, (38,40))
      xb = 500
      yb = 350
      sxb = 18
      syb = 17
      blue = pg.image.load("1/blue.png")
      blue = pg.transform.scale(blue , (150,30))
      xbl = 425
      ybl = 650


      red = pg.image.load("1/red.png")
      red = pg.transform.scale(red , (150,30))
      xr = 425
      yr = 20


      sp = 18
      pr = 0
      pb = 0

      font = pg.font.Font("ARLRDBD.TTF", 30)
      font2 = pg.font.Font("ARLRDBD.TTF", 60)
      start = font2.render('Start' , True , (0,0,255))
      spos = start.get_rect()
      spos.center = (500, 350)

      hs = start.get_height()
      ws = start.get_width()
      run = False 
      run0 = True


      rightr = False
      leftr = False
      rightb = False
      leftb = False
      while run0 :
            win.blit(bg,(0,0))
            win.blit(start,spos)
            for event in pg.event.get() :
                  if event.type == pg.QUIT :
                        run0 = False
                  if event.type == pg.KEYDOWN:
                        if event.key == pg.K_p:
                              pg.mixer.music.stop()
                  if event.type == pg.MOUSEMOTION:
                        xm , ym = event.pos
                        if 500 - ws/2 < xm < 500 + ws/2 and 350 - hs/2 < ym < 350 + hs/2:
                              start = font2.render('Start' , True , (255,0,0))
                        else:
                              start = font2.render('Start' , True , (0,0,255))
                  
                  if event.type == pg.MOUSEBUTTONDOWN :
                        xm , ym = event.pos
                  
                        if 500 - ws/2 < xm < 500 + ws/2 and 350 - hs/2 < ym < 350 + hs/2:
                              run = True
                              pb = pr = 0
                              xr = 425
                              yr = 20
                              xbl = 425
                              ybl = 650
                              xb = 500
                              yb = 350
            

            pg.display.update()                
            while run :
                  for event in pg.event.get() :
                        if event.type == pg.QUIT :
                              run = False
                              run0 = False
                              
                        if event.type == pg.MOUSEBUTTONDOWN:
                              xm, ym = event.pos

                              if 10 < xm < 60 and 325 < ym < 375:
                                    run = False
                                    start = font2.render('Start' , True , (0,0,255))
                        if event.type == pg.KEYDOWN :
                              if event.key == pg.K_p:
                                    pg.mixer.music.stop()
                              if event.key == pg.K_RIGHT:
                                    rightr = True
                              if event.key == pg.K_LEFT:
                                    leftr = True
                              if event.key == pg.K_d:
                                    rightb = True
                              if event.key == pg.K_a:
                                    leftb = True
                              if event.key == pg.K_m:
                                    pg.mixer.music.stop()
                        if event.type == pg.KEYUP:
                              if event.key == pg.K_RIGHT:
                                    rightr = False
                              if event.key == pg.K_LEFT:
                                    leftr = False
                              if event.key == pg.K_d:
                                    rightb = False
                              if event.key == pg.K_a:
                                    leftb = False
                              
                  
                  if rightr and xr < 1000-160 :
                        xr += sp
                  if leftr and xr > 10:
                        xr -= sp
                  if rightb and xbl < 1000-160 :
                        xbl += sp
                  if leftb and xbl > 10:
                        xbl -= sp

                  win.blit(bg,(0,0))
                  win.blit(ball,(xb-20,yb-20))
                  win.blit(red,(xr,yr))
                  win.blit(blue,(xbl,ybl))


                  xb += sxb
                  yb += syb
                  if (xbl < xb < xbl + 150 or xbl < xb + 38 < xbl + 150) and (ybl <= yb + 40):
                        syb = -syb
                        hit.play()
                  if (xr < xb < xr + 150 or xr < xb + 38 < xr + 150) and (yb <= yr + 45):
                        syb = -syb
                        hit.play()
                  if xb >= 970 or xb <= 30 :
                        sxb *= -1
                        hit.play()


                  if yb >= 695 :
                        scoring.play()
                        pr += 1
                        xb = 500-20
                        yb = 350-20
                        syb*= -1
                        if pr%2 == 0 :
                              sxb *= -1
                        
                  if yb <= 5 :
                        scoring.play()
                        pb += 1
                        xb = 500-20
                        yb = 350-20
                        syb*= -1
                        if pb%2 == 0 :
                              sxb *= -1
                              
                  if pr == 10 or pb == 10 :
                        break
                  
                        
                  
                  textr = font.render(str(pr), True , (255,0,0))
                  textb = font.render(str(pb), True , (0,0,255))
                  text_ = font.render("-", True , (255,255,255))
                  win.blit(textr,(30,60))
                  win.blit(text_,(50,60))
                  win.blit(textb,(65,60))
                  win.blit(home_button, (10, 325))
                        
                  
                  pg.time.Clock().tick(40)
                  
                  pg.display.update()

            a = 'red'
            color = (255,0,0)
            if pb == 10 :
                  a = 'blue'
                  color = (0,0,255)
            winning = font2.render('Player '+a+' has won the game' , True , color)
            d = winning.get_rect()
            d.center = (500, 350)
            while run :
                  for event in pg.event.get() :
                        if event.type == pg.QUIT :
                              run = False
                              run0 = False
                        if event.type == pg.MOUSEBUTTONDOWN:
                              xm, ym = event.pos

                              if 10 < xm < 60 and 10 < ym < 60:
                                    run = False
                                    start = font2.render('Start' , True , (0,0,255))
                  
                  win.blit(bg,(0,0))
                  win.blit(home_button, (10, 10))
                  win.blit(winning,d)
                  pg.display.update()
