class GameState:
    def __init__(self):
        self.board = [
            ["bR", "bN","bB","bQ", "bK","bB","bN","bR"],
            ["bp","bp","bp","bp","bp","bp","bp","bp"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["wp","wp","wp","wp","wp","wp","wp","wp"],
            ["wR","wN","wB","wQ","wK","wB","wN","wR"],
        ]
        self.whiteToMove = True
        self.moveLog = []

    def MakeMove(self,move):
        self.board[move.startRow][move.startCol] = "--" #on remet à nulle la position que vient de quitter la pièce
        self.board[move.endRow][move.endCol] = move.pieceMoved #et on inscrit la pièce sur sa position d'arrivée
        self.moveLog.append(move) #pour afficher l'historique des moves
        self.whiteToMove = not self.whiteToMove


class Move:
    ranksToRows = {"1": 7, "2": 6, "3": 5, "4": 4,
                   "5": 3, "6": 2, "7": 1, "8": 0} #standard notation for rows
    rowsToRanks = {value: key for key, value in ranksToRows.items()} #inverse les valeurs dans ce nouveau dictionnaire
    filesToCols = {"a": 0, "b": 1, "c": 2, "d": 3,
                   "e": 4, "f": 5, "g": 6, "h": 7} #standard notation for cols
    colsToFiles = {value: key for key, value in filesToCols.items()} #permet d'afficher au joueur ensuite la bonne colonne
    def __init__(self,startSquare,endSquare,board):
        self.startRow = startSquare[0]
        self.startCol = startSquare[1]
        self.endRow = endSquare[0]
        self.endCol = endSquare[1]
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]

    def getChessNotation(self):
        return self.getRankFile(self.startRow,self.startCol) + self.getRankFile(self.endRow, self.endCol)
        #il manque la promotion, la prise (x), le roque, l'échec (+) ou l'échec et mat (++)

    def getRankFile(self, row, col):
        return self.colsToFiles[col] + self.rowsToRanks[row]