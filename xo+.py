import pygame
from pygame.locals import *
import time
import random

XO   = "X"   
grid = [ [ None, None, None, None, None ], \
         [ None, None, None,  None, None ], \
         [ None, None, None, None, None ], \
         [ None, None, None,  None, None ], \
         [ None, None,  None,  None, None ] ]

winner = None

game = "going"
mode = 0
def isWinner(board,letter):
      for row in range (0, 5):
        if ((grid [row][0] == grid[row][1] == grid[row][2]) and \
           (grid [row][0] is not None)):
            return True
        elif ((grid [row][3] == grid[row][1] == grid[row][2]) and \
           (grid [row][3] is not None)):
            return True
        elif ((grid [row][3] == grid[row][4] == grid[row][2]) and \
           (grid [row][3] is not None)):
            return True

      for col in range (0, 5):
        if (grid[0][col] == grid[1][col] == grid[2][col]) and \
           (grid[0][col] is not None):
            return True
        elif (grid[3][col] == grid[1][col] == grid[2][col]) and \
           (grid[3][col] is not None):
            return True
        elif (grid[3][col] == grid[4][col] == grid[2][col]) and \
           (grid[3][col] is not None):
            return True
      for row  in range(0,3):
        for col in range(0,3):
          if (grid[row][col] == grid[row+1][col+1] == grid[row+2][col+2]) and \
            (grid[row][col] is not None):
              return True
      for row  in range(0,3):
        for col in range(2,5):
          if (grid[row][col] == grid[row+1][col-1] == grid[row+2][col-2]) and \
            (grid[row][col] is not None):
              return True
      return False
def isBoardFull(board):
	for i in range(1,10):
		if isSpaceFree(board, i):
			return False
	return True

def isSpaceFree(board, move):
	return board[move] == None

def minimax(board, depth, isMax, alpha, beta, computerLetter):
    if(depth>3):
      return alpha
    if computerLetter == 'X':
      playerLetter = 'O'
    else:
      playerLetter = 'X'

    if isWinner(board, computerLetter):
      return 10
    if isWinner(board, playerLetter):
      return -10
    if isBoardFull(board):
      return 0
    print(depth)
    if isMax:
      best = -1000
      
      for i in range(0,10):
        if isSpaceFree(board, i):
          board[i] = computerLetter
          best = max(best, minimax(board, depth+1, not isMax, alpha, beta, computerLetter) - depth)
          alpha = max(alpha, best)
          board[i] = None

          if alpha >= beta:
            break

      return best
    else:
      best = 1000

      for i in range(0,10):
        if isSpaceFree(board, i):
          board[i] = playerLetter
          best = min(best, minimax(board, depth+1, not isMax, alpha, beta, computerLetter) + depth)
          beta = min(beta, best)
          board[i] = None

          if alpha >= beta:
            break

      return best


def findBestMove(board, computerLetter):
    print(board)
    bestVal = -1000
    bestMove = -1

    for i in range(0,25):
      if isSpaceFree(board, i):
        board[i] = computerLetter

        moveVal = minimax(board, 0, False, -1000, 1000, computerLetter)

        board[i] = ' '

        if moveVal > bestVal:
          bestMove = i
          bestVal = moveVal

    return bestMove


def initChoice(ttt):
    background = pygame.Surface (ttt.get_size())
    background = background.convert()
    background.fill ((0, 0, 0))

    pygame.draw.line (background, (250,250,250), (100, 100), (100, 400), 2)
    pygame.draw.line (background, (250,250,250), (450, 100), (450, 400), 2)

    pygame.draw.line (background, (250,250,250), (100, 100), (450, 100), 2)
    pygame.draw.line (background, (250,250,250), (100, 250), (450, 250), 2)
    pygame.draw.line (background, (250,250,250), (100, 400), (450, 400), 2)
    return background

def initBoard(ttt):
    background = pygame.Surface (ttt.get_size())
    background = background.convert()
    background.fill ((0, 0, 0))

    pygame.draw.line (background, (250,250,250), (100, 0), (100, 500), 2)
    pygame.draw.line (background, (250,250,250), (200, 0), (200, 500), 2)
    pygame.draw.line (background, (250,250,250), (300, 0), (300, 500), 2)
    pygame.draw.line (background, (250,250,250), (400, 0), (400, 500), 2)

    pygame.draw.line (background, (250,250,250), (0, 100), (500, 100), 2)
    pygame.draw.line (background, (250,250,250), (0, 200), (500, 200), 2)
    pygame.draw.line (background, (250,250,250), (0, 300), (500, 300), 2)
    pygame.draw.line (background, (250,250,250), (0, 400), (500, 400), 2)

    return background

