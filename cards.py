from time import sleep
import pygame as pg, random as rdm

def cards():
      pg.init()

      def x_and_y():
            a = []
            x = 180
            y = 100
            for i in range(0, 640, 80):
                  for j in range(0, 640, 80):
                        a.append((j + x, i + y))
            
            return a

      def randoming(imgs):
            a = [0] * 64
            for i in range(16):
                  for j in range(4):
                        flag = False
                        while not flag:
                              b = rdm.randint(0, 63)
                              if a[b] == 0:
                                    a[b] = imgs[i]
                                    flag = True
                              else:
                                    flag = False
            
            return a

      home_button = pg.transform.scale(pg.image.load("home_button.png"), (50, 50))
      pg.display.set_caption("Memory Cards")
      
      bg_color = (230, 40, 10)

      win = pg.display.set_mode((1000, 770))
      pg.display.set_caption("cards")

      font = pg.font.Font("ARLRDBD.ttf", 30)
      font2 = pg.font.Font("ARLRDBD.ttf", 60)
      start = font2.render('Start' , True , (255, 255, 255))
      startpos = start.get_rect()
      startpos.center = (500, 350)

      card = pg.transform.scale(pg.image.load("5/card.png"), (75, 75))
      lists = x_and_y()

      images = []
      for i in range(16):
            images.append(pg.transform.scale(pg.image.load("5/" + str(i + 1) + ".png"), (75, 75)))

      pg.display.set_icon(images[4])
      shekl_khone = randoming(images)

      hs = start.get_height()
      ws = start.get_width()

      score_red = score_blue = 0

      first_select = second_select = None
      player_turn = "red"

      run = False
      run0 = True

      gameover = False


      while run0:
            win.fill((150, 150, 150))
            win.blit(start,startpos)
            for event in pg.event.get():
                  if event.type == pg.KEYDOWN:
                        if event.key == pg.K_p:
                              pg.mixer.music.stop()
                  
                  if event.type == pg.QUIT:
                        run0 = False
                  if event.type == pg.MOUSEMOTION:
                        xm, ym = event.pos
                        if 500 - ws/2 < xm < 500 + ws/2 and 350 - hs/2 < ym < 350 + hs/2:
                              start = font2.render('Start', True, (0, 0, 0))
                        else:
                              start = font2.render('Start' , True , (255, 255, 255))
                  
                  if event.type == pg.MOUSEBUTTONDOWN :
                        xm, ym = event.pos
                  
                        if 500 - ws/2 < xm < 500 + ws/2 and 350 - hs/2 < ym < 350 + hs/2:
                              run = True
                              lists = x_and_y()
                              shekl_khone = randoming(images)
                              gameover = False
                              score_red = score_blue = 0
                              player_turn = "red"
                              bg_color = (230, 50, 20)


                        
            pg.display.update()


            while run:
                  for event in pg.event.get():
                        if event.type == pg.QUIT:
                              run = False
                              run0 = False
                        if event.type == pg.KEYDOWN:
                              if event.key == pg.K_p:
                                    pg.mixer.music.stop()
                        if event.type == pg.MOUSEBUTTONDOWN:
                              xm, ym = event.pos
                              
                              if 10 < xm < 60 and 10 < ym < 60:
                                    run = False
                                    start = font2.render('Start' , True , (255, 255, 255))
                              for i in lists:
                                    if i != 0:
                                          if i[0] < xm < i[0] + 75 and i[1] < ym < i[1] + 75:
                                                if first_select is None:
                                                      first_select = lists.index(i)
                                                if lists.index(i) != first_select and second_select is None:
                                                      second_select = lists.index(i)


                  win.fill(bg_color)

                  score_txt = font2.render(str(score_red) + " - " + str(score_blue), True, (0, 0, 0))
                  d = score_txt.get_rect()
                  d.center = (500, 50)

                  win.blit(score_txt, d)
                  win.blit(home_button, (10, 10))
                  for i in range(len(lists)):
                        if shekl_khone[i] != 0 and lists[i] != 0:
                              if first_select == i:
                                    win.blit(shekl_khone[i], (lists[i][0], lists[i][1]))
                              elif second_select == i:
                                    win.blit(shekl_khone[i], (lists[i][0], lists[i][1]))
                              else:
                                    win.blit(card, (lists[i][0], lists[i][1]))
                  pg.display.update()


                  if first_select != None and second_select != None:
                        if shekl_khone[first_select] == shekl_khone[second_select]:
                              if player_turn == "red":
                                    score_red += 1
                              else:
                                    score_blue += 1
                              
                              lists[first_select] = 0
                              lists[second_select] = 0
                              shekl_khone[first_select] = 0
                              shekl_khone[second_select] = 0
                        else:
                              if player_turn == "red":
                                    player_turn = "blue"
                                    bg_color = (20, 100, 200)
                              else:
                                    player_turn = "red"
                                    bg_color = (230, 50, 20)


                        sleep(1)
                        first_select = second_select = None

                  gameover = True
                  for i in lists:
                        if i != 0:
                              gameover = False
                              break
                  
                  if gameover:
                        break
            

            if score_blue > score_red:
                  win_txt = font2.render("Player blue has won the game", True, (255, 255, 255))
                  color = (0, 0, 255)
            elif score_red > score_blue:
                  win_txt = font2.render("Player red has won the game", True, (255, 255, 255))
                  color = (255, 0, 0)
            else:
                  win_txt = font2.render("Draw", True, (255, 255, 255))
                  color = (0, 0, 0)

            d_win = win_txt.get_rect()
            d_win.center = (500, 350)
            
            while run and gameover:
                  
                  for event in pg.event.get():
                        if event.type == pg.QUIT:
                              run = False
                              run = False
                        if event.type == pg.MOUSEBUTTONDOWN:
                              xm, ym = event.pos 

                              if 10 < xm < 60 and 10 < ym < 60:
                                    run = False
                                    start = font2.render('Start' , True , (255, 255, 255))
                  win.fill(color)
                  win.blit(win_txt, d_win)
                  win.blit(home_button, (10, 10))
                  pg.display.update()
