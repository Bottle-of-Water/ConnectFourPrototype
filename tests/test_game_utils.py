from game_utils import * 

from enum import Enum
import numpy as np
import pytest 


# tests for initalise_game_state() 

def test_if_board_has_correct_2d_lengths(): 
    result_array= initialize_game_state() 
    assert len(result_array) == BOARD_SHAPE[0] and len(result_array[0]) == BOARD_SHAPE[1]


def test_if_board_is_filled_with_no_player(): 
    res_arr= initialize_game_state()  
    t = True
    for arr in res_arr:
        for i in arr:
            if i != NO_PLAYER:
                t = False 
    assert t== True 


# tests for pretty_print_board() and its helper function 

def test_single_empty_line(): 
    empty_line = np.zeros(BOARD_SHAPE[1], dtype= BoardPiece)
    result = print_single_line(empty_line) 
    assert (result == "|              |\n") 


def test_single_filled_line(): 
    random_line = np.array([0,0,1,2,0,2,0], dtype=BoardPiece)
    result = print_single_line(random_line) 
    assert (result == "|    X O   O   |\n") 


emptyboard='''|==============|
|              |
|              |
|              |
|              |
|              |
|              |
|==============|
|0 1 2 3 4 5 6 |'''


board1='''|==============|
|X X O X X     |
|O       O     |
|O       X     |
|              |
|              |
|              |
|==============|
|0 1 2 3 4 5 6 |'''


def test_if_returns_empty_board(): 
    test_array = np.zeros((BOARD_SHAPE[0], BOARD_SHAPE[1]), dtype=BoardPiece) 
    result = pretty_print_board(test_array)
    assert (result == emptyboard) 


