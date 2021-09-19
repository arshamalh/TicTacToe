from itertools import cycle
import re

class GameBoard:

    x = "X"
    o = "O"

    def __init__(self):
        self.player_cyc = cycle([1, 2])
        self.placeFilled = 0
        self.matrix = [['-' for _ in range(3)] for _ in range(3)]

    def drawer(self):
        self.shape = ''
        for i in range(3):
            self.shape += ' ---' * 3 + '\n'
            for j in range(3):
                self.shape += f'| {self.matrix[i][j]} '
            self.shape += '|' + '\n'
        self.shape += ' ---' * 3 + '\n'
        return self.shape

    def filler(self, player, choice):
        if self.matrix[choice[0] - 1][choice[1] - 1] != '-': return False
        self.matrix[choice[0] - 1][choice[1] - 1] = self.x if player == 1 else self.o
        return True

    def checker(self):
        winner = {1: False, 2: False}

        # like ---
        for i in self.matrix:
          winner[1] = i[0] == i[1] == i[2] == self.x
          winner[2] = i[0] == i[1] == i[2] == self.o
          if winner[1] or winner[2]: return winner

        # like |
        for i in range(3):
          winner[1] = self.matrix[0][i] == self.matrix[1][i] == self.matrix[2][i] == self.x
          winner[2] = self.matrix[0][i] == self.matrix[1][i] == self.matrix[2][i] == self.o
          if winner[1] or winner[2]: return winner

        # like \ or /
        winner[1] = self.matrix[0][0] == self.matrix[1][1] == self.matrix[2][2] == self.x or self.matrix[0][2] == self.matrix[1][1] == self.matrix[2][0] == self.x
        winner[2] = self.matrix[0][0] == self.matrix[1][1] == self.matrix[2][2] == self.o or self.matrix[0][2] == self.matrix[1][1] == self.matrix[2][0] == self.o
        if winner[1] or winner[2]: return winner

        return False

    @property
    def player(self): return next(self.player_cyc)


board = GameBoard()
player_cyc = cycle([1, 2]) # cycle players between players number 1 and 2.
def getCordination(pl):
    # Get user input and replace anything except 0-9
    position = re.sub("[^1-3]", "", input(f'player {pl} please enter your position: '))
    cordination = [int(ch) for ch in position]
    return cordination

while True:
    pl = board.player
    cordination = getCordination(pl)

    while len(cordination) != 2: 
        print('Cordination is wrong! try somewhere else.')
        cordination = getCordination(pl)

    while not board.filler(pl, cordination): 
        print('Coordination is filled, try somewhere else.')
        cordination = getCordination(pl)

    board.placeFilled += 1
    print(board.drawer(), f'\n {board.placeFilled} place is filled')
    if board.placeFilled > 4:
        winner = board.checker()
        if winner:
            print(f'Player 1 has won!') if winner[1] else print(f'Player 2 has won!')
            break
        elif board.placeFilled == 9:
            print('No player won, play again!')

# TODO: Make everything happened in class an while loop in play method
# TODO: Can it be a package? so make it simpler to understand and documented
# TODO: Don't repeat, line 75 and 89 are same (position input)
# TODO: It has to work for bigger GameBords (the problem is with cheker)
