import pygame as pg, time

def wrestling():
      pg.init()
      win = pg.display.set_mode((1000,700))
      pw = 80
      ph = 120
      sp = 3
      x1 = 600
      y1 = 275
      x2 = 300
      y2 = 275

      score_red = 0
      score_blue = 0

      home_button = pg.transform.scale(pg.image.load("home_button.png"), (50, 50))

      pg.display.set_caption("wrestling")
      icon = pg.image.load("11/p1.png")
      pg.display.set_icon(icon)

      whistle = pg.mixer.Sound("11/whistle.mp3")

      boom = pg.image.load("11/boom.png")
      boom = pg.transform.scale(boom, (80, 80))
      font = pg.font.Font("ARLRDBD.ttf", 80)
      font2 = pg.font.Font("ARLRDBD.ttf", 50)
      font3 = pg.font.Font("ARLRDBD.ttf", 20)
      start_txt = font.render("Start", True, (255, 255, 255))
      height_start = start_txt.get_height()
      width_start = start_txt.get_width()
      stpos = start_txt.get_rect()
      stpos.center = (500, 350)
      bg = pg.image.load("11/bg.png")
      bg = pg.transform.scale(bg,(1000,700))
      p1 = pg.image.load("11/p1.png")
      p1 = pg.transform.scale(p1,(80,120))
      p2 = pg.image.load("11/p2.png")
      p2 = pg.transform.scale(p2,(80,120))

      right1 = False
      left1 = False
      up1 = False
      down1 = False
      winer = False

      power1 = 0
      power2 = 0

      right2 = False
      left2 = False
      up2 = False
      down2 = False
      run = False
      run0 = True
      flag_dead = False

      while run0:
            for event in pg.event.get():
                  if event.type == pg.QUIT:
                        run0= False
                  if event.type == pg.KEYDOWN:
                        if event.key == pg.K_p:
                              pg.mixer.music.stop()
                  if event.type == pg.MOUSEBUTTONDOWN :
                        xm, ym = event.pos
                  
                        if 500 - width_start/2 < xm < 500 + width_start/2 and 350 - height_start/2 < ym < 350 + height_start/2:
                              run = True
                              sp = 2
                              score_blue = score_red = 0
                              x1 = 600
                              x2 = 300
                              y1 = y2 = 275
                              power1 = power2 = 0
                              winer = False
                              right1 = right2 = False
                              left1 = left2 = False
                              up1 = up2 = False
                              down1 = down2 = False

                  if event.type == pg.MOUSEMOTION :
                        xm, ym = event.pos
                  
                        if 500 - width_start/2 < xm < 500 + width_start/2 and 350 - height_start/2 < ym < 350 + height_start/2:
                              start_txt = font.render("Start", True, (0, 0, 0))
                        else:
                              start_txt = font.render("Start", True, (255, 255, 255))


            win.blit(bg, (0, 0))
            win.blit(start_txt, stpos)
            pg.display.update()
            while run:
                  for event in pg.event.get():
                        if event.type == pg.QUIT:
                              run = False
                              run0 = False
                        if event.type == pg.MOUSEBUTTONDOWN :
                              xm , ym = event.pos
                              
                              if 940 < xm < 990 and 640 < ym < 690:
                                    run = False
                                    start_txt = font.render("Start", True, (255, 255, 255))
                        if event.type == pg.KEYDOWN:
                              if event.key == pg.K_q:
                                    power2 += 1
                              if event.key == pg.K_o:
                                    power1 += 1
                              if event.key == pg.K_RIGHT:
                                    right1 = True
                              if event.key == pg.K_LEFT:
                                    left1 = True
                              if event.key == pg.K_UP:
                                    up1 = True
                              if event.key == pg.K_DOWN:
                                    down1 = True
                              if event.key == pg.K_d:
                                    right2 = True
                              if event.key == pg.K_a:
                                    left2 = True
                              if event.key == pg.K_w:
                                    up2 = True
                              if event.key == pg.K_s:
                                    down2 = True
                              if event.key == pg.K_p:
                                    pg.mixer.music.stop()
                        if event.type == pg.KEYUP:
                              if event.key == pg.K_RIGHT:
                                    right1 = False
                              if event.key == pg.K_LEFT:
                                    left1 = False
                              if event.key == pg.K_UP:
                                    up1 = False
                              if event.key == pg.K_DOWN:
                                    down1 = False
                              if event.key == pg.K_d:
                                    right2 = False
                              if event.key == pg.K_a:
                                    left2 = False
                              if event.key == pg.K_w:
                                    up2 = False
                              if event.key == pg.K_s:
                                    down2 = False
                                    
                  
                  if right1:
                        x1 += sp
                  if left1:
                        x1 -= sp
                  if up1 :
                        y1 -= sp
                  if down1:
                        y1 += sp
                  if right2:
                        x2 += sp
                  if left2:
                        x2 -= sp
                  if up2 :
                        y2 -= sp
                  if down2:
                        y2 += sp

                  if x1 < 0 or x1 + pw > 1000 or y1 < 0 or y1 + ph > 700:
                        score_blue += 1
                        flag_dead = True
                        m = (x1, y1)

                  if x2 < 0 or x2 + pw > 1000 or y2 < 0 or y2 + ph > 700:
                        flag_dead = True
                        score_red += 1
                        m = (x2, y2)
                  
                  
                  if (x1 <= x2 <= x1 + pw or x1 <= x2 + pw <= x1 + pw) and (y1 <= y2 <= y1 + ph or y1 <= y2 + ph <= y1 + ph) and power1 > power2:
                        score_red += 1
                        flag_dead = True
                        m = (x2, y2)

                  if (x2 <= x1 <= x2 + pw or x2 <= x1 + pw <= x2 + pw) and (y2 <= y1 <= y2 + ph or y2 <= y1 + ph <= y2 + ph) and power2 > power1:
                        score_blue += 1
                        flag_dead = True
                        m = (x1, y1)
                        
                  txt_score = font2.render("Blue " + str(score_blue) + " - " + str(score_red) + " Red", True , (255, 255, 255))
                  p2_tx = font3.render("Power Blue " + str(power2), True, (0, 0, 255))
                  p1_tx = font3.render(str(power1) + " Power Red" , True, (255, 0, 0))
                  p1_tx_wi = p1_tx.get_width()
                  sc_pos = txt_score.get_rect()
                  sc_pos.center = (500, 40)
                  sp += 0.04
                  win.blit(bg,(0,0))
                  win.blit(p1,(x1,y1))
                  win.blit(p2,(x2,y2))
                  win.blit(p2_tx, (10, 10))
                  win.blit(p1_tx, (990 - p1_tx_wi, 10))
                  win.blit(txt_score, sc_pos)
                  win.blit(home_button, (940, 640))
                  pg.display.update()
                  pg.time.Clock().tick(60)

                  if flag_dead:
                        
                        win.blit(boom, m)
                        pg.display.update()
                        flag_dead = False
                        
                        whistle.play()
                        time.sleep(1)
                        sp = 2
                        power1 = power2 = 0
                        x1 = 600
                        y1 = 275
                        x2 = 300
                        y2 = 275
                        right1 = right2 = False
                        left1 = left2 = False
                        up1 = up2 = False
                        down1 = down2 = False
                        

                  if score_blue == 3:
                        winer = "blue"
                        break
                  if score_red == 3:
                        winer = "red"
                        break

            if winer:
                  color = (255, 0, 0)
                  if winer == "blue":
                        color = (0, 0, 255)
                  winning = font2.render('Player ' + winer + ' has won the game' , True , color)
                  d = winning.get_rect()
                  d.center = (500, 350)
            while run:
                  for event in pg.event.get() :
                        if event.type == pg.QUIT :
                              run = False
                              run0 = False
                        if event.type == pg.MOUSEBUTTONDOWN :
                              xm , ym = event.pos
                              
                              if 940 < xm < 990 and 640 < ym < 690:
                                    run = False
                                    start_txt = font.render("Start", True, (255, 255, 255))
                  win.blit(bg,(0,0))
                  win.blit(winning,d)
                  win.blit(home_button, (940, 640))
                  pg.display.update()
