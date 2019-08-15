import gameHelper as helper


class Board:

    def __init__(self, dimensions):
        self.w, self.h = dimensions
        self.positions = [[None for x in range(self.w)] for y in range(self.h)]

    def addPositionToBoard(self, coordinates, piece):
        x, y = coordinates

        try:
            if self.positions[x][y] is None:
                self.positions[x][y] = piece.value
                return True
            else:
                print(f'space {x}, {y} is occupied')
                return False
        except IndexError as e:
            print(e)
            return False

    def draw(self):
        helper.clearConsole()
        for row in self.positions:
            for position in row:
                if (position is not None):
                    print(position, end=' ')
                else:
                    print(' ', end=' ')
            print('')
