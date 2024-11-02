from typing import Callable, Optional, Any
from enum import Enum
import numpy as np

BOARD_COLS = 7
BOARD_ROWS = 6
BOARD_SHAPE = (6, 7)
INDEX_HIGHEST_ROW = BOARD_ROWS - 1
INDEX_LOWEST_ROW = 0

BoardPiece = np.int8  # The data type (dtype) of the board pieces
NO_PLAYER = BoardPiece(0)  # board[i, j] == NO_PLAYER where the position is empty
PLAYER1 = BoardPiece(1)  # board[i, j] == PLAYER1 where player 1 (player to move first) has a piece
PLAYER2 = BoardPiece(2)  # board[i, j] == PLAYER2 where player 2 (player to move second) has a piece

BoardPiecePrint = str  # dtype for string representation of BoardPiece
NO_PLAYER_PRINT = BoardPiecePrint(' ')
PLAYER1_PRINT = BoardPiecePrint('X')
PLAYER2_PRINT = BoardPiecePrint('O')

PlayerAction = np.int8  # The column to be played

class GameState(Enum):
    IS_WIN = 1
    IS_DRAW = -1
    STILL_PLAYING = 0

class MoveStatus(Enum):
    IS_VALID = 1
    WRONG_TYPE = 'Input is not a number.'
    NOT_INTEGER = ('Input is not an integer, or isn\'t equal to an integer in '
                   'value.')
    OUT_OF_BOUNDS = 'Input is out of bounds.'
    FULL_COLUMN = 'Selected column is full.'

class SavedState:
    pass

GenMove = Callable[
    [np.ndarray, BoardPiece, Optional[SavedState]],  # Arguments for the generate_move function
    tuple[PlayerAction, Optional[SavedState]]  # Return type of the generate_move function
]


def initialize_game_state() -> np.ndarray:
    """
    Returns an ndarray, shape BOARD_SHAPE and data type (dtype) BoardPiece, initialized to 0 (NO_PLAYER).
    """
    arr = np.zeros((BOARD_SHAPE[0], BOARD_SHAPE[1]), dtype=BoardPiece)
    return arr 


def pretty_print_board(board: np.ndarray) -> str:
    """
    Should return `board` converted to a human readable string representation,
    to be used when playing or printing diagnostics to the console (stdout). The piece in
    board[0, 0] of the array should appear in the lower-left in the printed string representation. Here's an example output, note that we use
    PLAYER1_Print to represent PLAYER1 and PLAYER2_Print to represent PLAYER2):
    |==============|
    |              |
    |              |
    |    X X       |
    |    O X X     |
    |  O X O O     |
    |  O O X X     |
    |==============|
    |0 1 2 3 4 5 6 |
    """
    stri= "|==============|\n" 
    for arr in board:
        stri += "|"
        for i in arr:
            if i == PLAYER1:
                stri += PLAYER1_PRINT
            elif i == PLAYER2:
                stri += PLAYER2_PRINT
            else: 
                stri += NO_PLAYER_PRINT
            stri += " " 
        stri += "|\n" 
    stri+= "|==============|\n|0 1 2 3 4 5 6 |"   
    return (stri)
    
def print_single_line(arr: np.array) -> str: 
    line_string= "|"
    for i in arr:
        if i == PLAYER1:
            stri += PLAYER1_PRINT
        elif i == PLAYER2:
            stri += PLAYER2_PRINT
        else: 
            stri += NO_PLAYER_PRINT
        stri += " " 
    return (stri += "|") 

def string_to_board(pp_board: str) -> np.ndarray:
    """
    Takes the output of pretty_print_board and turns it back into an ndarray.
    This is quite useful for debugging, when the agent crashed and you have the last
    board state as a string.
    |==============|
    |              |
    |              |
    |    X X       |
    |    O X X     |
    |  O X O O     |
    |  O O X X     |
    |==============|
    |0 1 2 3 4 5 6 |
    """

    arr = np.zeros((BOARD_SHAPE[0], BOARD_SHAPE[1]), dtype=BoardPiece) 
    rows = pp_board.strip().split('\n')[1:-2]
    count_row= 0 

    for row in rows: 
        count_i= 0
        count_position_in_arr=0
        for i in row: 
            if (count_i % 2)!= 0 and i!="|":  
                arr[count_row][count_position_in_arr] = (
                NO_PLAYER if i == NO_PLAYER_PRINT  else
                PLAYER1 if i == PLAYER1_PRINT else
                PLAYER2 if i == PLAYER2_PRINT else NO_PLAYER
                )
                count_position_in_arr += 1
            count_i += 1
        count_row += 1
    return arr 


