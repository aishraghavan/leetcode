from design_tic_tac_toe import TicTacToe

def test_1():
    obj = TicTacToe(2)
    print obj.move(0,0,2)
    print obj.move(0,1,1)
    print obj.move(1,1,2)

def test_aish():
    obj = TicTacToe(3)
    print obj.grids

if __name__ == "__main__":
    test_1()