def drawStatus (board):
    global XO, winner, game

    if (winner is None):
        message = "na potezu je " + XO
    else:
        message = winner + " je pobedio!!!"
        font = pygame.font.Font(None, 60)
        text = font.render(message, 1, (250, 0, 0))

        board.fill ((250, 250, 250), (0, 500, 500, 25))
        board.blit(text, (150, 200))
        game = "over"
    font = pygame.font.Font(None, 24)
    text = font.render(message, 1, (10, 10, 10))
    board.fill ((250, 250, 250), (0, 500, 500, 25))
    board.blit(text, (10, 500))

def showText(ttt, board):
  message = " Igrac protiv dva bota"
  font = pygame.font.Font(None, 30)
  text = font.render(message, 1, (250, 0, 0))
  board.fill ((250, 250, 250), (0, 500, 500, 25))
  board.blit(text, (180, 175))
  ttt.blit (board, (0, 0))
  pygame.display.flip()
  message = " Dva igraca protiv bota"
  font = pygame.font.Font(None, 30)
  text = font.render(message, 1, (250, 0, 0))
  board.fill ((250, 250, 250), (0, 500, 500, 25))
  board.blit(text, (160, 325))
  ttt.blit (board, (0, 0))
  pygame.display.flip()
    

def showBoard (ttt, board):
    global game
    drawStatus (board)
    ttt.blit (board, (0, 0))
    pygame.display.flip()
    while(game=="over"):
      time.sleep(1)
    
    
def boardPos (mouseX, mouseY):
    if (mouseY < 100):
        row = 0
    elif (mouseY < 200):
        row = 1
    elif (mouseY < 300):
        row = 2
    elif (mouseY < 400):
        row = 3
    else:
        row = 4

    if (mouseX < 100):
        col = 0
    elif (mouseX < 200):
        col = 1
    elif (mouseX < 300):
        col = 2
    elif (mouseX < 400):
        col = 3
    else:
        col = 4

    return (row, col)

def drawMove (board, boardRow, boardCol, Piece):
    centerX = ((boardCol) * 100) + 50
    centerY = ((boardRow) * 100) + 50

    if (Piece == 'O'):
        pygame.draw.circle (board, (250,250,250), (centerX, centerY), 44, 2)
    elif (Piece == "+"):
        pygame.draw.line (board, (250,250,250), (centerX, centerY - 22), \
                         (centerX, centerY + 22), 2)
        pygame.draw.line (board, (250,250,250), (centerX - 22, centerY), \
                         (centerX + 22, centerY), 2)
    else:
        pygame.draw.line (board, (250,250,250), (centerX - 22, centerY - 22), \
                         (centerX + 22, centerY + 22), 2)
        pygame.draw.line (board, (250,250,250), (centerX + 22, centerY - 22), \
                         (centerX - 22, centerY + 22), 2)

    grid [boardRow][boardCol] = Piece
def choseBoard(board):
  global grid, XO, mode, running
    
  (mouseX, mouseY) = pygame.mouse.get_pos()
  if(mouseX>100 and mouseX<450 and mouseY>100 and mouseY<240):
    pygame.draw.circle (board, (250,250,250), (150, 175), 44, 2)
    mode=1
    running=0
  elif(mouseX>100 and mouseX<450 and mouseY>260 and mouseY<400):
    pygame.draw.circle (board, (250,250,250), (150, 425), 44, 2)
    mode=2
    running=0

def clickBoard(board):
    
    global grid, XO,mode
    
    (mouseX, mouseY) = pygame.mouse.get_pos()
    (row, col) = boardPos (mouseX, mouseY)

    if ((grid[row][col] == "X") or (grid[row][col] == "O") or (grid[row][col] == "+")):
        return

    if(mode==1):
      if(XO=="X"):
        drawMove (board, row, col, XO)
        gameWon (board)
        showBoard (ttt, board)
        XO = "O"
        for i in range(0,2):  
          find=False
          x=0
          y=0
          bod=[]
          for i in range(0,5):
            for j in range(0,5):
              bod.append(grid[i][j])
          val=findBestMove(bod,XO)
          x=val//5
          y=val%5
          drawMove (board, x, y, XO)
          gameWon (board)
          showBoard (ttt, board)
          if (XO == "X"):
              XO = "O"
          elif (XO == "O"):
            XO = "+"
          else:
              XO = "X"   
    else:
      if(XO=="O"):
        drawMove (board, row, col, XO)
        gameWon (board)
        showBoard (ttt, board)
        XO="+"
        find=False
        x=0
        y=0
        bod=[]
        for i in range(0,5):
          for j in range(0,5):
            bod.append(grid[i][j])
        val=findBestMove(bod,XO)
        x=val//5
        y=val%5
        drawMove (board, x, y, XO)
        gameWon (board)
        showBoard (ttt, board)
        XO = "X"
      else:
        drawMove (board, row, col, XO)
        gameWon (board)
        showBoard (ttt, board)
        if (XO == "X"):
          XO = "O"
        elif (XO == "O"):
          XO = "+"
        else:
          XO = "X"
    
