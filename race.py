from time import sleep
import pygame as pg


def race():
    pg.init()
    win = pg.display.set_mode((500, 750))
    pg.display.set_caption("Race")
    home_button = pg.transform.scale(pg.image.load("home_button.png"), (50, 50))

    font = pg.font.Font("ARLRDBD.TTF", 50)
    start_txt = font.render("Start", True, (255, 255, 255))
    stpos = start_txt.get_rect()
    stpos.center = (250, 375)
    stw = start_txt.get_width()
    sth = start_txt.get_height()
    bg = pg.transform.scale(pg.image.load("8/bg.png"), (500, 750))
    red = pg.transform.scale(pg.image.load("8/red.png"), (45, 100))
    yellow = pg.transform.scale(pg.image.load("8/yellow.png"), (45, 100))

    pg.display.set_icon(red)
    run0 = True
    turn = False
    run = False
    yr = 600
    yy = 600
    sr = 0
    sy = 0
    score_r = 0
    score_b = 0
    gameover = False
    winner = False

    while run0:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_p:
                    pg.mixer.music.stop()
            if event.type == pg.QUIT:
                run0 = False
            if event.type == pg.MOUSEMOTION:
                xm, ym = event.pos

                if 250 - stw/2 < xm < 250 + stw/2 and 375 - sth/2 < ym < 375 + sth/2:
                    start_txt = font.render("Start", True, (0, 0, 0))
                else:
                    start_txt = font.render("Start", True, (255, 255, 255))

            if event.type == pg.MOUSEBUTTONDOWN:
                xm, ym = event.pos

                if 250 - stw/2 < xm < 250 + stw/2 and 375 - sth/2 < ym < 375 + sth/2:
                    turn = False
                    run = True
                    yr = 600
                    yy = 600
                    sr = 0
                    sy = 0
                    gameover = False
                    winner = False

        win.blit(bg, (0, 0))
        win.blit(start_txt, stpos)

        
        pg.display.update()

        while run:
            sr = sy = 0
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
                    run0 = False
                if event.type == pg.MOUSEBUTTONDOWN:
                    xm, ym = event.pos 

                    if 10 < xm < 60 and 10 < ym < 60:
                        run = False
                        start_txt = font.render("Start", True, (255, 255, 255))
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_p:
                        pg.mixer.music.stop()
                    if event.key == pg.K_o:
                        sr = -5
                    if event.key == pg.K_q:
                        sy = -5

            yr += sr
            yy += sy
            if yr == 75 and yy != 75:
                gameover = True
                winner = "red"
            if yy == 75 and yr != 75:
                winner = "yellow"
                gameover = True
            if yy == yr == 75:
                gameover = True
                winner = "draw"

            win.blit(bg, (0, 0))
            win.blit(yellow, (150, yy))
            win.blit(red, (305, yr))
            win.blit(home_button, (10, 10))
            pg.display.update()

            if gameover:
                sleep(1)
                break

        if winner == "yellow":
            win_txt = font.render("Yellow car won", True, (255, 255, 0))
        elif winner == "red":
            win_txt = font.render("Red car won", True, (255, 0, 0))
        else:
            win_txt = font.render("Draw", True, (255, 255, 255))

        d_win = win_txt.get_rect()
        d_win.center = (250, 375)
        while run and gameover:
                
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
                    run0 = False
                if event.type == pg.MOUSEBUTTONDOWN:
                    xm, ym = event.pos 

                    if 10 < xm < 60 and 10 < ym < 60:
                        run = False
                        start_txt = font.render("Start", True, (255, 255, 255))
            win.blit(bg, (0, 0))
            win.blit(win_txt, d_win)
            win.blit(home_button, (10, 10))
            pg.display.update()
