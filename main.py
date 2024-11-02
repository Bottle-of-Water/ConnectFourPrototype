from typing import Callable, Optional, Any
from enum import Enum
import numpy as np 
from game_utils import pretty_print_board, BOARD_SHAPE, BoardPiece, string_to_board

def main():
    arr = np.zeros((BOARD_SHAPE[0], BOARD_SHAPE[1]), dtype=BoardPiece)
    arr[0,2]= 2
    arr[0,3]= 2
    arr[1,3]= 1
    arr[5,0]= 1
    result= pretty_print_board(arr) 
    print(result)
    l= string_to_board(result)
    print("COmPAREEEEE")
    print(pretty_print_board(l))
    q= string_to_board("""|==============|
|    O O       |
|      X       |
|              |
|O             |
|              |
|X X           |
|==============|
|0 1 2 3 4 5 6 |""")
    print(q)

if __name__ == "__main__":
    main() 

