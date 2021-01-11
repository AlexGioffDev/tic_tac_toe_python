from util import clear, art
import random

class Board():
    def __init__(self):
        self.board_position = ['*', '*', '*', '*', '*', '*', '*', '*', '*']
    

    def print_board(self):
        p = self.board_position
        board = f'''
        ------------------------------
        |        ||        ||        |
        |   1    ||   2    ||   3    |
        |   {p[0]}    ||   {p[1]}    ||   {p[2]}    |
        |        ||        ||        |
        ------------------------------
        |        ||        ||        |
        |   4    ||   5    ||   6    |
        |   {p[3]}    ||   {p[4]}    ||   {p[5]}    |
        |        ||        ||        |
        ------------------------------
        |        ||        ||        |
        |   7    ||   8    ||   9    |
        |   {p[6]}    ||   {p[7]}    ||   {p[8]}    |
        |        ||        ||        |
        ------------------------------
        '''
        print(board)


    def reset_board(self):
        self.board_position = ['*', '*', '*', '*', '*', '*', '*', '*', '*']
    
    def change_value(self, symbol, position):
        self.board_position[position] = symbol
    
    def board_full(self):
        position_free = [idx+1 for idx,value in enumerate(self.board_position) if value == '*']
        if len(position_free) == 0:
            return True
        return False


class Player():

    def __init__(self, symbol):
        self.symbol = symbol
    
    def move(self, board):
        position_free = [idx+1 for idx,value in enumerate(board) if value == '*']
        print("Free Position")
        for pos in position_free:
            print(f"{pos}", end=', ')
        user_choice = int(input("Write the position: "))
        while user_choice not in position_free:
            print("Please choice a valid position!")
            user_choice = int(input("Write the position: ")) 
        else:
            return user_choice-1

    def move_auto(self, board):
        position_free = [idx+1 for idx,value in enumerate(board) if value == '*']
        rand_pos = random.choice(position_free)
        return rand_pos - 1

    def check_winner(self, board):
        if (board[0] == board[1] and board[0] == board[2] and board[0] != '*') or (board[0] == board[3] and board[0] == board[6] and board[0] != '*') or (board[0] == board[4] and board[0] == board[8] and board[0] != '*') or (board[1] == board[4] and board[1] == board[7] and board[1] != '*') or (board[2] == board[5] and board[2] == board[8] and board[2] != '*') or (board[2] == board[4] and board[2] == board[6] and board[2] != '*') or (board[3] == board[4] and board[3] == board[5] and board[3] != '*') or (board[6] == board[7] and board[6] == board[8] and board[6] != '*'):
            return True
        else:
            return False


board = Board()
player = Player('O')
pc = Player('X')
game_over = False



while not game_over:
    clear()
    print(art)
    board.print_board()
    pos_player = player.move(board.board_position)
    board.change_value(player.symbol, pos_player)
    player_win = player.check_winner(board.board_position)
    
    if player_win:
        game_over = True
        clear()
        print(art)
        board.print_board()
        print("You Win!")
        break
    elif board.board_full():
        game_over = True
        clear()
        print(art)
        board.print_board()
        print('Draw')
        break
    elif not board.board_full():
        pos_pc = pc.move_auto(board.board_position)
        board.change_value(pc.symbol, pos_pc)
        pc_win = pc.check_winner(board.board_position)
        if pc_win:
            game_over = True
            clear()
            print(art)
            board.print_board()
            print("You Lose")
            break
        elif board.board_full():
            game_over = True
            clear()
            print(art)
            board.print_board()
            print('Draw')
            break