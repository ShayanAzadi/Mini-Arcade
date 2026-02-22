from time import sleep
import pygame as pg
import random as rdm


def red_hands():
    def reset(sr : int, sb : int, yr : int, yb : int, turn : bool, win : pg.surface):
        sleep(0.5)
        if (not turn and sr < 0) or turn:
            sr = -sr
        if sr == 0:
            sr = 25

        if (turn and sb > 0) or not turn:
            sb = -sb
        if sb == 0:
            sb = -25

        while True:
            if yr != -300:
                yr += sr
            
            if yb != 400:
                yb += sb

            win.blit(bg, (0, 0))

            score_txt = font.render(str(score_r), True, (255, 0, 0))
            d = score_txt.get_rect()
            d.center = (30, 300)

            win.blit(score_txt, d)

            score_txt = font.render(str(score_b), True, (0, 0, 255))
            d = score_txt.get_rect()
            d.center = (30, 400)

            win.blit(score_txt, d)

            if turn:
                win.blit(police_r[(score_b + 2) // 2 - 1], (129, yr + 300))
                win.blit(racer_b[(score_r + 2) // 2 - 1], (129, yb))
            else:
                win.blit(police_b[(score_r + 2) // 2 - 1], (129, yb))
                win.blit(racer_r[(score_b + 2) // 2 - 1], (129, yr + 300))
            
            win.blit(home_button, (10, 10))
            pg.display.update()
            pg.time.Clock().tick(70)

            if yr == -300 and yb == 400:
                sr = 0
                sb = 0
                break
        
        pg.event.clear()

        return sr, sb, yr, yb, False, 0


    pg.init()

    win = pg.display.set_mode((400, 700))
    pg.display.set_caption("Broken Cars")
    font = pg.font.Font("ARLRDBD.TTF", 50)
    start_txt = font.render("Start", True, (255, 0, 0))
    stpos = start_txt.get_rect()
    stpos.center = (200, 350)
    stw = start_txt.get_width()
    sth = start_txt.get_height()

    bg = pg.transform.scale(pg.image.load("7/bg.png"), (400, 700))

    police_b = []
    racer_b = []
    police_r = []
    racer_r = []

    for i in range(1, 6):
        a = pg.transform.scale(pg.image.load("7/police" + str(i) + ".png"), (142, 300))
        a1 = pg.transform.rotate(a, 180)
        police_b.append(a)
        police_r.append(a1)
        racer_b.append(pg.transform.scale(pg.image.load("7/racer_b" + str(i) + ".png"), (142, 300)))
        racer_r.append(pg.transform.rotate(pg.transform.scale(pg.image.load("7/racer_r" + str(i) + ".png"), (142, 300)), 180))

    a = pg.transform.scale(pg.image.load("7/police" + str(i) + ".png"), (142, 300))
    a1 = pg.transform.rotate(a, 180)
    police_b.append(a)
    police_r.append(a1)
    racer_b.append(pg.transform.scale(pg.image.load("7/racer_b" + str(i) + ".png"), (142, 300)))
    racer_r.append(pg.transform.rotate(pg.transform.scale(pg.image.load("7/racer_r" + str(i) + ".png"), (142, 300)), 180))

    home_button = pg.transform.scale(pg.image.load("home_button.png"), (50, 50))

    pg.display.set_icon(pg.transform.scale(a, (50, 50)))
    run0 = True
    turn = rdm.randint(False, True)
    run = False
    yr = -300
    yb = 400
    sr = 0
    sb = 0
    score_r = 0
    score_b = 0
    gameover = False
    xr = 0
    xb = 0

    while run0:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_p:
                    pg.mixer.music.stop()
            if event.type == pg.QUIT:
                run0 = False
            if event.type == pg.MOUSEMOTION:
                xm, ym = event.pos

                if 200 - stw/2 < xm < 200 + stw/2 and 350 - sth/2 < ym < 350 + sth/2:
                    start_txt = font.render("Start", True, (0, 0, 255))
                else:
                    start_txt = font.render("Start", True, (255, 0, 0))

            if event.type == pg.MOUSEBUTTONDOWN:
                xm, ym = event.pos

                if 200 - stw/2 < xm < 200 + stw/2 and 350 - sth/2 < ym < 350 + sth/2:
                    turn = rdm.randint(False, True)
                    run = True
                    yr = -300
                    yb = 400
                    sr = 0
                    sb = 0
                    score_r = 0
                    score_b = 0
                    gameover = False
                    xr = 0
                    xb = 0
                    i = 0
                    flag_i = False

        #win.fill((16, 255, 144))
        win.blit(bg, (0, 0))
        win.blit(start_txt, stpos)

        
        pg.display.update()


        while run:
            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONDOWN:
                    xm, ym = event.pos 

                    if 10 < xm < 60 and 10 < ym < 60:
                        run = False
                        start_txt = font.render("Start", True, (255, 0, 0))
                if event.type == pg.QUIT:
                    run = False
                    run0 = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_p:
                        pg.mixer.music.stop()
                    if event.key == pg.K_q:
                        if turn and sr == 0:
                            sr = 25
                            xr = -50
                        elif sr == 0:
                            sr = -25
                            xr = -550

                    if event.key == pg.K_o:
                        if not turn and sb == 0:
                            sb = -25
                            xb = 150
                        elif sb == 0:
                            sb = 25
                            xb = 650


            if yr + 600 >= yb:
                sr, sb, yr, yb, flag_i, i = reset(sr, sb, yr, yb, turn, win)

                if turn:
                    score_r += 1
                else:
                    score_b += 1

            if yr == xr and xr != -300:
                if xr == -50:
                    sr, sb, yr, yb, flag_i, i = reset(sr, sb, yr, yb, turn, win)
                    turn = not turn
                else:
                    sr = 0
                    flag_i = True
                    if i == 25:
                        flag_i = False
                        i = 0
                        sr = 25
                        xr = -300   
            elif xr == yr and sr != 0:
                score_b += 1
                sr = 0

            if yb == xb and xb != 400:
                if xb == 150:
                    sr, sb, yr, yb, flag_i, i = reset(sr, sb, yr, yb, turn, win)
                    turn = not turn
                else:
                    sb = 0
                    flag_i = True
                    if i == 25:
                        flag_i = False
                        i = 0
                        sb = -25
                        xb = 400
            elif xb == yb and sb != 0:
                sb = 0
                score_r += 1
            
            
            yb += sb
            yr += sr
            
            if flag_i:
                i += 1

            win.blit(bg, (0, 0))

            score_txt = font.render(str(score_r), True, (255, 0, 0))
            d = score_txt.get_rect()
            d.center = (30, 300)

            win.blit(score_txt, d)

            score_txt = font.render(str(score_b), True, (0, 0, 255))
            d = score_txt.get_rect()
            d.center = (30, 400)

            win.blit(score_txt, d)

            if turn:
                win.blit(police_r[(score_b + 2) // 2 - 1], (129, yr + 300))
                win.blit(racer_b[(score_r + 2) // 2 - 1], (129, yb))
            else:
                win.blit(police_b[(score_r + 2) // 2 - 1], (129, yb))
                win.blit(racer_r[(score_b + 2) // 2 - 1], (129, yr + 300))
            
            win.blit(home_button, (10, 10))
            pg.display.update()
            pg.time.Clock().tick(100)


            if score_r == 10 or score_b == 10:
                gameover = True
                break



        if score_b > score_r:
            win_txt = font.render("You won", True, (0, 0, 255))
            lose_txt = font.render("You lost", True, (255, 0, 0))
            d_win = win_txt.get_rect()
            d_win.center = (200, 525)
            d_lose = lose_txt.get_rect()
            d_lose.center = (200, 125)
        else:
            win_txt = font.render("You won", True, (255, 0, 0))
            lose_txt = font.render("You lost", True, (0, 0, 255))
            d_win = win_txt.get_rect()
            d_win.center = (200, 125)
            d_lose = lose_txt.get_rect()
            d_lose.center = (200, 525)

        while run and gameover:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
                    run0 = False
                
                if event.type == pg.MOUSEBUTTONDOWN:
                    xm, ym = event.pos 

                    if 10 < xm < 60 and 10 < ym < 60:
                        run = False
                        start_txt = font.render("Start", True, (255, 0, 0))

            win.blit(bg, (0, 0))
            win.blit(win_txt, d_win)
            win.blit(lose_txt, d_lose)
            win.blit(home_button, (10, 10))
            pg.display.update()

    