def gameWon(board):
    
    global grid, winner

    for row in range (0, 5):
        if ((grid [row][0] == grid[row][1] == grid[row][2]) and \
           (grid [row][0] is not None)):
            winner = grid[row][0]
            pygame.draw.line (board, (250,250,250), (0, (row + 1)*100 - 50), \
                              (300, (row + 1)*100 - 50), 2)
            print(grid)
            break
        elif ((grid [row][3] == grid[row][1] == grid[row][2]) and \
           (grid [row][3] is not None)):
            winner = grid[row][3]
            pygame.draw.line (board, (250,250,250), (100, (row + 1)*100 - 50), \
                              (400, (row + 1)*100 - 50), 2)
            break
        elif ((grid [row][3] == grid[row][4] == grid[row][2]) and \
           (grid [row][3] is not None)):
            winner = grid[row][3]
            pygame.draw.line (board, (250,250,250), (200, (row + 1)*100 - 50), \
                              (500, (row + 1)*100 - 50), 2)
            break

    for col in range (0, 5):
        if (grid[0][col] == grid[1][col] == grid[2][col]) and \
           (grid[0][col] is not None):
            winner = grid[0][col]
            pygame.draw.line (board, (250,250,250), ((col + 1)* 100 - 50, 0), \
                              ((col + 1)* 100 - 50, 300), 2)
            break
        elif (grid[3][col] == grid[1][col] == grid[2][col]) and \
           (grid[3][col] is not None):
            winner = grid[3][col]
            pygame.draw.line (board, (250,250,250), ((col + 1)* 100 - 50, 100), \
                              ((col + 1)* 100 - 50, 400), 2)
            break
        elif (grid[3][col] == grid[4][col] == grid[2][col]) and \
           (grid[3][col] is not None):
            winner = grid[3][col]
            pygame.draw.line (board, (250,250,250), ((col + 1)* 100 - 50, 200), \
                              ((col + 1)* 100 - 50, 500), 2)
            break
    for row  in range(0,3):
      for col in range(0,3):
        if (grid[row][col] == grid[row+1][col+1] == grid[row+2][col+2]) and \
          (grid[row][col] is not None):
            winner = grid[row][col]
            pygame.draw.line (board, (250,250,250), (((col*100)+50), (row*100)+50), (((col+2)*100)+50, ((row+2)*100)+50), 2)
            break
    for row  in range(0,3):
      for col in range(2,5):
        if (grid[row][col] == grid[row+1][col-1] == grid[row+2][col-2]) and \
          (grid[row][col] is not None):
            winner = grid[row][col]
            pygame.draw.line (board, (250,250,250), ((col*100)+50, (row*100)+50), (((col-2)*100)+50, ((row+2)*100)+50), 2)
            break
pygame.init()

mod = pygame.display.set_mode ((500, 525))
pygame.display.set_caption ('X-O-+')
choose = initChoice (mod)
running =1
while (running == 1):
    
    for event in pygame.event.get():
        if(not(game=="over")):
          if event.type is QUIT:
              running = 0
          elif event.type is MOUSEBUTTONDOWN:
              choseBoard(choose)
              

          gameWon (choose)

          showText (mod, choose)


ttt = pygame.display.set_mode ((500, 525))
pygame.display.set_caption ('X-O-+')

board = initBoard (ttt)
running = 1

while (running == 1):
    for event in pygame.event.get():
        if(not(game=="over")):
          if event.type is QUIT:
              running = 0
          elif event.type is MOUSEBUTTONDOWN:
              clickBoard(board)
          gameWon (board)
          showBoard (ttt, board)
          



          font = pygame.font.Font('freesansbold.ttf', 32) 
  