def test_if_returns_correct_filled_board(): 
    test_array = np.array([[0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [2, 0, 0, 0, 1, 0, 0],
                    [2, 0, 0, 0, 2, 0, 0],
                    [1, 1, 2, 1, 1, 0, 0]], dtype=BoardPiece) 

    assert (pretty_print_board(test_array) == board1)


# tests for string_to_board() and its helper function

def test_if_filled_line_becomes_array(): 
    str = "|X X O X X     |"
    test_array = np.array([1,1,2,1,1,0,0], dtype=BoardPiece)
    assert (convert_single_line_to_array(str) == test_array).all() 


def test_if_empty_line_becomes_array(): 
    str = "|              |"
    test_array = np.zeros((BOARD_SHAPE[1]), dtype=BoardPiece) 
    assert (convert_single_line_to_array(str) == test_array).all() 


def test_if_empty_board_becomes_array(): 
    empty_test_board = np.zeros((BOARD_SHAPE[0],BOARD_SHAPE[1]), dtype=BoardPiece) 
    assert (string_to_board(emptyboard) == empty_test_board).all() 


def test_if_filled_board_becomes_array(): 
    test_board = np.array([[0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [2, 0, 0, 0, 1, 0, 0],
                    [2, 0, 0, 0, 2, 0, 0],
                    [1, 1, 2, 1, 1, 0, 0]], dtype=BoardPiece)
    assert ((string_to_board(board1) == test_board).all()) 


#tests for apply_player_action()

def test_if_applies_action_if_no_piece(): 
    a = np.array([[0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]], dtype=BoardPiece) 
    apply_player_action(a,4,PLAYER1)
    b= np.array([[0, 0, 0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0]], dtype=BoardPiece) 
    assert (a==b).all()


def test_if_applies_action_if_there_is_pieces(): 
    a = np.array([[1, 1, 0, 0, 0, 0, 0],
                    [2, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0]], dtype=BoardPiece) 
    apply_player_action(a,0,PLAYER2)
    b = np.array([[1, 1, 0, 0, 0, 0, 0],
                    [2, 0, 0, 0, 0, 0, 0],
                    [2, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0]], dtype=BoardPiece)  
    assert (a==b).all()
 

def test_if_column_full_action_doesnt_change_state():
    a = np.array([[1, 0, 0, 0, 0, 0, 0],
                    [1, 0, 0, 0, 0, 0, 0],
                    [2, 0, 0, 0, 0, 0, 0],
                    [2, 0, 0, 0, 0, 0, 0],
                    [2, 0, 0, 0, 0, 0, 0],
                    [1, 0, 0, 0, 0, 0, 0]], dtype=BoardPiece) 
    b = np.array([[1, 0, 0, 0, 0, 0, 0],
                    [1, 0, 0, 0, 0, 0, 0],
                    [2, 0, 0, 0, 0, 0, 0],
                    [2, 0, 0, 0, 0, 0, 0],
                    [2, 0, 0, 0, 0, 0, 0],
                    [1, 0, 0, 0, 0, 0, 0]], dtype=BoardPiece) 
    apply_player_action(a,0,PLAYER2)
    assert (b==a).all()


#tests for connected_four()

def test_four_above_each_other(): 
    test_array = np.array([[2, 0, 0, 0, 0, 0, 0],
                    [2, 0, 0, 0, 0, 0, 0],
                    [2, 0, 0, 0, 0, 0, 0],
                    [2, 0, 0, 0, 0, 0, 0],
                    [1, 0, 0, 0, 0, 0, 0],
                    [1, 0, 0, 0, 0, 0, 0]], dtype=BoardPiece) 
    t = connected_four(test_array,PLAYER2)  #correct player 
    b = connected_four(test_array,PLAYER1)  #wrong player 
    assert (t == True) and (b==False)


def test_four_next_to_each_other(): 
    test_array = np.array([[0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 2, 0],
                    [1, 1, 1, 1, 0, 1, 2]], dtype=BoardPiece) 
    
    test_array_wrong = np.array([[0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 2, 0],
                    [1, 1, 1, 0, 0, 1, 2]], dtype=BoardPiece) 
    t = connected_four(test_array,PLAYER1)
    b = connected_four(test_array,PLAYER2) 
    tw= connected_four(test_array_wrong,PLAYER1)
    bw= connected_four(test_array_wrong,PLAYER1)
    assert (t== True) and (b == False) and (tw == False) and (bw ==False) 


def test_four_diagonal_right(): #/ 
    test_array = np.array([[0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 2, 0, 0, 0],
                    [0, 0, 2, 0, 0, 0, 0],
                    [0, 2, 0, 0, 0, 2, 0],
                    [2, 0, 0, 1, 0, 1, 2]], dtype=BoardPiece) 
    t = connected_four(test_array,PLAYER2) 
    b = connected_four(test_array,PLAYER1) 
    assert (t == True) and (b== False)
 

def test_four_diagonal_left(): #\ 
    test_array = np.array([[0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 2, 0, 0, 0],
                    [0, 1, 0, 0, 2, 0, 0],
                    [0, 2, 0, 0, 0, 2, 0],
                    [1, 2, 2, 0, 0, 1, 2]], dtype=BoardPiece) 
    t = connected_four(test_array,PLAYER2) 
    b = connected_four(test_array,PLAYER1) 
    assert (t == True) and (b== False) 


#tests for check_end_state() 

def test_win_state(): 
    test_array = np.array([[2, 0, 0, 0, 0, 0, 0],
                    [2, 0, 0, 0, 0, 0, 0],
                    [2, 0, 0, 0, 0, 0, 0],
                    [2, 0, 0, 0, 0, 0, 0],
                    [1, 0, 0, 1, 2, 1, 0],
                    [1, 1, 1, 2, 2, 1, 1]], dtype=BoardPiece)
    t = check_end_state(test_array,PLAYER2)
    b = check_end_state(test_array,PLAYER1)
    assert (t== GameState.IS_WIN) and (b== GameState.STILL_PLAYING) 


def test_draw_state(): 
    test_array = np.array([[1, 2, 1, 2, 1, 2, 1],
                    [1, 2, 1, 2, 1, 2, 1],
                    [2, 1, 2, 1, 2, 1, 2],
                    [2, 1, 2, 1, 2, 1, 2],
                    [1, 2, 1, 2, 1, 2, 1],
                    [1, 2, 1, 2, 1, 2, 1]], dtype=BoardPiece)
    t = check_end_state(test_array,PLAYER2)
    b = check_end_state(test_array,PLAYER1)
    assert (t== GameState.IS_DRAW) and (b== GameState.IS_DRAW) 


def test_still_playing_state(): 
    test_array = np.array([[1, 2, 1, 2, 1, 2, 1],
                    [1, 2, 1, 2, 1, 2, 1],
                    [2, 1, 2, 1, 2, 0, 0],
                    [2, 1, 2, 1, 2, 0, 0],
                    [1, 2, 1, 2, 1, 0, 0],
                    [1, 2, 1, 2, 1, 0, 0]], dtype=BoardPiece)
    t = check_end_state(test_array,PLAYER2)
    b = check_end_state(test_array,PLAYER1)
    assert (t== GameState.STILL_PLAYING) and (b== GameState.STILL_PLAYING) 


#tests for check_move_status() 

def test_move_status_valid(): 
    test_array= np.array([[1, 2, 1, 2, 0, 0, 0],
        [1, 2, 1, 2, 1, 2, 0],
        [2, 1, 2, 1, 2, 1, 0],
        [2, 1, 2, 1, 2, 1, 0],
        [1, 2, 1, 2, 1, 2, 0],
        [1, 2, 1, 2, 1, 2, 0]], dtype=BoardPiece) 
    r= check_move_status(test_array, 6)
    r= check_move_status(test_array, 6.0)
    r= check_move_status(test_array, '6')
    assert (r== MoveStatus.IS_VALID)


def test_move_status_wrong_type(): 
    test_array= np.array([[1, 2, 1, 2, 0, 0, 0],
        [1, 2, 1, 2, 1, 2, 0],
        [2, 1, 2, 1, 2, 1, 0],
        [2, 1, 2, 1, 2, 1, 2],
        [1, 2, 1, 2, 1, 2, 1],
        [1, 2, 1, 2, 1, 2, 1]], dtype=BoardPiece) 
    r= check_move_status(test_array, 'a')
    assert (r== MoveStatus.WRONG_TYPE)


def test_move_status_not_integer(): 
    test_array= np.array([[1, 2, 1, 2, 0, 0, 0],
        [1, 2, 1, 2, 1, 2, 0],
        [2, 1, 2, 1, 2, 1, 0],
        [2, 1, 2, 1, 2, 1, 2],
        [1, 2, 1, 2, 1, 2, 1],
        [1, 2, 1, 2, 1, 2, 1]], dtype=BoardPiece) 
    r= check_move_status(test_array, 6.1)
    assert (r== MoveStatus.NOT_INTEGER)


def test_move_status_out_of_bounds(): 
    test_array= np.array([[1, 2, 1, 2, 0, 0, 0],
        [1, 2, 1, 2, 1, 2, 0],
        [2, 1, 2, 1, 2, 1, 0],
        [2, 1, 2, 1, 2, 1, 2],
        [1, 2, 1, 2, 1, 2, 1],
        [1, 2, 1, 2, 1, 2, 1]], dtype=BoardPiece) 
    r= check_move_status(test_array, 7)
    assert (r== MoveStatus.OUT_OF_BOUNDS)


def test_move_status_full_column(): 
    test_array= np.array([[1, 2, 1, 2, 0, 0, 0],
        [1, 2, 1, 2, 1, 2, 0],
        [2, 1, 2, 1, 2, 1, 0],
        [2, 1, 2, 1, 2, 1, 0],
        [1, 2, 1, 2, 1, 2, 0],
        [1, 2, 1, 2, 1, 2, 0]], dtype=BoardPiece) 
    r= check_move_status(test_array, 0)
    assert (r== MoveStatus.FULL_COLUMN) 
