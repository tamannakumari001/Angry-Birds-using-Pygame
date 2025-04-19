from initialized import *
# import random


while True:
        
    screen.blit(background,(0,0))
    pygame.display.set_caption('Angry Birds')

    events=pygame.event.get()
    for event in events:
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if input_player0.collidepoint(event.pos):
                active_0 = True
                active_1 = False
            elif input_player1.collidepoint(event.pos):
                active_1 =True
                active_0 = False
            else:
                active_0 =False
                active_1 =False
        elif event.type == pygame.KEYDOWN:
            if active_0:
                if event.key == pygame.K_RETURN:
                    text_surface_0 = font.render(player0.name, True, "Black")
                    # score_0 = font.render(str(player0.score), True, "Black")
                    # score_0_Rect = text_surface_0.get_rect(center = (width/4,height/4+50))
                    text_surface_0_Rect = text_surface_0.get_rect(center = (width/4,height/4))
                    input0_bool = False
                elif event.key == pygame.K_BACKSPACE:
                    player0.name = player0.name[:-1]
                else:
                    player0.name += event.unicode

            if active_1:
                if event.key == pygame.K_RETURN:
                    text_surface_1 = font.render(player1.name, True, "Black")
                    text_surface_1_Rect = text_surface_1.get_rect(center = (3*width/4,height/4))
                    # score_1 = font.render(str(player1.score), True, "Black")
                    # score_1_Rect = text_surface_1.get_rect(center = (3*width/4,height/4+50))


                    input1_bool = False
                elif event.key == pygame.K_BACKSPACE:
                    player1.name = player1.name[:-1]
                else:
                    player1.name += event.unicode
        
                
        

    mouse = pygame.mouse.get_pos()
    if (play_button.is_clicked()):
        play_button.active = True
    if (quit_button.is_clicked()):
        quit_button.active = True
    if (play_button.active):


        if (input0_bool):
            draw_input(screen,input_player0,"Black", "Player1", font,player0.name,input_box)
        else:
            screen.blit(text_surface_0, text_surface_0_Rect)
            for index in range(len(player0.birds)):
                screen.blit(player0.birds[index].surface, (width/2 -200-100*index,100))


        if input1_bool:
            draw_input(screen,input_player1,"Black", "Player2", font,player1.name,input_box)
        else:
            screen.blit(text_surface_1,text_surface_1_Rect)
            for index in range(len(player1.birds)):
                screen.blit(player1.birds[index].surface, (width/2 + 160 + 100*index,100))


        if (not(input0_bool or input1_bool)):
            both_inputs_done = True

        if (both_inputs_done):
            if (len(player0.birds)<3):
                select_birds(player0,red_menu,blue_menu,chuck_menu,bomb_menu,screen,font_menu,red_0,blue_0,chuck_0,bomb_0)
            elif (len(player1.birds)<3):
                select_birds(player1,red_menu,blue_menu,chuck_menu,bomb_menu,screen,font_menu,red_1,blue_1,chuck_1,bomb_1)
            else:
                game_start = True
                if (player0.active):
                    b = player0.birds[player0.current_bird]
                    b_Rect = b.surface.get_rect(center = sling1_center)
                    b.isactive = True
                    target_bs = bs_1_rect
                    target_pos = bs_1_pos
                    target = player1
                    target_side = 1
                    active_player = player0

                elif (player1.active):
                    b = player1.birds[player1.current_bird]
                    b_Rect = b.surface.get_rect(center = sling1_center)
                    b.isactive = True
                    target_bs = bs_0_rect
                    target_pos = bs_0_pos
                    target = player0
                    target_side = 0
                    active_player = player1

        if (player0.score == 0 or player1.score == 0):
            game_over = True
            game_start = False
            if (player1.score > player0.score):
                winner = player1
            else:
                winner = player0



        bs0.create_block_set(bs_0_pos,0)
        bs1.create_block_set(bs_1_pos,1)
        screen.blit(sling0,sling0_rect)
        screen.blit(sling1,sling1_rect)

        if game_start:

            if (b.isactive):
                b_Rect.center = (b.x,b.y)
                screen.blit(b.surface,b_Rect)
                launch_bird(b,b_Rect,mouse,active_player.start,target_side)
                if (b.being_dragged):
                    show_trajectory(b,active_player.start,5,screen,target_side)
                if collide_bird(b,target_bs):
                    damage_done(b,target_side,target_pos,target,active_player)
                if b.y > height or b.x < 0 or b.x > width : 
                    b.isactive = False
                    b.ready = False
                    b.being_dragged = False
                    active_player.deactivate_player()
                    target.activate_player()



                    

                score_1 = font.render(str(player1.score), True, "Black")
                score_1_Rect = text_surface_1.get_rect(center = (3*width/4,height/4+50))
                score_0 = font.render(str(player0.score), True, "Black")
                score_0_Rect = text_surface_0.get_rect(center = (width/4,height/4+50))


                screen.blit(score_1, score_1_Rect)  
                screen.blit(score_0, score_0_Rect)


            if b.ready: b.update()
    else:
        play_button.display()
    
    if game_over:
        screen.blit(score_1, score_1_Rect)  
        screen.blit(score_0, score_0_Rect)
        winner_display(winner,screen,font_winner)
 
 
    if (quit_button.active):
        pygame.quit()
        sys.exit()
    else:
        quit_button.display()

    pygame.display.update()
    clock.tick(6000)


