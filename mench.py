import random as rdm
import time
import pygame as pg

def mench():
    def players(win : pg.surface, font : pg.font):
        run = True
        p = 1
        txt = []
        d = []
        for i in range(2, 5):
            txt.append(font.render(str(i) + "players: Click button " + str(i), True, (0, 0, 0)))
            d.append((400, (i + 1) * 100))

        while run:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_2:
                        p = 2
                    if event.key == pg.K_3:
                        p = 3
                    if event.key == pg.K_4:
                        p = 4

            win.fill((16, 255, 142))
            for i in range(len(txt)):
                dic = txt[i].get_rect()
                dic.center = d[i]
                win.blit(txt[i], dic)
            pg.display.update()
            if p != 1:
                break
        
        return p - 1, run

    def check_turn(mohre_xy : list, dice_number : int, road : list):
        for i in mohre_xy:
            if (i in road or (i not in road and dice_number == 5)) and can(road, mohre_xy, dice_number, mohre_xy.index(i)):
                return True

        return False

    def can(road : list, mohre_xy : list, dice_number : int, harekat_mohre : int):
        index = None

        if mohre_xy[harekat_mohre] in road:
            index = road.index(mohre_xy[harekat_mohre])
        if index is not None and index + dice_number + 1>= len(road):
            return False


        if index is not None and road[index + dice_number + 1] in mohre_xy:
            return False

        if index is None and dice_number == 5:
            if road[0] in mohre_xy:
                return False

        return True

    def dicing(img : list, turn : int, number : int, disp : pg.surface, xy_dice):
        n = rdm.randint(3, 10)
        for i in range(n - 1):
            random_img = rdm.choice(img)
            random_img = random_img[turn]
            disp.blit(random_img, xy_dice)
            pg.display.update()
            pg.time.Clock().tick(30)
            time.sleep(0.12)
        

        disp.blit(img[number][turn], xy_dice)
        pg.display.update()
        pg.time.Clock().tick(30)
        if number != 5:
            time.sleep(1.5)

        return


    def kill(mohre_xy, turn, harekat_mohre, first_pos):
        for i in range(len(mohre_xy)):
            if i != turn:
                for k in range(4):
                    if mohre_xy[i][k] == mohre_xy[turn][harekat_mohre]:
                        mohre_xy[i][k] = first_pos[i][k]
        return  mohre_xy

    def vector():
        ls_green = [(60, 332), (128, 332), (196, 332), (264, 332), (332, 332), (332, 264), (332, 196), (332, 128), (332, 60), (400, 60)]
        ls_blue = [(468, 60), (468, 128), (468, 196), (468, 264), (468, 332), (536, 332), (604, 332), (672, 332), (740, 332), (740, 400)]
        ls_yellow = [(740, 468), (672, 468), (604, 468), (536, 468), (468, 468), (468, 536), (468, 604), (468, 672), (468, 740), (400, 740)]
        ls_red = [(332, 740), (332, 672), (332, 604), (332, 536), (332, 468), (264, 468), (196, 468), (128, 468), (60, 468), (60, 400)]


        green = ls_green + ls_blue + ls_yellow + ls_red
        blue = ls_blue + ls_yellow + ls_red + ls_green
        yellow = ls_yellow + ls_red + ls_green + ls_blue
        red = ls_red + ls_green + ls_blue + ls_yellow

        return green, blue, yellow, red

    pg.init()
    win = pg.display.set_mode((800, 800))
    pg.display.set_caption("mench")
    font = pg.font.Font("ARLRDBD.TTF", 50)
    start_txt = font.render("Start", True, (255, 255, 255))
    stpos = start_txt.get_rect()
    stpos.center = (400, 400)
    stw = start_txt.get_width()
    sth = start_txt.get_height()

    main_bg = pg.transform.scale(pg.image.load("9/mench.png"), (800, 800))

    dice_xy = [(204, 204), (521, 521), (521, 204), (204, 521)]

    dice_imgs = []
    turn = 0

    win_txt = [font.render("Player Green won", True, (0, 255, 0)), font.render("Player Yellow won", True, (0, 0, 255)), font.render("Player Blue won", True, (255, 255, 0))
    , font.render("Player Red won", True, (255, 0, 0))]

    home_button = pg.transform.scale(pg.image.load("home_button.png"), (50, 50))

    pg.display.set_icon(main_bg)

    xy_road = [0, 0, 0, 0]
    xy_road[0], xy_road[2], xy_road[1], xy_road[3] = vector()
    xy_road[0] += [(128, 400), (196, 400), (264, 400), (332, 400)]
    xy_road[2] += [(400, 128), (400, 196), (400, 264), (400, 332)]
    xy_road[1] += [(672, 400), (604, 400), (536, 400), (468, 400)]
    xy_road[3] += [(400, 672), (400, 604), (400, 536), (400, 468)]

    first_pos = [[(60, 60), (128, 60), (60, 128), (128, 128)],
    [(672, 672), (740, 672), (672, 740), (740, 740)], 
    [(672, 60), (740, 60), (672, 128), (740, 128)],  
    [(60, 672), (128, 672), (60, 740), (128, 740)]]

    mohre_xy = [[(60, 60), (128, 60), (60, 128), (128, 128)], 
    [(672, 672), (740, 672), (672, 740), (740, 740)],
    [(672, 60), (740, 60), (672, 128), (740, 128)],  
    [(60, 672), (128, 672), (60, 740), (128, 740)]]


    color = [(0, 255, 0), (255, 255, 0), (0, 0, 255), (255, 0, 0)]

    win_pos = [[(128, 400), (196, 400), (264, 400), (332, 400)],  [(672, 400), (604, 400), (536, 400), (468, 400)], [(400, 128), (400, 196), (400, 264), (400, 332)],
    [(400, 672), (400, 604), (400, 536), (400, 468)]]

    for i in range(1, 7):
        dice_number = []
        dice_number.append(pg.transform.scale(pg.image.load("9/dice_green_" + str(i) + ".png"), (74, 74)))
        dice_number.append(pg.transform.scale(pg.image.load("9/dice_yellow_" + str(i) + ".png"), (74, 74)))
        dice_number.append(pg.transform.scale(pg.image.load("9/dice_blue_" + str(i) + ".png"), (74, 74)))
        dice_number.append(pg.transform.scale(pg.image.load("9/dice_red_" + str(i) + ".png"), (74, 74)))
        
        dice_imgs.append(dice_number)

    run = False
    run0 = True
    winner = None
    gamover = False


    while run0:
        win.fill((16, 255, 142))
        win.blit(start_txt, stpos)

        pg.display.update()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run0 = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_p:
                    pg.mixer.music.stop()
            if event.type == pg.MOUSEMOTION:
                xm, ym = event.pos

                if 400 - stw/2 < xm < 400 + stw/2 and 400 - sth/2 < ym < 400 + sth/2:
                    start_txt = font.render("Start", True, (0, 0, 0))
                else:
                    start_txt = font.render("Start", True, (255, 255, 255))

            if event.type == pg.MOUSEBUTTONDOWN:
                gamover = False
                harekat_mohre = None
                player = 3
                dice_flag = None
                xm, ym = event.pos
                turn = 0
                dice_number = [0] * 4
                i_dice = -1
                i_dice_primary = 0
                flag_in = False
                mohre_xy = [[(60, 60), (128, 60), (60, 128), (128, 128)], 
                [(672, 672), (740, 672), (672, 740), (740, 740)],
                [(672, 60), (740, 60), (672, 128), (740, 128)],  
                [(60, 672), (128, 672), (60, 740), (128, 740)]]

                if 400 - stw/2 < xm < 400 + stw/2 and 400 - sth/2 < ym < 400 + sth/2:
                    player, run0 = players(win, font)
                    if run0:
                        run = True                    

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

                    if 375 < xm < 425 and 375 < ym < 425:
                        run = False
                        start_txt = font.render("Start", True, (255, 255, 255))
                    if dice_flag is None:
                        for i in range(len(dice_xy)):
                            if dice_xy[i][0] < xm < dice_xy[i][0] + 74 and dice_xy[i][1] < ym < dice_xy[i][1] + 74 and i == turn:
                                dice_number[i] = rdm.randint(0, 5)
                                dicing(dice_imgs, turn, dice_number[i], win, dice_xy[turn])
                                dice_flag = False
                                for j in mohre_xy[turn]:
                                    if j in xy_road[turn] or dice_number[i] == 5:
                                        dice_flag = True
                                        break

                                if not dice_flag:
                                    dice_flag = None
                                    turn += 1
                                    if turn > player:
                                        turn = 0
                                else:
                                    check = check_turn(mohre_xy[turn], dice_number[i], xy_road[turn])
                                    if not check and dice_number[i] != 5:
                                        dice_flag = None
                                        turn += 1
                                        if turn > player:
                                            turn = 0
                                        time.sleep(1)
                                    elif dice_number[i] == 5 and not check:
                                        dice_flag = None
                            
                    if dice_flag:
                        for j in mohre_xy[turn]:
                            if j[0] - 15 < xm < j[0] + 15 and j[1] - 15 < ym < j[1] + 15:
                                i_dice_primary = None

                                flag_in = False
                                harekat_mohre = mohre_xy[turn].index(j)
                                if j in xy_road[turn]:
                                    i_dice_primary = xy_road[turn].index(j)
                                    flag_in = True
                                else:
                                    if dice_number[turn] + 1 == 6:
                                        i_dice_primary = 0


                                if i_dice_primary is not None and can(xy_road[turn], mohre_xy[turn], dice_number[turn], harekat_mohre):
                                    i_dice = -1
                                    dice_flag = False
                                else:
                                    harekat_mohre = None
                    
            if harekat_mohre is not None:
                time.sleep(0.25)
                i_dice += 1
                mohre_xy[turn][harekat_mohre] = xy_road[turn][i_dice + i_dice_primary]
                if i_dice_primary == 0 and i_dice == 0 and not flag_in:
                    mohre_xy = kill(mohre_xy, turn, harekat_mohre, first_pos)
                    dice_flag = None
                    harekat_mohre = None
                elif i_dice == dice_number[turn] + 1:
                    mohre_xy = kill(mohre_xy, turn, harekat_mohre, first_pos)
                    dice_flag = None
                    if dice_number[turn] != 5:
                        turn += 1
                        if turn > player:
                            turn = 0
                    harekat_mohre = None

            win.blit(main_bg, (0, 0))
            win.blit(dice_imgs[dice_number[turn]][turn], dice_xy[turn])
            for i in range(len(mohre_xy)):
                for j in mohre_xy[i]:
                    pg.draw.circle(win, color[i], j, 15)


            win.blit(home_button, (375, 375))
            pg.display.update()



            for i in range(4):
                for j in win_pos[i]:
                    winner = True
                    if j not in mohre_xy[i]:
                        winner = False
                        break
                if winner == True:
                    winner = i
                    gamover = True
                    break

            if gamover:
                break

        while run and gamover:

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
                    run0 = False
                if event.type == pg.MOUSEBUTTONDOWN:
                    xm, ym = event.pos

                    if 375 < xm < 425 and 375 < ym < 425:
                        run = False
                        start_txt = font.render("Start", True, (255, 255, 255))

            d_win = win_txt[winner].get_rect()
            d_win.center = (400, 400)
            win.fill((172, 70, 89))
            win.blit(win_txt[winner], d_win)
            pg.display.update()
