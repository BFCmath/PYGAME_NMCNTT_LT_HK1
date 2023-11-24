class Board:
    BOARD_WIDTH = 1000
    BOARD_HEIGHT = 600
    BACKGROUND_COLOR = (137, 165, 97)
    GAME_CAPTION = "Game Caro"

def calculate_rect_size(ratioPostitionX,ratioPositionY,ratioWidth,ratioHeight):
        _width = Board.BOARD_WIDTH*ratioWidth
        _height = Board.BOARD_HEIGHT*ratioHeight
        _postionX = Board.BOARD_WIDTH* ratioPostitionX - _width//2
        _postionY = Board.BOARD_HEIGHT*ratioPositionY - _height//2
        return (_postionX,_postionY,_width,_height)
        
class Menu:
    
    TITLE_RECT = calculate_rect_size(1/2,2/7,1/5,1/6)
    TITLE_TEXT_SIZE = 80

    PLAY_BUTTON_RECT = calculate_rect_size(1/2,4/7,1/8,1/12)
    PLAY_BUTTON_SIZE = 35

    SETTINGS_BUTTON_RECT = calculate_rect_size(1/2,11/14,1/6,1/12)
    SETTINGS_BUTTON_SIZE = 50

    BUTTON_COLOR = (255, 255, 255)  # White
    BUTTON_TEXT_COLOR = (0, 0, 0)  # Black
    TITLE_TEXT = 'Caro'
    PLAY_TEXT = 'Play game'
    SETTINGS_TEXT = 'Settings'