def apply_player_action(board: np.ndarray, action: PlayerAction, player: BoardPiece):
    """
    Sets board[i, action] = player, where i is the lowest open row. The input 
    board should be modified in place, such that it's not necessary to return 
    something.
    """
    for lowest_row in range((BOARD_ROWS - 1), -1, -1): 
        if board[lowest_row, action] == NO_PLAYER: 
            board[lowest_row, action] = player 
            return 
    print("Column was full")

#### connectedFour functions 
def connected_four(board: np.ndarray, player: BoardPiece) -> bool:
    """
    Returns True if there are four adjacent pieces equal to `player` arranged
    in either a horizontal, vertical, or diagonal line. Returns False otherwise.
    """
    return (check_row(board, player) or check_column(board,player) or check_diagonal_left(board,player) or check_diagonal_right(board,player))

def check_row(board: np.ndarray, player: BoardPiece) -> bool:
    for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS - 3):  
                if (board[row, col] == player and
                    board[row, col + 1] == player and
                    board[row, col + 2] == player and
                    board[row, col + 3] == player):
                    return True
    return False 

def check_column(board: np.ndarray, player: BoardPiece) -> bool:
    for col in range(BOARD_COLS):
        for row in range(BOARD_ROWS - 3):  
            if (board[row, col] == player and
                board[row + 1, col] == player and
                board[row + 2, col] == player and
                board[row + 3, col] == player):
                return True
    return False

def check_diagonal_left(board: np.ndarray, player: BoardPiece) -> bool:
    for row in range(3, BOARD_ROWS):
            for col in range(BOARD_COLS - 3):
                if (board[row, col] == player and
                    board[row - 1, col + 1] == player and
                    board[row - 2, col + 2] == player and
                    board[row - 3, col + 3] == player):
                    return True
    return False 

def check_diagonal_right(board: np.ndarray, player: BoardPiece) -> bool:
    for row in range(BOARD_ROWS - 3):
        for col in range(BOARD_COLS - 3):
            if (board[row, col] == player and
                board[row + 1, col + 1] == player and
                board[row + 2, col + 2] == player and
                board[row + 3, col + 3] == player):
                return True
    return False 

def check_end_state(board: np.ndarray, player: BoardPiece) -> GameState:
    """
    Returns the current game state for the current `player`, i.e. has their last
    action won (GameState.IS_WIN) or drawn (GameState.IS_DRAW) the game,
    or is play still on-going (GameState.STILL_PLAYING)?
    """
    if connected_four(board,player): 
        return GameState.IS_WIN 
    elif np.any(board == NO_PLAYER):
        return GameState.STILL_PLAYING
    else: 
        return GameState.IS_DRAW
    


def check_move_status(board: np.ndarray, column: Any) -> MoveStatus:
    """
    Returns a MoveStatus indicating whether a move is legal or illegal, and why 
    the move is illegal.
    Any column type is accepted if it is convertible to a number (e.g., '3' but 
    not 'a') and if the conversion results in a whole number (e.g., '3.0' would
    be okay, but not '3.1').
    Furthermore, the column must be within the bounds of the board and the
    column must not be full.
    """
    if isinstance(column, str):
        if column.isdigit():
            c = int(column)  
        else:
            return MoveStatus.WRONG_TYPE
    else:
        c = float(column)
        if not c.is_integer():
            return MoveStatus.NOT_INTEGER

    c= int(column)
    if (c < 0) or (c> (BOARD_COLS -1)):
        return MoveStatus.OUT_OF_BOUNDS
    elif board[0, c] != NO_PLAYER:  
        return MoveStatus.FULL_COLUMN
    
    return MoveStatus.IS_VALID