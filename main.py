#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 12:29:53 2018

@author: Denizhan Akar

DESCRIPTION
An AI made from the principles which guarantee as much success as possible.

GAME: Minesweeper
TYPE: Perfect Information

TODO, by priority

Total conversion to class based system? 
- No need to constantly insert board parameter.
- Methods work more intricately.

Construct internal data representation of game
Formalize rules of game:
    ??? Make 2 modes: 
        ??? Play minesweeper on python
        Parse screen data and play
Formalize strategy to win game
    Choose starting locations anywhere other than middle
    For now choose just 4. If blank space is not found, continue pressing.
    
    Only consider empty tiles 
    
    If the number of empty tiles around warning number is equal to the 
    warning number minus bomb tiles flagged around it, they are bombs.
    
    Else: Probability

Use OpenCV to take minesweeper game data
Process data into internal data representation

Use Probability Theory to make wise choice

"""
# Main Executor
"""
This is to serve as the main decision flow of the program.
"""

# Import own modules
from Minesweeper import Minesweeper
from AI import Minesweeper_with_AI

# Game constants
row_count = 8
col_count = 8
activity_mode = "analysis"  # game/analysis/parsing
bomb_locations = [[3,3], [4,4]]
#total_bomb_count = 10

game = Minesweeper_with_AI(row_count, col_count, activity_mode, bomb_locations=bomb_locations)

game.print_board()

# Assign bombs to board.

#board = rul.change_random_tiles(row_count, col_count, board, amount=4, replace="3", strategy="no_sides")

#board = AI.probability_nearby(board)

#board= strat.probability_not_nearby(total_bomb_count, board)

game.probability_nearby()

game.probability_not_nearby()

game.print_board()


#rep.print_board(board)


