from initialized import *
# import random


while True:
      
    screen.blit(backgrounds[current_bg],(0,0))
    pygame.display.set_caption('Angry Birds')

    events=pygame.event.get()
    for event in events:
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:

            '''taking player name input'''

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
                    text_surface_0 = font.render(player0.name, True, MIDNIGHT_BLUE)
                    text_surface_0_Rect = text_surface_0.get_rect(center = (width/4,height/4))
                    input0_bool = False
                elif event.key == pygame.K_BACKSPACE:
                    player0.name = player0.name[:-1]

                else:
                    player0.name += event.unicode

            if active_1:
                if event.key == pygame.K_RETURN:
                    text_surface_1 = font.render(player1.name, True, MAROON)
                    text_surface_1_Rect = text_surface_1.get_rect(center = (3*width/4,height/4))

                    input1_bool = False
                elif event.key == pygame.K_BACKSPACE:
                    player1.name = player1.name[:-1]
                else:
                    player1.name += event.unicode
        
                
        

    mouse = pygame.mouse.get_pos()
    current_time = pygame.time.get_ticks()/1000
    if (play_button.is_clicked()):
        play_button.active = True
    if (quit_button.is_clicked()):
        quit_button.active = True
    if (loading_time == 0):
        current_bg = 1
        for i in range(loaded):
            pygame.mixer.music.play(-1)
            loaded -= 1
        if (play_button.active):
            current_bg = 2
            bs0.create_block_set(bs_0_pos,0,block_side)        
            bs1.create_block_set(bs_1_pos,1,block_side)
            screen.blit(sling0,sling0_rect)
            screen.blit(sling1,sling1_rect)

            if (input0_bool):
                draw_input(screen,input_player0,"Black", "Player1", font,player0.name,input_box,factor_x,factor_y)
            else:
                screen.blit(text_surface_0, text_surface_0_Rect)
                if not red_ability_active:
                    player0.show_birds(screen,width,factor_x,factor_y)                


            if input1_bool:
                draw_input(screen,input_player1,"Black", "Player2", font,player1.name,input_box,factor_x,factor_y)
            else:
                screen.blit(text_surface_1,text_surface_1_Rect)
                if not red_ability_active:
                    player1.show_birds(screen,width,factor_x,factor_y)                
                else:
                    screen.blit(big_red_surface, (width/2 ,100*factor_y))


            if (not(input0_bool or input1_bool)):
                both_inputs_done = True

            if (both_inputs_done):
                if (len(player0.birds)<3):
                    select_birds(player0,red_menu,blue_menu,chuck_menu,bomb_menu,screen,font_menu,red_0,blue_0,chuck_0,bomb_0,factor_y,bird_menu)
                elif (len(player1.birds)<3):
                    select_birds(player1,red_menu,blue_menu,chuck_menu,bomb_menu,screen,font_menu,red_1,blue_1,chuck_1,bomb_1,factor_y,bird_menu)
                elif showing_rules:
                    started_showing = current_time
                    start_show = True
                    game_start_audio.play()
                    if not music_is_paused:
                        pygame.mixer.music.pause()
                        music_is_paused = True
                    showing_rules = False

                elif start_show:
                    time_elapsed  = current_time - started_showing
                    if time_elapsed > 3:
                        start_show = False
                    else:
                        screen.blit(pregame_background,(0,0))
                        begin_game(dim_surface,screen,player0,player1,first_to_zero_surf,time_elapsed,VS,small_font,large_font)
                
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
                        blueA = blueA_0
                        blueB = blueB_0
                        big_red_surface = big_Red_0_surf

                    elif (player1.active):
                        b = player1.birds[player1.current_bird]
                        b_Rect = b.surface.get_rect(center = sling1_center)
                        b.isactive = True
                        target_bs = bs_0_rect
                        target_pos = bs_0_pos
                        target = player0
                        target_side = 0
                        active_player = player1
                        blueA = blueA_1
                        blueB = blueB_1
                        big_red_surface = big_Red_1_surf

            if (player0.score == 0 or player1.score == 0):
                game_over = True
                game_start = False
                if (player1.score > player0.score):
                    winner = player1
                else:
                    winner = player0



            if game_start:
                if not pause_button.active:
                    pause_button.display()
                else:
                    resume_button.display()
                if pause_button.is_clicked():
                    if pause_button.active:
                        pause_button.play_button_sound()
                    pause_button.active = not pause_button.active

                target.show_wind_button(wind_state)
                active_player.show_wind_button(wind_state)

                # playing(font,block_side,b,b_Rect,screen,mouse,active_player,target_side,factor_x,factor_y,target_bs,height,width,bomb_ability_active,max_bomb_usage,target,target_pos,player1,player0,text_surface_1,text_surface_0)
                if (b.isactive):
                    b_Rect.center = (b.x,b.y)
                    if triplify_bool:
                        screen.blit(blueA.surface,blueA_rect)
                        screen.blit(blueB.surface,blueB_rect)
                    if not pause_button.active:
                        if triplify_bool:
                            blueA_rect.center = (blueA.x,blueA.y)
                            blueB_rect.center = (blueB.x,blueB.y)
                            if collide_bird(blueA,target_bs):
                                damage_done(blueA,target_side,target_pos,target,active_player,block_side,Prev_cords_A,False)
                            if collide_bird(blueB,target_bs):
                                damage_done(blueB,target_side,target_pos,target,active_player,block_side,Prev_cords_B,False)
                        if not b.ready:  
                            retry_button.display()

                            launch_bird(b,b_Rect,mouse,active_player.start,factor_x)
                            if (b.being_dragged):
                                b.x = mouse[0]
                                b.y = mouse[1]
                                x_dist = (b.x-active_player.start[0])
                                y_dist = (b.y-active_player.start[1])
                                dist = math.sqrt(x_dist**2+y_dist**2)
                                theta = math.atan2(y_dist,x_dist)
                                if dist > 100*factor_x:
                                    b.x = active_player.start[0] + 100*factor_x*math.cos(theta)
                                    b.y = active_player.start[1] + 100*factor_x*math.sin(theta)
                                show_trajectory(b,active_player.start,30,screen,target_side,factor_x,factor_y)
                                show_stretch(b,active_player.start,screen,factor_x,DARK_BROWN)

                        
                        if collide_bird(b,ground_rect):
                            b.velocity[0] *= 0.7
                            b.velocity[1] *= -0.7
                            b.y = ground_rect.y
                        if triplify_bool:
                            if collide_bird(blueA,ground_rect):
                                blueA.velocity[0] *= 0.7
                                blueA.velocity[1] *= -0.7
                                blueA.y = ground_rect.y
                            if collide_bird(blueB,ground_rect):
                                blueB.velocity[0] *= 0.7
                                blueB.velocity[1] *= -0.7
                                blueB.y = ground_rect.y



                        if collide_bird(b,target_bs):

                            if bomb_ability_active:
                                blast_starts = bomb_ability(b,target,active_player,target_side,target_pos,block_side,target,bomb_audio)
                                start_time = current_time
                                max_bomb_usage -= 1
                                bomb_ability_active = not blast_starts

                            elif red_ability_active:
                                damage_done(b,target_side,target_pos,target,active_player,block_side,Prev_cords,red_ability_active)
                            else:
                                damage_done(b,target_side,target_pos,target,active_player,block_side,Prev_cords,False)

                        Prev_cords = (b.x,b.y)
                        if triplify_bool:
                            Prev_cords_A = (blueA.x,blueA.y)
                            Prev_cords_B = (blueB.x,blueB.y)

                        

                        if b.y > height or b.x < 0 or b.x > width : 
                            switch_players(b,active_player,target,wind_state)
                            if triplify_bool:
                                triplify_bool = False
                                can_active_triplify = True
                            if red_ability_active:
                                b.surface = OGsurf
                                red_ability_active  = False
                            if bomb_ability_active : 
                                bomb_ability_active = False

                        


                    display_score(font,player0,'Black',width,height,factor_y,screen)
                    display_score(font,player1,'Black',width,height,factor_y,screen)

                    screen.blit(b.surface,b_Rect)
                    screen.blit(sling_0_hand,(sling0_rect.x - 5*factor_x,sling0_rect.y-2*factor_y))
                    screen.blit(sling_1_hand,(sling1_rect.x + (sling0x-slinghandx+5)*factor_x,sling1_rect.y-2*factor_y))
                    if blast_starts:
                        t = current_time - start_time
                        if t > 1:
                            blast_starts = False
                            switch_players(b,active_player,target,wind_state)
                        else:
                            blast_surf = pygame.transform.scale(bomb_blast_surf,(player_bird_size*5*t,player_bird_size*5*t))
                            blast_rect = blast_surf.get_rect(center = (b.x,b.y))
                            screen.blit(blast_surf,blast_rect)


                if b.ready and not pause_button.active:

                    if triplify_bool:
                        blueA.update(factor_x,factor_y,wind_state)
                        blueB.update(factor_x,factor_y,wind_state)

                    b.update(factor_x,factor_y,wind_state)
                    if pygame.mouse.get_pressed()[2]:
                        if b.type == 2 and max_bomb_usage>0:
                            bomb_ability_active = True
                        if b.type==1:    
                            speed_ability(b)
                        if b.type == 3 and can_active_triplify ==True:
                            triplify_bool = True
                            can_active_triplify = False
                            (blueA.x,blueA.y) = (b.x,b.y + block_side/2)
                            (blueB.x,blueB.y) = (b.x,b.y - block_side/2)
                            b.velocity[0] *= 0.75
                            b.velocity[1] *= 0.75
                            blueA.velocity = b.velocity.copy()
                            blueB.velocity = b.velocity.copy()
                            blueA.isactive = blueB.isactive = True
                            blueA_rect = blueA.surface.get_rect(center = (blueA.x,blueA.y))
                            blueB_rect = blueB.surface.get_rect(center = (blueB.x,blueB.y))
                        if b.type == 0 and active_player.max_big_red_active > 0:
                            active_player.max_big_red_active -= 1
                            red_ability_active = True
                            OGsurf = pygame.transform.flip((pygame.transform.scale(b.surface1, (player_bird_size,player_bird_size))),flip_x=not target_side,flip_y=False)
                            b.surface = big_red_surface
                    
                    speed = math.sqrt(b.velocity[0]**2 + b.velocity[1]**2)
                    if 2.5*factor_x>speed >= 0:
                        if triplify_bool:
                            triplify_bool = False
                            can_active_triplify = True
                        bomb_ability_active = False

                        if puff_timer != 0 :
                            if puff_timer == 102:
                                puff_audio.play()
                            puff_Rect = puff_list[(puff_timer//25)%2].get_rect(center = (b.x,b.y))
                            screen.blit(puff_list[(puff_timer//25)%2],puff_Rect)
                            puff_timer -= 3
                        else:
                            puff_timer = 102
                            switch_players(b,active_player,target,wind_state)
                            if red_ability_active:
                                b.surface = OGsurf
                                red_ability_active  = False
                    if check_if_stuck(b,target_bs,Prev_cords,factor_x,active_player,target,wind_state):
                        if triplify_bool:
                            triplify_bool = False
                            can_active_triplify = True
                        if red_ability_active:
                            b.surface = OGsurf
                            red_ability_active  = False
                        if bomb_ability_active : 
                            bomb_ability_active = False
                else:                 
                    if (retry_button.is_clicked()):
                        wind_state = [False,None]
                        # if red_ability_active:
                        #     b.surface = OGsurf
                        bomb_ability_active = False
                        triplify_bool = False
                        max_bomb_usage = random.randint(0,5)
                        red_ability_active = False
                        can_active_triplify = True
                        player0.reset()
                        player1.reset()
                        random_player_activation(player1,player0)




        else:
            screen.blit(logo_surf,logo_rect)
            play_button.display()
    else:
        loading_time -= 1
        pygame.draw.line(screen,"White",(width/4,3*height/4),(3*width/4 - (loading_time**2/900)*factor_x,3*height/4),int(50*factor_y))

    
    if game_over:
        if music_is_paused:
            pygame.mixer.music.unpause()
        display_score(font,player0,'Black',width,height,factor_y,screen)
        display_score(font,player1,'Black',width,height,factor_y,screen)
        screen.blit(dim_surface,(0,0))

        if (winner_timer < 0):
            winner_display(winner,screen,font_winner,factor_x)
            new_game_button.display()
            if new_game_button.is_clicked():
                os.execv(sys.executable, [sys.executable] + sys.argv)

        else:
            if not played_game_over:
                game_over_audio.play()
                played_game_over = not played_game_over
            screen.blit(game_over_logo,game_over_logo_rect)
            winner_timer-=3

 
 
    if (quit_button.active):
        pygame.quit()
        sys.exit()
    else:
        quit_button.display()



    pygame.display.update()
    clock.tick(1200)


