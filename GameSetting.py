class Board:
    BOARD_WIDTH = 1000
    BOARD_HEIGHT = 600
    BACKGROUND_COLOR = (3, 252, 165)
    GAME_CAPTION = "Game Caro"


class Menu:
    def CalculateRectSize(ratioPostitionX,ratioPositionY,ratioWidth,ratioHeight):
        width = Board.BOARD_WIDTH*ratioWidth
        height = Board.BOARD_HEIGHT*ratioHeight
        postionX = Board.BOARD_WIDTH* ratioPostitionX - width//2
        postionY = Board.BOARD_HEIGHT*ratioPositionY - height//2
        return (postionX,postionY,width,height)
    
    TITLE_RECT = CalculateRectSize(1/2,2/7,1/5,1/6)
    TITLE_TEXT_SIZE = 100

    PLAY_BUTTON_RECT = CalculateRectSize(1/2,4/7,1/8,1/12)
    PLAY_BUTTON_SIZE = 35

    SETTINGS_BUTTON_RECT = CalculateRectSize(1/2,11/14,1/6,1/12)
    SETTINGS_BUTTON_SIZE = 50

    BUTTON_COLOR = (255, 255, 255)  # White
    BUTTON_TEXT_COLOR = (0, 0, 0)  # Black
    TITLE_TEXT = 'Caro'
    PLAY_TEXT = 'Play game'
    SETTINGS_TEXT = 'Settings'

