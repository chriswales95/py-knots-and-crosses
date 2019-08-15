from board import Board
import sys


class Game:

    def __init__(self, players, id, boardDimensions):
        self.id = id
        self.inProgress = True
        self.player1, self.player2 = players
        self.boardDimensions = boardDimensions
        self.board = Board(boardDimensions)
        self.turn = self.player1

    def playGame(self):
        while (self.inProgress):
            print(f'Turn: {self.turn}')
            try:
                move = (int(input('row: ')), int(input('column ')))
                attemptMove = self.board.addPositionToBoard(
                    move, self.turn.piece)
                if attemptMove is True:
                    self.board.draw()
                    self.nextTurn()
            except KeyboardInterrupt as e:
                print(e)
                sys.exit()

    def nextTurn(self):
        if self.turn is self.player1:
            self.turn = self.player2
        else:
            self.turn = self.player1
