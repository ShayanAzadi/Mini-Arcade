import pygame as pg, time
pg.init()

def sumo():
    disp = pg.display.set_mode((1000, 700))
    pg.display.set_caption("sumo")
    font = pg.font.Font("ARLRDBD.TTF", 50)
    font2 = pg.font.Font("ARLRDBD.TTF", 80)
    start_txt = font2.render("Start", True, (255, 255, 255))
    d_st = start_txt.get_rect()
    d_st.center = (500, 350)
    hs = start_txt.get_height()
    ws = start_txt.get_width()

    home_button = pg.transform.scale(pg.image.load("home_button.png"), (50, 50))

    bkground = pg.image.load("3/bg.png")
    bkground = pg.transform.scale(bkground, (1000, 700))
    p_red = pg.transform.scale(pg.image.load("3/p_red.png"), (202, 187))
    p_blue = pg.transform.scale(pg.image.load("3/p_blue.png"), (202, 187))

    pg.display.set_icon(pg.transform.scale(p_red, (50, 50)))
    xb = 600
    xr = 200
    sr = 0
    sb = 0
    pb = pr = 0
    run = False
    run0 = True
    flag = False

    while run0:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run0 = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_p:
                    pg.mixer.music.stop()
            if event.type == pg.MOUSEMOTION:
                    xm, ym = event.pos
                    if 500 - ws/2 < xm < 500 + ws/2 and 350 - hs/2 < ym < 350 + hs/2:
                            start_txt = font2.render('Start' , True , (0, 0, 0))
                    else:
                            start_txt = font2.render('Start' , True , (255, 255, 255))
            if event.type == pg.MOUSEBUTTONDOWN :
                    xm , ym = event.pos
                    if 500 - ws/2 < xm < 500 + ws/2 and 350 - hs/2 < ym < 350 + hs/2:
                            run = True
                            pb = pr = 0
                            xb = 600
                            xr = 198
                
        disp.blit(bkground, (0, 0))
        disp.blit(start_txt, d_st)
        pg.display.update()

        while run:
            sr = sb = 0
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
                    run0 = False
                    start_txt = font2.render('Start' , True , (255, 255, 255))
                if event.type == pg.MOUSEBUTTONDOWN:
                    xm, ym = event.pos

                    if 10 < xm < 60 and 10 < ym < 60:
                        run = False
                        start_txt = font2.render("Start", True, (255, 255, 255))
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_p:
                        pg.mixer.music.stop()
                    if event.key == pg.K_q:
                        sr = 10
                    if event.key == pg.K_o:
                        sb = -10
            
            xb += sb
            xr += sr

            if sr == 10 and xr + 202 >= xb:
                xb += 15
            if sb == -10 and xb <= xr + 202:
                xr -= 15
            if xr + 202 < 257:
                pb += 1
                flag = True
            if xb > 500 + 243:
                pr += 1
                flag = True
                
            score_txt = font.render(str(pr) + " - " + str(pb), True, (0, 0, 0))
            d = score_txt.get_rect()
            d.center = (500, 50)

            disp.blit(bkground, (0, 0))
            disp.blit(p_red, (xr, 256))
            disp.blit(p_blue, (xb, 256))
            disp.blit(score_txt, (d))
            disp.blit(home_button, (10, 10))
            pg.display.update()

            if flag:
                xb = 600
                xr = 198
                flag = False
                time.sleep(2)
            
            if pr == 3 or pb == 3:
                break
        
        a = 'red'
        color = (255,0,0)
        if pb == 3 :
                a = 'blue'
                color = (0,0,255)
        winning = font.render('Player '+a+' has won the game' , True , color)
        d_w = winning.get_rect()
        d_w.center = (500, 350)
        while run :
                for event in pg.event.get() :
                    if event.type == pg.QUIT :
                        run = False
                        run0 = False
                    if event.type == pg.MOUSEBUTTONDOWN:
                        xm, ym = event.pos

                        if 10 < xm < 60 and 10 < ym < 60:
                            run = False
                            start_txt = font2.render("Start", True, (255, 255, 255))
                disp.blit(bkground,(0,0))
                disp.blit(winning,d_w)
                disp.blit(home_button, (10, 10))
                pg.display.update()
