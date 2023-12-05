def calculate_rect_size(ratioPostitionX,ratioPositionY,ratioWidth,ratioHeight):
        _width = Board.BOARD_WIDTH*ratioWidth
        _height = Board.BOARD_HEIGHT*ratioHeight
        _postionX = Board.BOARD_WIDTH* ratioPostitionX - _width//2
        _postionY = Board.BOARD_HEIGHT*ratioPositionY - _height//2
        return (_postionX,_postionY,_width,_height)
def calculate_square_size(ratioPostitionX,ratioPositionY,ratioEdge):
        _edge = Board.BOARD_WIDTH*ratioEdge
        _postionX = Board.BOARD_WIDTH* ratioPostitionX - _edge//2
        _postionY = Board.BOARD_HEIGHT*ratioPositionY - _edge//2
        return (_postionX,_postionY,_edge,_edge)
def calculate_hover_size(rect,addition_width,addition_height):
    x, y, width, height = rect
    new_width = width + addition_width
    new_height = height + addition_height
    new_x = x - addition_width // 2
    new_y = y - addition_height // 2
    return (new_x, new_y, new_width, new_height)
     
class Board:
    BOARD_WIDTH = 1000
    BOARD_HEIGHT = 600
    BACKGROUND_COLOR = (137, 165, 97)
    GAME_CAPTION = "Game Caro"

class Intro:
    LOGO_RECT = calculate_rect_size(1/2,1/2,1/3,1/3)
    LOGO_IMAGE = '__others\logo_caro.jpg'
    LOGO_IMAGE_SIZE = (400,400)
    LOGO_BACKGROUND_COLOR = (255,255,255)
    LOGO_BORDER_COLOR = (0,0,0)

    LOADING_BAR_RECT = calculate_rect_size(1/2,0.9,1/2,1/20)
    LOADING_BAR_COLOR = (0, 128, 0)
    LOADING_BAR_BACKGROUND_COLOR = (128, 128, 128)
    LOADING_TIME = 1000
    
class Menu:
    TITLE_RECT = calculate_rect_size(1/2,2/7,1/5,1/6)
    TITLE_TEXT_SIZE = 50

    PLAY_BUTTON_RECT = calculate_rect_size(1/2,4/7,2/11,1/12)
    PLAY_BUTTON_SIZE = 20
    PLAY_HOVER_BUTTON_RECT = calculate_hover_size(PLAY_BUTTON_RECT, 50, 20)

    SETTINGS_BUTTON_RECT = calculate_rect_size(1/2,11/14,1/8,1/13)
    SETTINGS_BUTTON_SIZE = 13
    SETTINGS_HOVER_BUTTON_RECT = calculate_hover_size(SETTINGS_BUTTON_RECT, 40, 10)

    QUIT_BUTTON_RECT = calculate_rect_size(1/2,0.9,0.1,0.05)
    QUIT_BUTTON_SIZE = 13
    QUIT_HOVER_BUTTON_RECT = calculate_hover_size(QUIT_BUTTON_RECT, 30, 10)

    BUTTON_COLOR = (255, 255, 255)  # White
    BUTTON_TEXT_COLOR = (0, 0, 0)  # Black
    TITLE_TEXT = 'Caro'
    PLAY_TEXT = 'Play game'
    SETTINGS_TEXT = 'Settings'
    QUIT_TEXT = 'Quit'
    FONT = '__others\kongtext.ttf'

