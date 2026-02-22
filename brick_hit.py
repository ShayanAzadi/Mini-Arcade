import pygame as pg, random as rdm, time


def brick_hit():
    def calculator(x, y, ball_pos):
        ekh_x = x - ball_pos[0]
        ekh_y = y - ball_pos[1]

        if abs(ekh_x) > abs(ekh_y):
            if ekh_x > 0:
                return [10], [ekh_y / ekh_x * 10]
            return [-10], [ekh_y / ekh_x * -10]

        return [ekh_x / ekh_y * -10], [-10]

    def y(ls):
        for i in range(len(ls)):
            ls[i] = (ls[i][0], ls[i][1] + 32)
        
        return ls, ls[0][1]

    def make_box(ls : list):
        ls2 = [True, False]
        ls3 = []
        ls4 = []
        x = 10
        t = 0
        for i in range(10):
            if rdm.choice(ls2):
                ls3.append((x, 40))
                t += 1
            else:
                ls4.append((x + 15, 55))
            x += 32
        if len(ls3) == 10:
            return ls + ls3, t, None
        return ls + ls3, t, rdm.choice(ls4)

    pg.init()

    home_button = pg.transform.scale(pg.image.load("home_button.png"), (50, 50))

    disp = pg.display.set_mode((338, 500))
    font = pg.font.Font("freesansbold.ttf", 16)
    font2 = pg.font.Font("ARLRDBD.TTF", 34)
    start = font2.render('Start' , True , (0, 0, 0))
    spos = start.get_rect()
    spos.center = (169, 250)

    hs = start.get_height()
    ws = start.get_width()


    run0 = True
    run = False
    score = 0

    while run0:

        for event in pg.event.get():

            if event.type == pg.QUIT:
                run0 = False

            if event.type == pg.MOUSEMOTION:
                xm, ym = event.pos

                if 169 - ws/2 < xm < 169 + ws/2 and 250 - hs/2 < ym < 250 + hs/2:
                    start = font2.render('Start' , True , (255, 255, 255))
                else:
                    start = font2.render('Start' , True , (0, 0, 0))

                  
            if event.type == pg.MOUSEBUTTONDOWN :
                xm, ym = event.pos

                if 169 - ws/2 < xm < 169 + ws/2 and 250 - hs/2 < ym < 250 + hs/2:

                    xy_box, a, b = make_box([])
                    if b != None:
                        xy_ball_adder = [b]
                    else:
                        xy_ball_adder = []
                    xy_ball = [(169, 414)] * 35
                    counter = [len(xy_ball)] * a
                    bool_flag_i = [False] * len(xy_ball)
                    speed_x_ball, speed_y_ball = [0] * len(xy_ball), [-10] * len(xy_ball)
                    i_ball = -1
                    ball_add = 0
                    activate_flag = False
                    lvl = False
                    run = True
                    flag = False
                    end_flag = False
                    score = 0


        disp.fill((200, 200, 200))
        disp.blit(start, spos)
        pg.display.update()

        while run:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
                    run0 = False

                if event.type == pg.MOUSEBUTTONDOWN:
                    xm, ym = event.pos

                    if 283 <= xm <= 283 + 50 and 435 <= ym <= 435 + 50:
                        run = False
                        start = font2.render('Start' , True , (0, 0, 0))
                    
                    else:
                        flag = True
                
                if event.type == pg.MOUSEBUTTONUP and True not in bool_flag_i and i_ball == -1 and flag:
                    xm, ym = event.pos

                    speed_x_ball, speed_y_ball = calculator(xm, ym, xy_ball[0])
                    if speed_y_ball != [0]:
                        speed_x_ball *= len(xy_ball)
                        speed_y_ball *= len(xy_ball)
                        bool_flag_i = [False] * len(xy_ball)
                        activate_flag = True
                    
                    flag = False
            
            if (True in bool_flag_i and i_ball < len(xy_ball) - 1) or activate_flag:
                i_ball += 1
                activate_flag = False
                bool_flag_i[i_ball] = True
            
            if True not in bool_flag_i and i_ball == len(xy_ball) - 1:
                i_ball = -1
                lvl = True
            
            disp.fill((200, 200, 200))

            for ballAdder in xy_ball_adder:
                pg.draw.circle(disp, (255, 255, 255), ballAdder, 15)

            for box in range(len(xy_box)):
                pg.draw.rect(disp, (188, 158, 130), (xy_box[box], (30, 30)))
                text = font.render(str(counter[box]), True, (0, 0, 0))
                d_txt = text.get_rect()
                d_txt.center = (xy_box[box][0] + 15, xy_box[box][1] + 15)
                disp.blit(text, d_txt)

            pg.draw.line(disp, (255, 255, 255), (0, 420), (338, 420))
            
            if end_flag:
                pg.display.update()
                time.sleep(1)
                break

            for ball in range(len(xy_ball)):
                if bool_flag_i[ball]:
                    xy_ball[ball] = (xy_ball[ball][0] + speed_x_ball[ball], xy_ball[ball][1] + speed_y_ball[ball])
                    if xy_ball[ball][1] + 5 >= 419:
                        bool_flag_i[ball] = False
                
                if (xy_ball[ball][0] - 5 <= 10 and speed_x_ball[ball] < 0) or (xy_ball[ball][0] + 5 >= 328 and speed_x_ball[ball] > 0):
                    speed_x_ball[ball] *= -1
                if xy_ball[ball][1] - 5 <= 10:
                    speed_y_ball[ball] *= -1

                j = 0
                for i in range(len(xy_box)):
                    if xy_box[i - j][0] <= xy_ball[ball][0] - 5 <= xy_box[i - j][0] + 30 or xy_box[i - j][0] <= xy_ball[ball][0] + 5 <= xy_box[i - j][0] + 30:
                        if xy_box[i - j][1] <= xy_ball[ball][1] - 5 <= xy_box[i - j][1] + 30 or xy_box[i - j][1] <= xy_ball[ball][1] + 5 <= xy_box[i - j][1] + 30:

                            if xy_box[i - j][0] >= xy_ball[ball][0] - 5 and speed_x_ball[ball] > 0:
                                speed_x_ball[ball] *= -1
                            elif xy_box[i - j][0] + 30 <= xy_ball[ball][0] + 5 and speed_x_ball[ball] < 0:
                                speed_x_ball[ball] *= -1
                            if xy_box[i - j][1] >= xy_ball[ball][1] - 5 and speed_y_ball[ball] > 0:
                                speed_y_ball[ball] *= -1
                            elif xy_box[i - j][1] + 30 <= xy_ball[ball][1] + 5 and speed_y_ball[ball] < 0:
                                speed_y_ball[ball] *= -1

                            score += 1
                            counter[i - j] -= 1
                            if counter[i - j] == 0:
                                xy_box.pop(i - j)
                                counter.pop(i - j)
                                j += 1
                j = 0
                for i in range(len(xy_ball_adder)):
                    if xy_ball_adder[i - j][0] - 15 < xy_ball[ball][0] - 5  < xy_ball_adder[i - j][0] + 15 or xy_ball_adder[i - j][0] - 15 < xy_ball[ball][0] + 5 < xy_ball_adder[i - j][0] + 15:
                        if xy_ball_adder[i - j][1] - 15 < xy_ball[ball][1] - 5  < xy_ball_adder[i - j][1] + 15 or xy_ball_adder[i - j][1] - 15 < xy_ball[ball][1] + 5 < xy_ball_adder[i - j][1] + 15:
                            ball_add += 1
                            xy_ball_adder.pop(i - j)
                            j += 1
                            break

                pg.draw.circle(disp, (240, 240, 240), xy_ball[ball], 5)

            
            score_txt = font2.render("Score: " + str(score), True, (0, 0, 0))
            width_score_txt = score_txt.get_width()

            scorepos = score_txt.get_rect()
            scorepos.center = (10 + width_score_txt / 2, 460)

            disp.blit(home_button, (283, 435))
            disp.blit(score_txt, scorepos)

            pg.draw.line(disp, (255, 255, 255), (0, 420), (338, 420))
            pg.display.update()
            pg.time.Clock().tick(80)

            if lvl:
                xy_ball = [(rdm.randint(30, 308), 414)] * (len(xy_ball) + ball_add)
                bool_flag_i += [False] * (len(xy_ball) + ball_add)
                lvl = False
                finish = 0
                if len(xy_box) != 0:
                    xy_box, finish = y(xy_box)
                c = 0
                if len(xy_ball_adder) != 0:
                    xy_ball_adder, c = y(xy_ball_adder)
                xy_box, a, b = make_box(xy_box)
                if b != None:
                    xy_ball_adder += [b]
                if c == 392 + 15:
                    xy_ball_adder.pop(0)
                if finish == 392:
                    end_flag = True

                counter += [len(xy_ball)] * a
                ball_add = 0
        

        end_txt = font2.render("Score: " + str(score), True, (0, 0, 0))
        endpos = end_txt.get_rect()
        endpos.center = (169, 250)

        while run:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
                    run0 = False

                if event.type == pg.MOUSEBUTTONDOWN:
                    xm, ym = event.pos

                    if 10 <= xm <= 60 and 10 <= ym <= 60:
                        run = False
                        start = font2.render('Start' , True , (0, 0, 0))
            disp.fill((200, 200, 200))
            disp.blit(end_txt, endpos)
            disp.blit(home_button, (10, 10))
            pg.display.update()
