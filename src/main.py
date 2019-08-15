import gameHelper as helper
from player import Player
from gamePiece import Piece
from game import Game


def main():

    helper.clearConsole()
    menu()


def menu():
    try:
        print(f'1. Play a game \n2. Scores \n3. Exit')
        i = int(input('enter your choice: '))
        if i is 1:
            print('play game')
            startGame()
        elif i is 2:
            print('scores')
        elif i is 3:
            print('exit')
        else:
            print('invalid')
    except ValueError:
        print('error parsing input')


def startGame():
    p1Name = input("Enter player 1's name: ")
    p2Name = input("Enter player 2's name: ")

    p1 = Player(p1Name, Piece.CROSS)
    p2 = Player(p2Name, Piece.KNOT)

    boardSize = int(input('Size of board e.g. n^2: '))
    dimensions = (boardSize, boardSize)

    # game ID is hardcoded for the moment
    game = Game((p1, p2), 1, dimensions)
    game.playGame()


if __name__ == '__main__':
    main()
