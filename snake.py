from time import sleep
import pygame as pg, random as rdm

def snake():
      def randomfood (body):
            flag = True 
            
            while flag:
                  xf = rdm.randint(0, 290)
                  yf = rdm.randint(0, 290)
                  flag = False
                  for i in body:
                        if i[0] == xf and i[1] == yf:
                              flag = True
                  if not flag:
                        if xf % 10 != 0 or yf % 10 != 0:
                              flag = True
            return (xf , yf)
                  
      def left_shift(inp, ls):
            for i in range(len(ls) - 1, -1, -1):
                  a = ls[i]
                  ls[i] = inp
                  inp = a
            return ls
      

      def create_body(length):
            if length > 30:
                  length = 30

            x = 0
            ls = []
            for i in range(length):
                  ls.append([x, 0])
                  x += 10
            
            return ls


      pg.init()
      win = pg.display.set_mode((300, 300))
      pg.display.set_caption("snake")

      snake_head_img = pg.transform.scale(pg.image.load("2/head.png"), (10, 10))

      pg.display.set_icon(snake_head_img)
      bkground = pg.transform.scale(pg.image.load("2/bg.png"), (300, 300))

      apple_bite_sound = pg.mixer.Sound("2/Apple-bite.mp3")
      game_over_sound = pg.mixer.Sound("2/game-over.wav")

      img_snake_head = snake_head_img

      font = pg.font.Font("ARLRDBD.TTF", 40)
      font2 = pg.font.Font("ARLRDBD.TTF", 15)

      start_txt = font.render("Start", True, (255, 255, 255))
      start_txt_height = start_txt.get_height()
      start_txt_width = start_txt.get_width()
      center_start = start_txt.get_rect()
      center_start.center = (150, 150)

      food = pg.image.load("2/food.png")
      food = pg.transform.scale(food , (10, 10))
      xyfood = (150, 150)
      body_length = 15

      snake_color = (23, 132, 182)
      point_snake = 0

      ps = 0

      eat = False 
      run = False
      run0 = True
      left_click = False
      right_click = False
      up_click = False
      down_click = False
      lefts = False
      rights = False
      ups = False
      downs = False

      while run0:
            for event in pg.event.get():
                  if event.type == pg.QUIT:
                        run0 = False

                  if event.type == pg.KEYDOWN:
                        if event.key == pg.K_p:
                              pg.mixer.music.stop()

                  if event.type == pg.MOUSEMOTION:
                        xm, ym = event.pos 

                        if 150 - start_txt_width / 2 < xm <  150 + start_txt_width / 2 and 150 - start_txt_height / 2 < ym <  150 + start_txt_height / 2:
                              start_txt = font.render("Start", True, (0, 0, 0))
                        else:
                              start_txt = font.render("Start", True, (255, 255, 255))

                  if event.type == pg.MOUSEBUTTONDOWN:
                        xm, ym = event.pos 

                        if 150 - start_txt_width / 2 < xm <  150 + start_txt_width / 2 and 150 - start_txt_height / 2 < ym <  150 + start_txt_height / 2:
                              run = True
                              lefts = False
                              rights = False
                              ups = False
                              downs = False
                              eat = False
                              point_snake = 0
                              img_snake_head = snake_head_img
                              body = create_body(body_length)
                              xyfood = (150, 150)
                              ps = 0
            
            win.blit(bkground, (0, 0))
            win.blit(start_txt, center_start)
            
            pg.display.update()
            while run:
                  for event in pg.event.get():
                        if event.type == pg.QUIT:
                              run = False
                              run0 = False
                        if event.type == pg.KEYDOWN:
                              if event.key == pg.K_p:
                                    pg.mixer.music.stop()
                              if event.key == pg.K_RIGHT and lefts == False:
                                    right_click = True
                                    rights = True
                                    lefts = False
                                    ups = False
                                    downs = False
                                    img_snake_head = snake_head_img
                              if event.key == pg.K_LEFT and rights == False:
                                    left_click = True
                                    lefts = True
                                    rights = False
                                    ups = False
                                    downs = False
                                    img_snake_head = pg.transform.rotate(snake_head_img, 180)
                              if event.key == pg.K_DOWN and ups == False:
                                    down_click = True
                                    ups = False
                                    rights = False
                                    lefts = False
                                    downs = True
                                    img_snake_head = pg.transform.rotate(snake_head_img, 270)
                              if event.key == pg.K_UP and downs == False:
                                    up_click = True
                                    downs = False
                                    rights = False 
                                    lefts = False
                                    ups = True
                                    img_snake_head = pg.transform.rotate(snake_head_img, 90)

                  if rights or right_click:
                        body = left_shift([body[-1][0] + 10, body[-1][1]], body)
                        right_click = False
                        
                  if lefts or left_click:
                        body = left_shift([body[-1][0] - 10, body[-1][1]], body)
                        left_click = False
                        
                  if ups or up_click:
                        body = left_shift([body[-1][0], body[-1][1] - 10], body)
                        up_click = False
                        
                  if downs or down_click:
                        body = left_shift([body[-1][0], body[-1][1] + 10], body)
                        down_click = False
                        
                  if body[-1][0] + 10 > 300:
                        body = left_shift([0, body[-1][1]], body)
                  if body[-1][0] < 0:
                        body = left_shift([300, body[-1][1]], body)
                  if body[-1][1] + 10 > 300:
                        body = left_shift([body[-1][0], 0], body)
                  if body[-1][1] < 0:
                        body = left_shift([body[-1][0], 300], body)
                        
                  if body[-1][0] == xyfood[0] and body[-1][1] == xyfood[1]:
                        ps += 1
                        eat = True
                        
                  if body[-1] in body[:-1]:
                        game_over_sound.play()
                        pg.display.update()
                        sleep(2)
                        break

                  if eat:
                        apple_bite_sound.play()
                        point_snake += 1
                        body.insert(0, body[0])
                        xyfood = randomfood(body)
                        eat = False 

                  win.blit(bkground, (0, 0))
                  for i in range(len(body) - 1):
                        pg.draw.rect(win, snake_color, (body[i][0], body[i][1], 10, 10))
                  win.blit(img_snake_head, (body[-1][0], body[-1][1]))
                  win.blit(food, xyfood)
                  
                  pg.display.update()
                  pg.time.Clock().tick(12)
            
            losing = font2.render('You have lost the game, your score: ' + str(point_snake) , True , (255, 255, 255))
            d_lose = losing.get_rect()
            d_lose.center = (150, 150)
            while run:
                  for event in pg.event.get() :
                        if event.type == pg.QUIT :
                              run = False
                              start_txt = font.render("Start", True, (255, 255, 255))
                  win.blit(bkground ,(0,0))
                  win.blit(losing ,d_lose)
                  pg.display.update()
