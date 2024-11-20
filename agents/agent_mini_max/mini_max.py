import numpy as np
from game_utils import BOARD_ROWS, BOARD_COLS, BoardPiece, PLAYER1, PLAYER2, PlayerAction, MoveStatus, SavedState
from game_utils import connected_four, check_move_status, apply_player_action


def other_player(player: BoardPiece)-> BoardPiece:
    """ 
    Determines the other player, that has not been given as a parameter to the function. 

    Returns
    -------
    BoardPiece 
        BoardPiece (PLAYER1 or PLAYER2) that is not the input player parameter 

    """
    if player == PLAYER1:
        return PLAYER2
    if player == PLAYER2: 
        return PLAYER1 


def count_centre_row_pieces(board: np.ndarray, player: BoardPiece)-> int: 
    """
    Determines the amount of pieces a given player has in the 2nd, 3rd and 4th row on the board that is 
    passed as a parameter. The pieces in 3rd row are weighted as double, hence they count as two pieces. 

    Returns
    -------
    int
        Int that counts the weighted value of pieces a player has in the 3 most-centre rows. 

    """
    count= 0 
    for i in range(0,(BOARD_ROWS),1): 
        if board[i][2] == player: 
            count += 1 
        if board[i][3] == player:  
            count += 2  # Centre most row is weighted more, because it's most advantageous for player. 
        if board[i][4] == player:
            count += 1 
    return count 


def evaluate_board(board: np.ndarray, player: BoardPiece, counter: int)-> int:
    """
    Calculates the value attributed to a given board for a given player using a heuristic based
    on whether it won, lost or how many pieces it has in the centre 3 rows.
    Counter is used to factor in how soon a win/ loss will occur, so that sooner wins are valued
    higher than wins in the far future. 

    Returns
    -------
    int
        Int that represents value of board to player.

    """

    val = 0  
    if connected_four(board, player): 
        val= (100 - counter)  # Subtract counter from win, because a win earlier in the game is better than later. 
    elif connected_four(board, other_player(player)):
        val= ((-100) + counter) 
    else:  
        val= (count_centre_row_pieces(board, player))
    return val 

   
def all_possible_moves(board: np.ndarray)-> np.array: 
    """
    Creates an array of all possible moves that can be made on a given board in one turn.

    Returns
    -------
    np.array
        Array filled with col values ranging from 0-6 that represent possible moves for board
        
    """

    arr= [] 
    for i in range(0,(BOARD_COLS),1): 
        if (check_move_status(board, i)== MoveStatus.IS_VALID): 
            arr.append(i) 
    return arr 


def choose_val_from_list(arr: np.ndarray, player: BoardPiece, start_player:BoardPiece)-> tuple[int, int]:
    """
    Determines the max/min value from the given array of moves. Whether it maximises or minimises is dependent 
    on whether the player is the starting player or the second player. The starting_player is always the one
    who maximises. 

    Returns
    -------
    int
        Int that represents the highest/ lowest value of the array depending on player
    int 
        Int that represents the index of highest/ lowest value in the array 
    
    """

    val = 0
    index = 0
    if player == start_player:
        val = max(arr)
        index = np.argmax(arr) 
    else:
        val = min(arr)
        index = np.argmin(arr) 
    return val, index 


def one_level_of_branch(board: np.ndarray, start_player: BoardPiece, min_or_max_player: BoardPiece, counter: int) -> tuple[PlayerAction, int | None]: 
    """
    Calculates the best move for the start_player on the given board by evaluating all potential board states 
    that may arise from moves made by both players over the next (5 - counter) steps. 
    It assumes that the opposing player will try to pick moves that are the worst for the starting player. 

    Returns
    -------
    PlayerAction
        PlayerAction that has been calculated to be the best move or None  
    int 
        Int that represents the value of the best move or None 

    """

    if (counter <5): 
 
        possible_moves_list= all_possible_moves(board)
        value_list= [] 
         
        for move in possible_moves_list:  
            new_board= board.copy() 
            apply_player_action(new_board, move, min_or_max_player) 
            if connected_four(new_board,start_player): 
                return move,(100 - counter)   # Subtract counter from win, because a win earlier in the game is better than later.   
            elif connected_four(new_board,other_player(start_player)): 
                return move,(-100 + counter)  # Multiple returns despite causing "code smell", to increase efficiency. 
            else:
                _, val_of_this_move = one_level_of_branch(new_board,start_player,other_player(min_or_max_player),(counter+1))
                value_list.append(val_of_this_move)
        
        best_val, index_of_move = choose_val_from_list(value_list,min_or_max_player,start_player) 
        move = possible_moves_list[index_of_move]
        return move, best_val 
    
    else:
        val= evaluate_board(board, start_player,counter) 
        return 0, val  # 0 is a place holder. 


def generate_max_move(board: np.ndarray, player: BoardPiece, saved_state: SavedState | None
    ) -> tuple[PlayerAction, SavedState | None]: 
    """
    Generates the best move for the start_player on the given board by calling one_level_of_branch() 

    Returns
    -------
    PlayerAction
        PlayerAction that has been calculated to be the best move   
    SavedState 
        SavedState containing the unchanged SavedState of the game 
        
    """
    
    move, _= one_level_of_branch(board, player, player, 0)
    return move, saved_state
 