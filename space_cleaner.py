import pygame as pg, random, time


def space_cleaner():
    class space_objects:
        
        def __init__(self, x, y, img, width, height, destroy, movement):
            self.x = x
            self.y = y
            self.img = img
            self.width = width
            self.height = height
            self.destroy = destroy
            self.movement = movement

        def blit_img(self, disp):
            disp.blit(self.img, (self.x, self.y))



    def create_space_object(space_objects_list):
        ls = [True, True, True, True, False]


        for i in range(1):

            if random.choice(ls):
                destroy = True
                obj_img = meteorite_img

            else:
                obj_img = random.choice(space_object_image_list)
                destroy = False
            

            obj_img_width = obj_img.get_width()
            obj_img_height = obj_img.get_height()

            x = random.randint(0, display_width - obj_img_width - 5)
            y = 0 - obj_img_height

            movement = random.randint(5, 8)

            new_space_obj = space_objects(x, y, obj_img, obj_img_width, obj_img_height, destroy, movement)


            space_objects_list.append(new_space_obj)
            return space_objects_list




    pg.init()


    display_width = 500
    display_height = 600


    disp = pg.display.set_mode((display_width, display_height))
    pg.display.set_caption("Space Cleaner")


    background_img = pg.transform.scale(pg.image.load("10/background.jpeg"), (500, 600))
    home_btn = pg.transform.scale(pg.image.load("10/home_button.png"), (50, 50))
    meteorite_img = pg.transform.scale(pg.image.load("10/meteorite.png"), (60, 135))
    satellite1_img = pg.transform.scale(pg.image.load("10/satellite1.png"), (30, 96.2))
    satellite2_img = pg.transform.scale(pg.image.load("10/satellite2.png"), (65, 68.8))
    spaceship_img = pg.transform.scale(pg.image.load("10/spaceship.png"), (40, 69.1))
    rocket_img = pg.transform.scale(pg.image.load("10/rocket.png"), (40, 100.5))
    recycle_bin_img = pg.transform.scale(pg.image.load("10/recycle_bin.png"), (50, 50))

    space_object_image_list = [satellite1_img, satellite2_img, spaceship_img, rocket_img]
    space_objects_list = []


    font = pg.font.Font("ARLRDBD.TTF", 50)
    font2 = pg.font.Font("ARLRDBD.TTF", 30)


    pg.display.set_icon(recycle_bin_img)


    start_txt = font.render("Start", True, (255, 255, 255))

    start_txt_pos = start_txt.get_rect()
    start_txt_pos.center = (display_width / 2, display_height / 2)

    start_txt_height = start_txt.get_height()
    start_txt_width = start_txt.get_width()


    score = 0


    run_menu = True
    run_game = False

    while run_menu:

        for event in pg.event.get():
            
            if event.type == pg.QUIT:
                run_menu = False

            if event.type == pg.MOUSEMOTION:
                
                xmouse, ymouse = event.pos

                if display_width / 2 - start_txt_width / 2 <= xmouse <= display_width / 2 + start_txt_width / 2 and display_height / 2 - start_txt_height / 2 <= ymouse <= display_height / 2 + start_txt_height / 2: 
                    start_txt = font.render("Start", True, (0, 0, 0))

                else:
                    start_txt = font.render("Start", True, (255, 255, 255))


            if event.type == pg.MOUSEBUTTONDOWN:

                xmouse, youse = event.pos

                if display_width / 2 - start_txt_width / 2 <= xmouse <= display_width / 2 + start_txt_width / 2 and display_height / 2 - start_txt_height / 2 <= ymouse <= display_height / 2 + start_txt_height / 2: 
                    run_game = True
                    score = 0
                    movement_player = 0
                    x_player = 225
                    y_player = 460
                    space_objects_list = []
                    start_spawn_obj_timer = time.time()
                    game_over = False

        
        disp.blit(background_img, (0, 0))
        disp.blit(start_txt, start_txt_pos)

        pg.display.update()




        while run_game:
            
            for event in pg.event.get():

                if event.type == pg.QUIT:
                    run_game = run_menu = False

                if event.type == pg.MOUSEBUTTONDOWN:

                    xmouse, ymouse = event.pos 

                    if display_width - 70 <= xmouse <= display_width - 20 and display_height - 70 <= ymouse <= display_height - 20:
                        run_game = False
                        start_txt = font.render("Start", True, (255, 255, 255))

                
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_LEFT:
                        movement_player = -3

                    if event.key == pg.K_RIGHT:
                        movement_player = 3

                if event.type == pg.KEYUP:
                    if event.key == pg.K_RIGHT or event.key == pg.K_LEFT:
                        movement_player = 0


            disp.blit(background_img, (0, 0))


            if movement_player > 0 and x_player + 50 < display_width - 5:
                x_player += movement_player

            if movement_player < 0 and x_player > 5:
                x_player += movement_player


            if time.time() - start_spawn_obj_timer >= 0.5:
                space_objects_list = create_space_object(space_objects_list).copy()
                start_spawn_obj_timer = time.time()


            remove_ls = []

            for i, space_obj in enumerate(space_objects_list):
                space_obj.blit_img(disp)

                if space_obj.x <= x_player <= space_obj.x + space_obj.width or space_obj.x <= x_player + 50 <= space_obj.x + space_obj.width:
                    if space_obj.y <= y_player <= space_obj.y + space_obj.height or space_obj.y <= y_player + 50 <= space_obj.y + space_obj.height:

                        if space_obj.destroy:
                            game_over = True
                            break

                        else:
                            score += 1
                            remove_ls.append(i)
                            continue

                elif x_player <= space_obj.x <= x_player + 50 or x_player <= space_obj.x + space_obj.width <= x_player + 50:
                    if y_player <= space_obj.y <= y_player + 50 or y_player <= space_obj.y + space_obj.height <= y_player + 50:

                        if space_obj.destroy:
                            game_over = True
                            break

                        else:
                            score += 1
                            remove_ls.append(i)
                            continue

                space_obj.y += space_obj.movement

                if space_obj.y >= 505:
                    remove_ls.append(i)

            j = 0

            for i in remove_ls:
                space_objects_list.pop(i - j)
                j += 1



            score_txt = font2.render(f"Score: {score}", True, (255, 255, 255))
            score_txt_height = score_txt.get_height()
            score_txt_width = score_txt.get_width()
            score_txt_pos = score_txt.get_rect()
            score_txt_pos.center = (20 + score_txt_width / 2, 580 - score_txt_height / 2)


            disp.blit(score_txt, score_txt_pos)
            disp.blit(home_btn, (display_width - 70, display_height - 70))
            disp.blit(recycle_bin_img, (x_player, y_player))
            
            pg.draw.line(disp, (255, 255, 255), (0, display_height - 90 + 1.5), (display_width, display_height - 90 + 1.5), 3)

            pg.time.Clock().tick(80)
            pg.display.update()

            if game_over:
                end_txt = font.render("Score: " + str(score), True, (255, 255, 255))
                endpos = end_txt.get_rect()
                endpos.center = (display_width / 2, display_height / 2)
                time.sleep(1)
                break


        while run_game:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run_game = False
                    run_menu = False

                if event.type == pg.MOUSEBUTTONDOWN:
                    xmouse, ymouse = event.pos

                    if 10 <= xmouse <= 60 and 10 <= ymouse <= 60:
                        run_game = False
                        start_txt = font.render('Start' , True , (255, 255, 255))

            disp.blit(background_img, (0, 0))
            disp.blit(end_txt, endpos)
            disp.blit(home_btn, (10, 10))
            pg.display.update()

