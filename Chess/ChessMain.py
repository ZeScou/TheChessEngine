import pygame as p
import ChessEngine
WIDTH = HEIGHT = 400
DIMENSION = 8 #for the 8x8 chessboard
SQUARE_SIZE = WIDTH // DIMENSION
MAX_FPS = 15
IMAGES = {}


PIPI = 3


def load_images():
    pieces = ['wp', 'wR', 'wN', 'wB', 'wQ', 'wK', 'bp', 'bR', 'bN', 'bB', 'bQ', 'bK']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load(f"images/{piece}.png"), (SQUARE_SIZE, SQUARE_SIZE))

def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    load_images()
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()

def drawGameState(screen, gs):
    drawBoard(screen) #squares on the board
    drawPieces(screen,gs.board) #pieces on the squares

def drawBoard(screen):
    colors = [p.Color("white"), p.Color("chocolate4")]
    for row in range(DIMENSION):
        for col in range(DIMENSION):
          color = colors[((row+col)%2)]
          p.draw.rect(screen, color, p.Rect(col*SQUARE_SIZE,row*SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE))


def drawPieces(screen, board):
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            piece = board[row][col]
            if piece != "--":
                screen.blit(IMAGES[piece],p.Rect(col*SQUARE_SIZE,row*SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE))


if __name__ == "__main__":
    main()