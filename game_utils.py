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
    Creates a `board` of BOARD_SHAPE, filled with BoardPieces that are initialized to NO_PLAYER.

    Returns
    -------
    np.ndarray
        2d array that represents an empty board.

    """
    
    arr = np.zeros((BOARD_SHAPE[0], BOARD_SHAPE[1]), dtype=BoardPiece)
    return arr 


def pretty_print_board(board: np.ndarray) -> str:
    """
    Converts `board` to a human readable string representation, where board[0, 0] 
    of the array should appear in the lower-left in the printed string representation.

    Returns
    -------
    str
        String of the human readable string representation. 

    """

    frame_line= "|==============|\n" 
    stri= frame_line 
    

    for line in board[::-1]: 
        stri += print_single_line(line) 
    
    stri+= frame_line  
    stri+= "|0 1 2 3 4 5 6 |"   
    return (stri)
    

def print_single_line(line: np.array) -> str: 
    """
    Converts a 1D array into a String representation, where PLAYER1 = X and PLAYER2 = O.

    Returns
    -------
    str
        String of 1 line of human readable string representation. 

    """

    stri= "|"
    for val in line:
        if val == PLAYER1:
            stri += PLAYER1_PRINT
        elif val == PLAYER2:
            stri += PLAYER2_PRINT
        else: 
            stri += NO_PLAYER_PRINT
        stri += " " 
    stri += "|\n" 
    return (stri) 


def string_to_board(pp_board: str) -> np.ndarray:
    """
    Takes the output of pretty_print_board and turns it back into an ndarray.

    Returns
    -------
    np.ndarray
        2d array of size BOARD_SHAPE filled with the values of string representation. 

    """

    arr = np.zeros((BOARD_SHAPE[0], BOARD_SHAPE[1]), dtype=BoardPiece) 
    rows = pp_board.strip().split('\n')[1:-2] # Removes "board framing" lines. 
    row_index= 0
    for row in rows[::-1]: 
        arr[row_index]= convert_single_line_to_array(row)
        row_index += 1 
    return arr 


def convert_single_line_to_array(line: str)-> np.array: 
    """
    Takes a single line of the pretty_print_board representation and turns into a 1D array

    Returns
    -------
    np.array
        Array of length BOARD_SHAPE[1] filled with the values of string. 

    """

    arr = np.zeros((BOARD_SHAPE[1]), dtype=BoardPiece) 
    index_in_string= 0
    index_in_arr=0

    for character in line: 
        if (index_in_string % 2)!= 0 and character!="|":   
            arr[index_in_arr] = (
            NO_PLAYER if character == NO_PLAYER_PRINT  else
            PLAYER1 if character == PLAYER1_PRINT else
            PLAYER2 if character == PLAYER2_PRINT else NO_PLAYER
            )
            index_in_arr += 1
        index_in_string += 1
    return arr 


def apply_player_action(board: np.ndarray, action: PlayerAction, player: BoardPiece):
    """
    Sets board[i, action] = player, where i is the lowest open row. The input 
    board is modified without a return. 

    """

    for lowest_row in range(0, BOARD_ROWS, 1): 
        if board[lowest_row, action] == NO_PLAYER: 
            board[lowest_row, action] = player 
            return 


def connected_four(board: np.ndarray, player: BoardPiece) -> bool:
    """
    Checks if there are four adjacent pieces equal to `player` arranged
    in either a horizontal, vertical, or diagonal line in the inputted board. 
    
    Returns
    -------
    bool 
        True if four adjacent pieces, otherwise False. 

    """

    return (check_row(board, player) or check_column(board,player) or
             check_diagonal_left(board,player) or check_diagonal_right(board,player))


def check_row(board: np.ndarray, player: BoardPiece) -> bool:
    """
    Checks if there are four adjacent pieces equal to `player` arranged
    in a horizontal line in the inputted board. 

    Returns
    -------
    bool 
        True if four horizontal piece line of player, otherwise False. 

    """

    connected = False 
    for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS - 3):  
                if (board[row, col] == player and
                    board[row, col + 1] == player and
                    board[row, col + 2] == player and
                    board[row, col + 3] == player):
                    connected=  True
    return connected 


def check_column(board: np.ndarray, player: BoardPiece) -> bool:
    """
    Checks if there are four adjacent pieces equal to `player` arranged
    in a vertical line in the inputted board. 

    Returns
    -------
    bool 
        True if four vertical piece line of player, otherwise False. 

    """

    connected = False 
    for col in range(BOARD_COLS):
        for row in range(BOARD_ROWS - 3):  
            if (board[row, col] == player and
                board[row + 1, col] == player and
                board[row + 2, col] == player and
                board[row + 3, col] == player):
                connected = True
    return connected


def check_diagonal_left(board: np.ndarray, player: BoardPiece) -> bool:
    """
    Checks if there are four adjacent pieces equal to `player` arranged
    in a left-oriented diagonal line in the inputted board. 

    Returns
    -------
    bool 
        True if left-oriented diagonal line of four player pieces, otherwise False. 

    """

    connected = False 
    for row in range(3, BOARD_ROWS):
            for col in range(BOARD_COLS - 3):
                if (board[row, col] == player and
                    board[row - 1, col + 1] == player and
                    board[row - 2, col + 2] == player and
                    board[row - 3, col + 3] == player):
                    connected= True
    return connected 


def check_diagonal_right(board: np.ndarray, player: BoardPiece) -> bool:
    """
    Checks if there are four adjacent pieces equal to `player` arranged
    in a right-oriented diagonal line in the inputted board. 

    Returns
    -------
    bool 
        True if right-oriented diagonal line of four player pieces, otherwise False. 

    """

    connected = False 
    for row in range(BOARD_ROWS - 3):
        for col in range(BOARD_COLS - 3):
            if (board[row, col] == player and
                board[row + 1, col + 1] == player and
                board[row + 2, col + 2] == player and
                board[row + 3, col + 3] == player):
                connected= True
    return connected


def check_end_state(board: np.ndarray, player: BoardPiece) -> GameState:
    """
    Checks the current game state for the current `player`, i.e. has their last action 
    won, or drawn the game, or is play still on-going

    Returns
    -------
    GameState
        GameState(.IS_WIN, .IS_DRAW or .STILL_PLAYING) depending on the state of the game. 

    """

    if connected_four(board,player): 
        state= GameState.IS_WIN 
    elif np.any(board == NO_PLAYER):
        state= GameState.STILL_PLAYING
    else: 
        state= GameState.IS_DRAW  
    return state


def check_move_status(board: np.ndarray, column: Any) -> MoveStatus:
    """
    Checks if a move is illegal 
    
    Returns
    -------
    MoveStatus 
        MoveStatus(.WRONG_TYPE, .NOT_INTEGER, .FULLCOLUMN, .OUT_OF_BOUNDS or .IS_VALID) 
        indicating whether a move is legal or illegal, and why the move is illegal.

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
    elif board[(BOARD_ROWS-1), c] != NO_PLAYER:  
        return MoveStatus.FULL_COLUMN
    return MoveStatus.IS_VALID