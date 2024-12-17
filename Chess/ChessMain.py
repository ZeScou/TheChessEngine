import pygame as p
from Chess import ChessEngine
WIDTH = HEIGHT = 400
DIMENSION = 8 #for the 8x8 chessboard
SQUARE_SIZE = WIDTH // DIMENSION
MAX_FPS = 15
IMAGES = {}

def load_images():
    IMAGES['wp'] = p.transform.scale(p.image.load("images/wp.png"), (SQUARE_SIZE, SQUARE_SIZE)),
    IMAGES['bp'] = p.transform.scale(p.image.load("images/bp.png"), (SQUARE_SIZE, SQUARE_SIZE)),
    IMAGES['wR'] = p.transform.scale(p.image.load("images/wR.png"), (SQUARE_SIZE, SQUARE_SIZE)),
    IMAGES['bR'] = p.transform.scale(p.image.load("images/bR.png"), (SQUARE_SIZE, SQUARE_SIZE)),
    IMAGES['wB'] = p.transform.scale(p.image.load("images/wB.png"), (SQUARE_SIZE, SQUARE_SIZE)),
    IMAGES['bB'] = p.transform.scale(p.image.load("images/bB.png"), (SQUARE_SIZE, SQUARE_SIZE)),
    IMAGES['wN'] = p.transform.scale(p.image.load("images/wN.png"), (SQUARE_SIZE, SQUARE_SIZE)),
    IMAGES['bN'] = p.transform.scale(p.image.load("images/bN.png"), (SQUARE_SIZE, SQUARE_SIZE)),
    IMAGES['wK'] = p.transform.scale(p.image.load("images/wK.png"), (SQUARE_SIZE, SQUARE_SIZE)),
    IMAGES['bK'] = p.transform.scale(p.image.load("images/bK.png"), (SQUARE_SIZE, SQUARE_SIZE)),
    IMAGES['wQ'] = p.transform.scale(p.image.load("images/wQ.png"), (SQUARE_SIZE, SQUARE_SIZE)),
    IMAGES['bQ'] = p.transform.scale(p.image.load("images/bQ.png"), (SQUARE_SIZE, SQUARE_SIZE))

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
    pass

if __name__ == "__main__":
    main()