from agents.agent_mini_max.mini_max import * 
from enum import Enum
import numpy as np
import pytest  

# test for other_player() 

def test_if_other_player_returns_other_player(): 
    assert (other_player(PLAYER1)== PLAYER2) and (other_player(PLAYER2)== PLAYER1)


# tests for  count_centre_row_pieces() 
def test_count_none_in_centre(): 
    test_array = np.array([[2, 0, 0, 0, 0, 0, 0],
                    [2, 0, 0, 0, 0, 0, 0],
                    [2, 0, 0, 0, 0, 0, 0],
                    [2, 0, 0, 0, 0, 0, 0],
                    [1, 0, 0, 0, 0, 0, 0],
                    [1, 0, 0, 0, 0, 0, 0]], dtype=BoardPiece) 
    assert count_centre_row_pieces(test_array, PLAYER1)  == 0 


def test_count_some_in_centre(): 
    test_array = np.array([[2, 0, 1, 1, 2, 0, 0],
                    [2, 0, 0, 0, 1, 0, 0],
                    [2, 0, 0, 0, 0, 0, 0],
                    [2, 0, 0, 0, 0, 0, 0],
                    [1, 0, 0, 0, 0, 0, 0],
                    [1, 0, 0, 0, 0, 0, 0]], dtype=BoardPiece) 
    assert (count_centre_row_pieces(test_array, PLAYER1) == 4) and (count_centre_row_pieces(test_array, PLAYER2) == 1)


def test_count_full_col_in_centre(): 
    test_array = np.array([[2, 0, 1, 0, 0, 0, 0],
                    [2, 0, 1, 0, 0, 0, 0],
                    [2, 0, 1, 0, 0, 0, 0],
                    [2, 0, 1, 0, 0, 0, 0],
                    [1, 0, 1, 0, 0, 0, 0],
                    [1, 0, 1, 0, 0, 0, 0]], dtype=BoardPiece) 
    assert (count_centre_row_pieces(test_array, PLAYER1) == 6)  


# tests for evaluate_board() 

def test_correct_evaluation_of_no_win_board(): 
    test_array = np.array([[2, 0, 1, 1, 2, 0, 0],
                    [2, 0, 0, 0, 1, 0, 0],
                    [2, 0, 0, 0, 0, 0, 0],
                    [1, 0, 0, 0, 0, 0, 0],
                    [1, 0, 0, 0, 0, 0, 0],
                    [1, 0, 0, 0, 0, 0, 0]], dtype=BoardPiece)  
    assert (evaluate_board(test_array,PLAYER1,0) == 4) and (evaluate_board(test_array, PLAYER2,0)== 1)


def test_correct_evaluation_of_win_board(): 
    test_array = np.array([[2, 0, 1, 1, 2, 0, 0],
                    [2, 0, 0, 0, 2, 0, 0],
                    [2, 0, 0, 0, 2, 0, 0],
                    [2, 0, 0, 0, 2, 0, 0],
                    [1, 0, 0, 0, 0, 0, 0],
                    [1, 0, 0, 0, 0, 0, 0]], dtype=BoardPiece)  
    assert (evaluate_board(test_array,PLAYER1,0) == -100) and (evaluate_board(test_array,PLAYER2,0) == 100) and (evaluate_board(test_array,PLAYER2,1) == 99)


# tests for all_possible_moves() 

def test_if_all_possible_moves_if_all_col_possible(): 
    test_array = np.array([[2, 0, 1, 1, 1, 0, 0],
                    [2, 0, 0, 0, 2, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0]], dtype=BoardPiece)  
    possible_moves= [0,1,2,3,4,5,6] 
    a= all_possible_moves(test_array)
    assert (a== possible_moves) 


def test_if_all_possible_moves_if_some_col_full(): 
    test_array = np.array([[2, 0, 1, 1, 1, 0, 0],
                    [2, 0, 0, 0, 2, 0, 0],
                    [2, 0, 0, 0, 2, 0, 0],
                    [2, 0, 0, 0, 2, 0, 0],
                    [1, 0, 0, 0, 1, 0, 0],
                    [1, 0, 0, 0, 1, 0, 0]], dtype=BoardPiece)  
    possible_moves= [1,2,3,5,6] 
    a= all_possible_moves(test_array)
    assert (a== possible_moves) 


# tests for choose_val_from_list()

def test_if_chooses_correct_val(): 
    val_a, ind_a= choose_val_from_list([1,2,10,4,5,6], PLAYER1,PLAYER1)
    val_b, ind_b= choose_val_from_list([1,2,10,4,5,6], PLAYER2,PLAYER1) 
    assert(val_a== 10) and (ind_a == 2) and (val_b== 1) and (ind_b == 0) 


def test_if_chooses_correct_val_with_multiples(): 
    val_a, ind_a= choose_val_from_list([1,2,1,4,6,6], PLAYER1,PLAYER1)
    val_b, ind_b= choose_val_from_list([1,2,1,4,6,6], PLAYER2,PLAYER1) 
    assert(val_a== 6) and (ind_a == 4) and (val_b== 1) and (ind_b == 0) 


# tests for one_level_of_branch() 

def test_if_picks_middle_row_on_empty_board(): 
    empty_board = np.array([[0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0]], dtype=BoardPiece) 
    move, val =  one_level_of_branch(empty_board,PLAYER1,PLAYER1,0) 
    assert (move == 3)


def test_would_block_win_of_enemy(): 
    test_board = np.array([[1, 2, 1, 0, 0, 0, 0],
                    [1, 2, 0, 0, 0, 0, 0],
                    [0, 2, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0]], dtype=BoardPiece) 
    move, _ =  one_level_of_branch(test_board,PLAYER1, PLAYER1,0) 
    assert (move == 1)


def test_would_make_winning_move(): 
    test_board = np.array([[1, 1, 1, 0, 2, 0, 0],
                        [1, 2, 2, 0, 0, 0, 0],
                        [0, 2, 0, 0, 0, 0, 0], 
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0]], dtype=BoardPiece) 
    move, _ =  one_level_of_branch(test_board,PLAYER1,PLAYER1,0) 
    assert (move == 3)


def test_would_make_winning_move_if_can_block_enemy(): 
    test_board = np.array([[1, 1, 1, 0, 0, 0, 0],
                        [1, 2, 2, 0, 0, 0, 0],
                        [0, 2, 0, 0, 0, 0, 0], 
                        [0, 2, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0]], dtype=BoardPiece) 
    move, _ =  one_level_of_branch(test_board,PLAYER1,PLAYER1,0) 
    assert (move == 3)


#tests generate_max_move()

def test_if_gen_max_move_returns_same_move_as_one_level_of_branch(): 
    test_board = np.array([[1, 1, 1, 0, 0, 0, 0],
                        [1, 2, 2, 0, 0, 0, 0],
                        [0, 2, 0, 0, 0, 0, 0], 
                        [0, 2, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0]], dtype=BoardPiece) 
    saved_state= {PLAYER1: None, PLAYER2: None}
    one_branch_move, _ =  one_level_of_branch(test_board,PLAYER1,PLAYER1,0) 
    gen_max_move, _ = generate_max_move(test_board, PLAYER1, saved_state)
    assert (one_branch_move == gen_max_move)