class Settings:
    SETTINGS_TITLE_RECT = calculate_rect_size(1/2,1/7,1/3,1/6)
    SETTINGS_TITLE_TEXT_SIZE = 40
    
    SETTINGS_BACK_BUTTON_RECT = calculate_rect_size(1/2,11/14,1/6,1/12)
    SETTINGS_BACK_BUTTON_SIZE = 25
    SETTINGS_BACK_HOVER_BUTTON_RECT = calculate_hover_size(SETTINGS_BACK_BUTTON_RECT, 50, 20)

    SETTINGS_BOARD_SIZE_RECT = calculate_rect_size(1/2,2.75/7,1/4,1/12)
    SETTINGS_BOARD_SIZE_TEXT_SIZE = 15
    
    SETTINGS_X_PLACE = (0.5,0.5)
    SETTINGS_X_SIZE = 20
    
    SETTINGS_INPUT_BOX_RECT_1 = calculate_square_size(SETTINGS_X_PLACE[0]-0.035,SETTINGS_X_PLACE[1],0.04)
    SETTINGS_INPUT_BOX_RECT_2 = calculate_square_size(SETTINGS_X_PLACE[0]+0.035,SETTINGS_X_PLACE[1],0.04)
    
    SETTINGS_NAME_INPUT_BOX_RECT_1 = (220,172,220,25)
    SETTINGS_NAME_INPUT_BOX_RECT_2 = (Board.BOARD_WIDTH-SETTINGS_NAME_INPUT_BOX_RECT_1[0]-SETTINGS_NAME_INPUT_BOX_RECT_1[2],SETTINGS_NAME_INPUT_BOX_RECT_1[1],220,25)
    ACTIVE_COLOR_INPUT_BOX = (255, 255, 145)  # White
    PASSIVE_COLOR_INPUT_BOX = (0, 0, 0)  # Black
    INPUT_BOX_BACKGROUND_COLOR = (255, 255, 255)  # Black
    INPUT_BOX_TEXT_COLOR = (111,111, 111)  # Gray
    SETTINGS_INPUT_BOX_TEXT_SIZE = 15
    
    NAME_PLACE_1 = (SETTINGS_NAME_INPUT_BOX_RECT_1[0],SETTINGS_NAME_INPUT_BOX_RECT_1[1]-15)
    NAME_PLACE_2 = (SETTINGS_NAME_INPUT_BOX_RECT_2[0],SETTINGS_NAME_INPUT_BOX_RECT_2[1]-15)
    NAME_SIZE = 10
    NAME_1 = 'User1\'s name:'
    NAME_2 = 'User2\'s name:'

    MAX_CARO_BOARD_SIZE = 30
    MIN_CARO_BOARD_SIZE = 5
    
    LIMIT_OF_NAME = 13
    SETTINGS_BUTTON_COLOR = (255, 255, 255) 
    SETTINGS_BUTTON_TEXT_COLOR = (0, 0, 10) 
    SETTINGS_INPUT_BOX_COLOR = (0, 0, 0) 
    SETTINGS_TITLE_TEXT = 'SETTINGS'
    SETTINGS_BACK_TEXT = 'Back' 
    SETTINGS_BOARD_SIZE_TEXT = 'Caro board size'
    SETTINGS_COLOR = (152,118,246)
    FONT = '__others\kongtext.ttf'


class PlayGame:
    
    TURN_TEXT_POSITION = (10, 10)
    BACK_BUTTON_RECT = calculate_rect_size(0.925,0.05,1/10,1/20)
    BACK_BUTTON_COLOR = (255, 255, 255)  # White
    BACK_TEXT_COLOR = (0,0,0)
    BACK_HOVER_BUTTON_RECT = calculate_hover_size(BACK_BUTTON_RECT, 10, 6)
    BACK_TEXT = 'Back'
    PLAYER1_TEXT_POSITION = (10, Board.BOARD_HEIGHT - 40)
    PLAYER2_TEXT_POSITION = (Board.BOARD_WIDTH - 10, Board.BOARD_HEIGHT - 40)
    PLAYER1_TEXT = 'Player 1: X'
    PLAYER2_TEXT = 'Player 2: O'
    BACKGROUND_COLOR = (123, 179, 243)
    
    
    TEXT_SIZE = 16
    TEXT_COLOR = (0, 0, 0)
    FONT = '__others\kongtext.ttf'

    CARO_BOARD_WIDTH = 900
    CARO_BOARD_HEIGHT = 500

    

class CellSetting:
    CELL_COLOR = (255, 255, 255)  # White
    CELL_TEXT_COLOR = (0, 0, 0)  # Black
    EDGE_COLOR = (0, 0, 0)  # Black
    SIGN_COLOR = [(46,165,205),(232,15,15)]
    SIGN_FONT = None