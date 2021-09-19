from itertools import cycle
import re

class GameBoard:

    signTurn = 'X'

    def __init__(self, row, column):
        self.size = [row, column]
        self.shape = ''
        self.matrix = [['-' for _ in range(self.size[1])]
                       for _ in range(self.size[0])]
        self.placeFilled = 0

    def drawer(self):
        self.shape = ''
        for i in range(self.size[0]):
            self.shape += ' ---' * self.size[1] + '\n'
            for j in range(self.size[1]):
                self.shape += f'| {self.matrix[i][j]} '
            self.shape += '|' + '\n'
        self.shape += ' ---' * self.size[1] + '\n'
        return self.shape

    def filler(self, player, choice):
        if self.matrix[choice[0] - 1][choice[1] - 1] == '-':
            if player == 1:
                self.signTurn = 'X'
            elif player == 2:
                self.signTurn = 'O'
            else:
                # TODO: Fix it!
                print('I have some problems with Player number!')
            self.matrix[choice[0] - 1][choice[1] - 1] = self.signTurn
            return True
        else:
            return False

    def checker(self):
        xPlayer, oPlayer, winnerX, winnerO = "X", "O", False, False
        def checkWinner(Wx, Wo): # has winner, winner
          if Wx:
            return 'Player 1 is winner'
          elif Wo:
            return 'Player 2 is winner'
          else:
            return False

        # like ---
        for i in self.matrix:
          winnerX = i[0] == i[1] == i[2] == xPlayer
          winnerO = i[0] == i[1] == i[2] == oPlayer
          if checkWinner(winnerX, winnerO):
            return True, checkWinner(winnerX, winnerO)

        # like |
        for i in range(3):
          winnerX = self.matrix[0][i] == self.matrix[1][i] == self.matrix[2][i] == xPlayer
          winnerO = self.matrix[0][i] == self.matrix[1][i] == self.matrix[2][i] == oPlayer

          if checkWinner(winnerX, winnerO):
            return True, checkWinner(winnerX, winnerO)

        # like this: \ and /
        winnerX = self.matrix[0][0] == self.matrix[1][1] == self.matrix[2][2] == xPlayer or self.matrix[0][2] == self.matrix[1][1] == self.matrix[2][0] == xPlayer
        winnerO = self.matrix[0][0] == self.matrix[1][1] == self.matrix[2][2] == oPlayer or self.matrix[0][2] == self.matrix[1][1] == self.matrix[2][0] == oPlayer

        if checkWinner(winnerX, winnerO):
          return True, checkWinner(winnerX, winnerO)

        return False, ""

board = GameBoard(3, 3)
player_cyc = cycle([1, 2]) # cycle players between players number 1 and 2.
def getCordination(pl):
    # Get user input and replace anything except 0-9
    position = re.sub("[^1-3]", "", input(f'player {pl} please enter your position: '))
    cordination = [int(ch) for ch in position]
    return cordination

while True:
    pl = next(player_cyc)
    cordination = getCordination(pl)

    while len(cordination) != 2: 
        print('Cordination is wrong! try somewhere else.')
        cordination = getCordination(pl)

    while not board.filler(pl, cordination): 
        print('Coordination is filled, try somewhere else.')
        cordination = getCordination(pl)

    # Erase and write to show it dynamic
    # sys.stdout.write("\033[F" * 10) 
    # print(("     " * 50 + "\n") * 10)
    # sys.stdout.write("\033[F" * 11)

    board.placeFilled += 1
    print(board.drawer())
    print(f'{board.placeFilled} place is filled')
    if board.placeFilled > 4:
        checked, pl_winner = board.checker()
        if checked:
            print(f'{pl_winner}')
            break
        elif board.placeFilled == 9:
            print('No player won, play again!')

# TODO: Make everything happened in class an while loop in play method
# TODO: Can it be a package? so make it simpler to understand and documented
# TODO: Don't repeat, line 75 and 89 are same (position input)
# TODO: It has to work for bigger GameBords (the problem is with cheker)
