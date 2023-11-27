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
def calculate_square_size(ratioPostitionX,ratioPositionY,ratioEdge):
        _edge = Board.BOARD_WIDTH*ratioEdge
        _postionX = Board.BOARD_WIDTH* ratioPostitionX - _edge//2
        _postionY = Board.BOARD_HEIGHT*ratioPositionY - _edge//2
        return (_postionX,_postionY,_edge,_edge)

class Menu:
    TITLE_RECT = calculate_rect_size(1/2,2/7,1/5,1/6)
    TITLE_TEXT_SIZE = 50

    PLAY_BUTTON_RECT = calculate_rect_size(1/2,4/7,2/11,1/12)
    PLAY_BUTTON_SIZE = 20

    SETTINGS_BUTTON_RECT = calculate_rect_size(1/2,11/14,1/8,1/13)
    SETTINGS_BUTTON_SIZE = 13

    BUTTON_COLOR = (255, 255, 255)  # White
    BUTTON_TEXT_COLOR = (0, 0, 0)  # Black
    TITLE_TEXT = 'Caro'
    PLAY_TEXT = 'Play game'
    SETTINGS_TEXT = 'Settings'
    FONT = 'kongtext.ttf'

class Settings:
    SETTINGS_TITLE_RECT = calculate_rect_size(1/2,1/7,1/3,1/6)
    SETTINGS_TITLE_TEXT_SIZE = 40
    
    SETTINGS_BACK_BUTTON_RECT = calculate_rect_size(1/2,11/14,1/6,1/12)
    SETTINGS_BACK_BUTTON_SIZE = 25

    SETTINGS_BOARD_SIZE_RECT = calculate_rect_size(1/2,2.75/7,1/4,1/12)
    SETTINGS_BOARD_SIZE_TEXT_SIZE = 15
    
    SETTINGS_X_PLACE = (0.5,0.5)
    SETTINGS_X_SIZE = 20
    
    SETTINGS_INPUT_BOX_RECT_1 = calculate_square_size(SETTINGS_X_PLACE[0]-0.035,SETTINGS_X_PLACE[1],0.04)
    SETTINGS_INPUT_BOX_RECT_2 = calculate_square_size(SETTINGS_X_PLACE[0]+0.035,SETTINGS_X_PLACE[1],0.04)
    
    SETTINGS_BUTTON_COLOR = (255, 255, 255) 
    SETTINGS_BUTTON_TEXT_COLOR = (116, 124, 10) 
    SETTINGS_INPUT_BOX_COLOR = (0, 0, 0) 
    SETTINGS_TITLE_TEXT = 'SETTINGS'
    SETTINGS_BACK_TEXT = 'Back' 
    SETTINGS_BOARD_SIZE_TEXT = 'Caro board size'
    SETTINGS_COLOR = (152,118,246)
    FONT = 'kongtext.ttf'

    row_cells = 5
    col_cells = 3

class PlayGame:
    
    TURN_TEXT_POSITION = (10, 10)
    BACK_BUTTON_RECT = calculate_rect_size(0.925,0.05,1/10,1/20)
    BACK_BUTTON_COLOR = (255, 255, 255)  # White
    BACK_TEXT_COLOR = (0,0,0)
    BACK_TEXT = 'Back'
    PLAYER1_TEXT_POSITION = (10, Board.BOARD_HEIGHT - 40)
    PLAYER2_TEXT_POSITION = (Board.BOARD_WIDTH - 10, Board.BOARD_HEIGHT - 40)
    PLAYER1_TEXT = 'Player 1: X'
    PLAYER2_TEXT = 'Player 2: O'
    BACKGROUND_COLOR = (123, 179, 243)
    
    turn_text = 'Player 1\'s turn!'
    TEXT_SIZE = 16
    TEXT_COLOR = (0, 0, 0)
    FONT = 'kongtext.ttf'
    CARO_BOARD_WIDTH = 800
    CARO_BOARD_HEIGHT = 400
    def change_turn_text(self, turn):
        if turn == 1:
            self.turn_text = 'Player 1\'s turn!'
        else:
            self.turn_text = 'Player 2\'s turn!'

class CellSetting:
    CELL_COLOR = (255, 255, 255)  # White
    CELL_TEXT_COLOR = (0, 0, 0)  # Black
    EDGE_COLOR = (0, 0, 0)  # Black
