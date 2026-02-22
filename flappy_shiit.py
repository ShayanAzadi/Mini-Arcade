import pygame as pg 
import random as rdm

def flappy_shiit():
      pg.init()
      win = pg.display.set_mode((1000, 600))
      pg.display.set_caption("little powerful bird")

      def __init__(block):
            blocks_x = [1100]
            block_trnsform = []
            length = []
            for i in range(1, 4):
                  blocks_x.append(blocks_x[i - 1] + 280)
                  length.append(rdm.randint(50, 320))
                  block_trnsform.append([pg.transform.scale(block, (80, length[i - 1])),  pg.transform.scale(block, (80, 550 - length[i - 1] - 150))])
            length.append(rdm.randint(50, 320))
            block_trnsform.append([pg.transform.scale(block, (80, length[i])),  pg.transform.scale(block, (80, 550 - (length[i] + 150)))])
            
            return blocks_x, block_trnsform, length

      def gameover(xj, yj, length, blocks_x):
            for i in range(len(blocks_x)):
                  if (blocks_x[i] < xj < blocks_x[i] + 80 or blocks_x[i] < xj + 60 < blocks_x[i] + 80) and (0 < yj < length[i] or 0 < yj + 40 < length[i] or yj + 40 <= 0):
                        return True
                  if (blocks_x[i] < xj < blocks_x[i] + 80 or blocks_x[i] < xj + 60 < blocks_x[i] + 80) and (length[i] + 150 < yj < 550 or length[i] + 150 < yj + 40 < 550):
                        return True
                  if yj + 40 >= 550:
                        return True
            
            return False



      joojoo = pg.image.load("6/joojoo.png")
      joojoo = pg.transform.scale(joojoo , (60, 40))

      pg.display.set_icon(joojoo)

      home_button = pg.transform.scale(pg.image.load("home_button.png"), (50, 50))

      lose = pg.mixer.Sound("6/loses.wav")
      block = pg.image.load("6/block.png")


      bg = pg.image.load("6/bg.png")
      bg = pg.transform.scale(bg , (1000, 600))



      font = pg.font.Font("ARLRDBD.TTF", 30)
      font2 = pg.font.Font("ARLRDBD.TTF", 60)


      start_txt = font2.render("Start", True, (255, 255, 255))
      stpos = start_txt.get_rect()
      stpos.center = (500, 300)
      stw = start_txt.get_width()
      sth = start_txt.get_height()


      end_txt = font2.render("you lost", True, (255, 0, 0))
      endpos = end_txt.get_rect()
      endpos.center = (500, 300)



      yj = 275
      sy = 12
      sq = 0
      spayeen = 12
      s_harekat_mane = 6

      run0 = True 
      run = False 
      jump = False

      while run0:
            win.blit(bg,(0,0))
            win.blit(start_txt,stpos)
            for event in pg.event.get() :
                  if event.type == pg.QUIT :
                        run0 = False
                  if event.type == pg.KEYDOWN:
                        if event.key == pg.K_p:
                              pg.mixer.music.stop()
                  if event.type == pg.MOUSEBUTTONDOWN :
                        xm , ym = event.pos
                        if 500 - stw/2 < xm < 500 + stw/2 and 300 - sth/2 < ym < 300 + sth/2 :
                                    run = True
                                    blocks_x, block_trnsform, length = __init__(block)
                                    score = 0
                                    sy = 12
                                    sq = 0
                                    spayeen = 0
                                    s_harekat_mane = 6
                                    yj = 275
                                    jump = False
                                    flag_score = False

                  if event.type == pg.MOUSEMOTION :
                        xm , ym = event.pos
                        if 500 - stw/2 < xm < 500 + stw/2 and 300 - sth/2 < ym < 300 + sth/2 :
                              start_txt = font2.render("Start", True, (0, 0, 0))
                        else :
                              start_txt = font2.render("Start", True, (255, 255, 255))

            pg.display.update()
            while run:
                  for event in pg.event.get():
                        if event.type == pg.QUIT:
                              run = False
                              run0 = False
                        if event.type == pg.MOUSEBUTTONDOWN:
                              xm, ym = event.pos 

                              if 10 < xm < 60 and 10 < ym < 60:
                                    run = False
                                    start_txt = font2.render("Start", True, (255, 255, 255))
                        if event.type == pg.KEYDOWN:
                              if event.key == pg.K_SPACE:
                                    if not jump:
                                          jump = True
                                          spayeen = 12
                                    else:
                                          sy += 12 - sq
                              if event.key == pg.K_p:
                                    pg.mixer.music.stop()
                  
                  if jump:
                        yj -= sy
                        sy -= 1
                        sq = sy
                        if sy == -13:
                              jump = False
                              sy = 12
                              sq = 12

                  else:
                        yj += spayeen
                        if spayeen:
                              spayeen += 0.5
                        
                  s_harekat_mane += 0.00005
                  win.blit(bg, (0, 0))
                  for i in range(len(blocks_x)):
                        if blocks_x[i] + 80 <= 80 and not flag_score:
                              score += 1
                              flag_score = True
                        
                        blocks_x[i] -= s_harekat_mane
                        if blocks_x[i] + 80 <= 0:
                              flag_score = False
                              blocks_x[i] = max(blocks_x) + 280
                              length[i] = rdm.randint(50, 320)
                              block_trnsform[i] = [pg.transform.scale(block, (80, length[i])),  pg.transform.scale(block, (80, 550 - length[i] - 150))]

                        win.blit(block_trnsform[i][0], (blocks_x[i], 0))
                        win.blit(block_trnsform[i][1], (blocks_x[i], length[i] + 150))

                  win.blit(joojoo, (80, yj))

                  win.blit(font.render("Score: " + str(score), True, (255, 255, 255)), (70, 15))

                  win.blit(home_button, (10, 10))
                  pg.display.update()
                  pg.time.Clock().tick(80)

                  if gameover(80, yj, length, blocks_x):
                        lose.play()
                        break

            lost_txt = font2.render("You Lost", True, (255, 255, 255))
            d_lost = lost_txt.get_rect()
            d_lost.center = (500, 300)
            while run:
                  for event in pg.event.get():
                        if event.type == pg.QUIT:
                              run = False
                              run0 = False
                        if event.type == pg.MOUSEBUTTONDOWN:
                              xm, ym = event.pos 

                              if 10 < xm < 60 and 10 < ym < 60:
                                    run = False
                                    start_txt = font2.render("Start", True, (255, 255, 255))

                  
                  win.blit(lost_txt, d_lost)
                  pg.display.update()
            