for event in pygame.event.get():
    #     #Quit
    #     if event.type == pygame.QUIT:
    #         pygame.quit()
    #         sys.exit()
    #     #Check the cursor
    #     if event.type == pygame.MOUSEBUTTONDOWN:
    #         active = input_rect.collidepoint(event.pos)
    #     #Typing...
    #     if event.type == pygame.KEYDOWN:
    #         #The cursor is outside the box text
    #         if active == False:
    #             continue
    #         #Backspace
    #         if event.key == pygame.K_BACKSPACE:
    #             user_text = user_text[:-1]
    #         #Digit
    #         # elif event.unicode.isdigit():
    #         #     checkBoardSize = 0
    #         #     #Adding up the input
    #         #     if user_text != '':
    #         #         checkBoardSize += int(user_text)
    #         #     checkBoardSize = checkBoardSize * 10 + int(event.unicode)
    #         #     #Valid range = [3; 15]
    #         #     if checkBoardSize != 2 and checkBoardSize <= 15:
    #         #         user_text += event.unicode
    #         else :
    #             user_text += event.unicode

    # ##Create the update sence
    # #Create an empty screen
    # screen.fill((0, 0, 0))
    # #Set the cursor color to its status colors
    # if active:
    #     color = color_active
    # else:
    #     color = color_passive
    # # #Draw the rectangle (border only)

    # #Expand the rectangle to the text size
    # text_surface = base_font.render(user_text, True, (255, 255, 255)) 
    # screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
    # input_rect.w = text_surface.get_width() + 10

    # #Update the sence
    # pygame.display.update()
    # fps.tick(60)