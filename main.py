from initialized import *


while  running:
    events=pygame.event.get()
    for event in events:
        if event.type==pygame.QUIT:
            running=False
            pygame.quit()
            sys.exit()

    mouse = pygame.mouse.get_pos()
    screen.blit(background,(0,0))
    pygame.display.set_caption('Angry Birds')
    if (play_button.is_clicked()):
        play_button.active = True
    if (play_button.active):
        bs0.create_block_set(bs_0_pos,0)
        bs1.create_block_set(bs_1_pos,1)
        screen.blit(sling0,sling0_rect)
        screen.blit(sling1,sling1_rect)
        b_Rect.center = (b.x,b.y)
        if (b.isactive):
            screen.blit(b.surface,b_Rect)

            launch_bird(b,b_Rect,mouse,sling1_center)
            if collide_bird(b,bs_0_rect):
                damage_done(b,bs_0_rect,0,bs_0_pos,bs0)

        if b.ready: b.update()
    else:
        play_button.display()



    #Intro Screen




    # bs0.create_block_set(bs_0_pos,0)
    # bs1.create_block_set(bs_1_pos,1)
    # screen.blit(sling0,sling0_rect)
    # screen.blit(sling1,sling1_rect)
    # b_Rect.center = (b.x,b.y)
    # if (b.isactive):
    #     screen.blit(b.surface,b_Rect)

    #     launch_bird(b,b_Rect,mouse,sling1_center)
    #     if collide_bird(b,bs_0_rect):
    #         damage_done(b,bs_0_rect,0,bs_0_pos,bs0)

    # if b.ready: b.update()
    pygame.display.update()
    clock.tick(600)


