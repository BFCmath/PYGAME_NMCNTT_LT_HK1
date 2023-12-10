import pygame, Define

pygame.mixer.init()

class Game_logic():
    def __init__(self, NumberWidthCell, NumberHeightCell, Board, Player1, Player2):
        self.NumberWidthCell = NumberWidthCell
        self.NumberHeightCell = NumberHeightCell

        self.Cell_Size = min(Define.BoardGame.BOARD_WIDTH // self.NumberWidthCell, Define.BoardGame.BOARD_HEIGHT // self.NumberHeightCell)

        self.x0 = (Define.Screen.SCREEN_WIDTH - self.NumberWidthCell*self.Cell_Size)//2
        self.y0 = (Define.Screen.SCREEN_HEIGHT - self.NumberHeightCell*self.Cell_Size)//2
        self.xn = self.x0 + self.NumberWidthCell*self.Cell_Size
        self.yn = self.y0 + self.NumberHeightCell*self.Cell_Size

        self.PlayerX = Player1
        self.PlayerO = Player2

        self.Board = Board

        self.X = Define.get_font(self.Cell_Size // 2).render('X', False, "blue")
        self.O = Define.get_font(self.Cell_Size // 2).render('O', False, "red")

        self.Turn = 1

        self.Score = (0, 0)

        self.Turn_Color = "#800000"
        self.not_Turn_Color = "black"

    def Draw_Piece(self, SCREEN, row, col):
        if self.Board[row][col] == 1:
            text_Rect = self.X.get_rect(center=(self.x0 + col*self.Cell_Size + self.Cell_Size // 2, self.y0 + row*self.Cell_Size + self.Cell_Size // 2))
            SCREEN.blit(self.X, text_Rect)
        elif self.Board[row][col] == -1:
            text_Rect = self.O.get_rect(center=(self.x0 + col*self.Cell_Size + self.Cell_Size // 2, self.y0 + row*self.Cell_Size + self.Cell_Size // 2))
            SCREEN.blit(self.O, text_Rect)

    def DrawBoard(self, SCREEN):
        for x in range(self.x0 + self.Cell_Size, self.xn, self.Cell_Size):
            pygame.draw.line(SCREEN, (160, 85, 45), (x, self.y0), (x, self.yn - 5), 3)
        for y in range(self.y0 + self.Cell_Size, self.yn, self.Cell_Size):
            pygame.draw.line(SCREEN, (160, 85, 45), (self.x0, y), (self.xn - 5, y), 3)
        
        pygame.draw.rect(SCREEN, (140, 70, 20), ((self.x0, self.y0), (self.Cell_Size*self.NumberWidthCell, self.Cell_Size*self.NumberHeightCell)), width = 7, border_radius = 5)
        
        for row in range(self.NumberHeightCell):
            for col in range(self.NumberWidthCell):
                if self.Board[row][col] == 1:
                    self.Draw_Piece(SCREEN, row, col)
                elif self.Board[row][col] == -1:
                    self.Draw_Piece(SCREEN, row, col)

        pygame.display.update()
    
    def PrintInfor(self, SCREEN):
        if self.Turn == 1:
            Player1 = Define.get_font(35).render(f"{self.PlayerX}: X", True, self.Turn_Color)
            Rect1 = pygame.Rect(30, 30, Player1.get_width(), Player1.get_height())
            SCREEN.blit(Player1, Rect1)

            Player2 = Define.get_font(25).render(f"{self.PlayerO}: O", True, self.not_Turn_Color)
            Rect2 = pygame.Rect(Define.Screen.SCREEN_WIDTH - 30 - Player2.get_width(), 30, Player1.get_width(), Player1.get_height())
            SCREEN.blit(Player2, Rect2)
        else:
            Player1 = Define.get_font(25).render(f"{self.PlayerX}: X", True, self.not_Turn_Color)
            Rect1 = pygame.Rect(30, 30, Player1.get_width(), Player1.get_height())
            SCREEN.blit(Player1, Rect1)

            Player2 = Define.get_font(35).render(f"{self.PlayerO}:O", True, self.Turn_Color)
            Rect2 = pygame.Rect(Define.Screen.SCREEN_WIDTH - 30 - Player2.get_width(), 30, Player1.get_width(), Player1.get_height())
            SCREEN.blit(Player2, Rect2)
        
        score = Define.get_font(35).render(f"{self.Score[0]} : {self.Score[1]}", False, "brown3")
        score_rect = score.get_rect(center=(640, 50))
        SCREEN.blit(score, score_rect)

    def checkEnd(self, row, col): #return 0(Draw), 1(X win), -1(O win)
        if Define.Find_in(0, self.Board):
            count = 0
            block = 0
            r = max(row - 1, 0)
            while (r > -1 and self.Board[r][col] == self.Board[row][col]):
                count = count + 1
                r = r - 1
            if r == -1 or self.Board[r][col] == - self.Board[row][col]:
                block = block + 1
            r = min(row + 1 , self.NumberHeightCell)
            while ( r < self.NumberHeightCell and self.Board[r][col] == self.Board[row][col]):
                count = count + 1
                r = r + 1
            if r == self.NumberHeightCell or self.Board[r][col] == - self.Board[row][col]:
                block = block + 1
            if (count > 3 and block < 2):
                print(f"{self.PlayerX if self.Board[row][col] == 1 else self.PlayerO} Win!")
                return self.Board[row][col]

            count = 0
            block = 0
            c = max(col - 1, 0)
            while (c > -1 and self.Board[row][c] == self.Board[row][col]):
                count = count + 1
                c = c - 1
            if c == -1 or self.Board[row][c] == - self.Board[row][col]:
                block = block + 1
            c = min(col + 1 , self.NumberWidthCell)
            while (c < self.NumberWidthCell and self.Board[row][c] == self.Board[row][col]):
                count = count + 1
                c = c + 1
            if c == self.NumberWidthCell or self.Board[row][c] == - self.Board[row][col]:
                block = block + 1
            if (count > 3 and block < 2):
                print(f"{self.PlayerX if self.Board[row][col] == 1 else self.PlayerO} Win!")
                return self.Board[row][col]

            count = 0
            block = 0
            i = 1
            while (row + i < self.NumberHeightCell and col + i < self.NumberWidthCell and self.Board[row + i][col + i] == self.Board[row][col]):
                count = count + 1
                i = i + 1
            if row + i == self.NumberHeightCell or col + i == self.NumberWidthCell or self.Board[row + i][col + i] == - self.Board[row][col]:
                block = block + 1
            i = 1
            while (row - i > -1 and col - i > -1 and self.Board[row - i][col - i] == self.Board[row][col]):
                count = count + 1
                i = i + 1
            if row - i == -1 or col - i == -1 or self.Board[row - i][col - i] == - self.Board[row][col]:
                block = block + 1
            if (count > 3 and block < 2):
                print(f"{self.PlayerX if self.Board[row][col] == 1 else self.PlayerO} Win!")
                return True    

            count = 0
            block = 0
            i = 1
            while (row + i < self.NumberHeightCell and col - i > -1 and self.Board[row + i][col - i] == self.Board[row][col]):
                count = count + 1
                i = i + 1
            if row + i == self.NumberHeightCell or col - i == -1 or self.Board[row + i][col - i] == - self.Board[row][col]:
                block = block + 1
            i = 1
            while (row - i > -1 and col + i < self.NumberWidthCell and self.Board[row - i][col + i] == self.Board[row][col]):
                count = count + 1
                i = i + 1
            if row - i == -1 or col + i == self.NumberWidthCell or self.Board[row - i][col + i] == - self.Board[row][col]:
                block = block + 1
            if (count > 3 and block < 2):
                print(f"{self.PlayerX if self.Board[row][col] == 1 else self.PlayerO} Win!")
                return self.Board[row][col]
            
            return 2
        else:
            print(self.Board, "\nDraw")
            return 0

    def makeMove(self, row, col):
        if self.Board[row][col] == 0:
            self.Board[row][col] = self.Turn
            self.checkEnd(row, col)
            self.Turn *= -1
            Define.Sound.SOUND_EFFECT.play()

    def checkForInput(self, position):
        if position[0] in range(self.x0, self.xn) and position[1] in range(self.y0, self.yn):
            self.makeMove((position[1] - self.y0) // self.Cell_Size, (position[0] - self.x0) // self.Cell_Size)
        