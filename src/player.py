class Player:

    def __init__(self, name, piece):
        self.name = name
        self.piece = piece
        self.numOfWins = None

    def __str__(self):
        return self.name
