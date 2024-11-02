from game_utils import * 


#BoardPiece, BOARD_SHAPE, NO_PLAYER, PLAYER1, PLAYER2, GameState, MoveStatus, apply_player_action, check_move_status, initialize_game_state, pretty_print_board, connected_four, check_end_state, check_column, check_diagonal_left, check_diagonal_right, check_row

from enum import Enum
import numpy as np

#####################################################################
################### initialize_game_state() tests ###################
#####################################################################

def test_if_board_has_correct_2d(): 
    res_arr= initialize_game_state() 
    assert len(res_arr) == BOARD_SHAPE[0] and len(res_arr[0]) == BOARD_SHAPE[1]

def test_if_board_is_filled_with_no_player(): 
    res_arr= initialize_game_state()  
    t = True
    for arr in res_arr:
        for i in arr:
            if i != NO_PLAYER:
                t = False 
    assert t== True 

#####################################################################
################### pretty_print_board() tests ######################
##################################################################### 
emptyboard = '''|==============|\n
        |              |\n
        |              |\n
        |              |\n
        |              |\n
        |              |\n
        |              |\n
        |==============|\n
        |0 1 2 3 4 5 6 |'''

def test_if_returns_empty_board(): 
    test_array = np.zeros((BOARD_SHAPE[0], BOARD_SHAPE[1]), dtype=BoardPiece) 
    assert (pretty_print_board(test_array) == emptyboard) 

def test_if_returns_correct_board(): 
    board1='''|==============|\n
        |              |\n
        |              |\n
        |              |\n
        |O       X     |\n
        |O       O     |\n
        |X X O X X     |\n
        |==============|\n
        |0 1 2 3 4 5 6 |'''

    test_array = np.array([[0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [2, 0, 0, 0, 1, 0, 0],
                    [2, 0, 0, 0, 2, 0, 0],
                    [1, 1, 2, 1, 1, 0, 0]], dtype=BoardPiece) 

    assert (pretty_print_board(test_array) == board1)

    #####################################################################
    ###################### string_to_board tests ########################
    ##################################################################### 




    #####################################################################
    #################### apply_player_action tests ######################
    ##################################################################### 

    def test_if_works_if_no_piece(): 
        test_array = np.array([[0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [2, 0, 0, 0, 0, 0, 0],
                        [2, 0, 0, 0, 0, 2, 0],
                        [1, 1, 0, 0, 0, 1, 2]], dtype=BoardPiece) 
        apply_player_action(test_array,4,PLAYER1)
        print(test_array)
        b= np.array([[0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [2, 0, 0, 0, 0, 0, 0],
                        [2, 0, 0, 0, 0, 2, 0],
                        [1, 1, 0, 0, 1, 1, 2]], dtype=BoardPiece) 
        assert (test_array==b).all()

def test_if_works_if_there_is_piece(): 
    test_array = np.array([[0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [2, 0, 0, 0, 0, 0, 0],
                    [2, 0, 0, 0, 0, 2, 0],
                    [1, 1, 0, 0, 0, 1, 2]], dtype=BoardPiece) 
    
    apply_player_action(test_array,0,PLAYER1)
    print(test_array)

    b= np.array([[0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [1, 0, 0, 0, 0, 0, 0],
                    [2, 0, 0, 0, 0, 0, 0],
                    [2, 0, 0, 0, 0, 2, 0],
                    [1, 1, 0, 0, 0, 1, 2]], dtype=BoardPiece) 
    
    assert (test_array==b).all()
 
def test_if_column_full_it_doesnt_change_state():
    test_array = np.array([[1, 0, 0, 0, 0, 0, 0],
                    [1, 0, 0, 0, 0, 0, 0],
                    [2, 0, 0, 0, 0, 0, 0],
                    [2, 0, 0, 0, 0, 0, 0],
                    [2, 0, 0, 0, 0, 2, 0],
                    [1, 1, 0, 0, 0, 1, 2]], dtype=BoardPiece) 
    
    apply_player_action(test_array,0,PLAYER2)
    print(test_array)

    b= np.array([[1, 0, 0, 0, 0, 0, 0],
                    [1, 0, 0, 0, 0, 0, 0],
                    [2, 0, 0, 0, 0, 0, 0],
                    [2, 0, 0, 0, 0, 0, 0],
                    [2, 0, 0, 0, 0, 2, 0],
                    [1, 1, 0, 0, 0, 1, 2]], dtype=BoardPiece)
    
    assert (test_array==b).all()


#####################################################################
######################## connected_four tests #######################
##################################################################### 

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

#####################################################################
###################### check game_state tests #######################
##################################################################### 

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
    test_array= np.array([[1, 2, 1, 2, 0, 0, 0],
        [1, 2, 1, 2, 1, 2, 0],
        [2, 1, 2, 1, 2, 1, 0],
        [2, 1, 2, 1, 2, 1, 2],
        [1, 2, 1, 2, 1, 2, 1],
        [1, 2, 1, 2, 1, 2, 1]], dtype=BoardPiece)
    t = check_end_state(test_array,PLAYER2)
    b = check_end_state(test_array,PLAYER1)
    assert (t== GameState.STILL_PLAYING) and (b== GameState.STILL_PLAYING) 

#####################################################################
###################### check game_state tests #######################
##################################################################### 

def test_move_status_valid(): 
    test_array= np.array([[1, 2, 1, 2, 0, 0, 0],
        [1, 2, 1, 2, 1, 2, 0],
        [2, 1, 2, 1, 2, 1, 0],
        [2, 1, 2, 1, 2, 1, 2],
        [1, 2, 1, 2, 1, 2, 1],
        [1, 2, 1, 2, 1, 2, 1]], dtype=BoardPiece) 
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
        [2, 1, 2, 1, 2, 1, 2],
        [1, 2, 1, 2, 1, 2, 1],
        [1, 2, 1, 2, 1, 2, 1]], dtype=BoardPiece) 
    r= check_move_status(test_array, 0)
    assert (r== MoveStatus.FULL_COLUMN) 
