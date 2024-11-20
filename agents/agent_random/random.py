import numpy as np
import random as rand 
from game_utils import BoardPiece, PlayerAction, SavedState, BOARD_COLS, check_move_status, MoveStatus

def generate_move_random(board: np.ndarray, player: BoardPiece, saved_state: SavedState | None
    ) -> tuple[PlayerAction, SavedState | None]:
    free= False 
    action = 0 
    while not free: 
        action= rand.randint(0, (BOARD_COLS-1))
        if (check_move_status(board, action)) ==  MoveStatus.IS_VALID: 
            free = True 
    return action, saved_state