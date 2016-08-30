class TicTacToe(object):

    def __init__(self, n):
        self.grids =[['']*n]*n
        pass

    def is_game_a_win(self, row, col, symbol):
        #first row -> no previous row possible directions are diagonal down , row down and col right
        if row == 0:
            if (self.grids[row+1][col+1] == symbol or
                self.grids[row+1][col] == symbol or
                self.grids[row][col+1] == symbol):
                return symbol

        

        if self.grids []
        # if row == 0:
        # if col == 0:
        #
        # if row == n-1:
        # if col == n-1:
        pass


    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins. */
        """
        symbol = 'X' if player == 1 else 'O'
        #if the the cell is empty:
        if self.grids[row][col] == '':
            self.grids[row][col] = symbol

        if is_game_a_win(row, col, symbol)
        return 0
