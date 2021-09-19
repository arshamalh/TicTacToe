from itertools import cycle
import re

class GameBoard:

    x = "X"
    o = "O"

    def __init__(self):
        self.player_cyc = cycle([1, 2])
        self.placeFilled = 0
        self.Input = input
        self.Print = print
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

    def play(self):
        while True:
            pl = self.player
            cordination = self.getCordination(pl)

            while len(cordination) != 2: 
                self.Print('Cordination is wrong! try somewhere else.')
                cordination = self.getCordination(pl)

            while not self.filler(pl, cordination): 
                self.Print('Coordination is filled, try somewhere else.')
                cordination = self.getCordination(pl)

            self.placeFilled += 1
            self.Print(self.drawer(), f'\n {self.placeFilled} place is filled')
            if self.placeFilled > 4:
                winner = self.checker()
                if winner:
                    self.Print(f'Player 1 has won!') if winner[1] else self.Print(f'Player 2 has won!')
                    break
                elif self.placeFilled == 9:
                    self.Print('No player won, play again!')

    def getCordination(self, pl):
        # Get user input and replace anything except 0-9
        position = re.sub("[^1-3]", "", self.Input(f'player {pl} please enter your position: '))
        cordination = [int(ch) for ch in position]
        return cordination

    @property
    def player(self): return next(self.player_cyc)

    def setInPrint(self, Input=input, Print=print):
        # Input function will get an argument an show it to user, it should return user input
        # Print function will get an argument an show it to user
        self.Input = Input
        self.Print = Print

board = GameBoard()
board.play()
