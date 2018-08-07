#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 00:09:14 2018

@author: denizhan
"""

# Formalized Strategy
import representation as rep
from random import randint

# GET Functions

def get_numbered_tiles(board):
    numbered_tiles = [] # [[tile_row, tile_col, number], ...]
        
    for row_index, row in enumerate(board):
        for col_index, item in enumerate(row):
            if item.isdigit():
                numbered_tiles.append([row_index, col_index, int(item)])
    return numbered_tiles


def get_tiles_around_tile(tile_loc, board):
    """
    Returns [[row, col, tile_type], ...]
    """
    around_tile = []
#   Shorten variables
    row = tile_loc[0]
    col = tile_loc[1]
    
    for i in range(-1, 2):
        for k in range(-1, 2):
            if not (i== 0 and k== 0):
                around_tile.append([row+i, col+k, rep.get_tile([row+i, col+k], board)])
    
    return around_tile

# CHANGE Functions

def change_random_tiles(row_count, col_count, board, amount=4, strategy="no_sides"):
    """
    HACK: Choose 4 random tiles not at the sides or corners.
    HACK: Just replace with 8
    """
    for i in range(amount):
        if strategy == "no_sides":
            tile_loc = [randint(2, row_count-1), randint(2, col_count-1)]
            board = rep.change_tile(tile_loc, "8", board)
            rep.print_board(board)  
    return board

#Get indexes for every numbered tile:

#for index in [range(row_count), range(col_count)]:
#for i in [col for col,x in enumerate(testlist) if x.isdigit()]:


# OPTIMIZE by skipping numbers already known.



def change_tiles_around_tile(tile_loc, condition, change, board):
    around_tile = get_tiles_around_tile(tile_loc, board)
    
    for tile_info in around_tile:
        if tile_info[2] == condition:
            board = rep.change_tile(tile_info[:2], change, board)
    
    return board

# STRATEGY Functions

def unknowns_around_equal_to_number_tile(numbered_tiles, board):
    #For every numbered tile:
    for numbered_tile in numbered_tiles:
    #   Check all nearby tiles
        tile_loc = numbered_tile[:2]
        number = numbered_tile[2]
        around_tile = get_tiles_around_tile(tile_loc, board)
    
    #   if number of unknown tiles == number of tile - flagged tiles:
    #       flag those unknown tiles
        unknown_count = 0
        for tile in around_tile:
            if tile[2] == "?":
                unknown_count += 1
            elif tile[2] == "F":
                number -= 1
            if unknown_count == number:
                board = change_tiles_around_tile(tile_loc, "?", "F", board)
                break
    return board


"""
If we cannot find a trivial next tile, we will be using Probability Theory.

In the event that no trivial tile can be flagged or opened, we have two methods: 
for nearby unknown tiles and for remaining non-nearby unknown tiles.

Nearby method is to go through every numbered tile, count number of empty tiles
around it, and divide the number of the numbered tile by the number of empty tiles. 
This gives us the probability that the unknown tiles will be a bomb.

The found probability value is assigned to the unknown tiles nearby the 
numbered tile. As individual unknown tiles get different probability values 
from more than one numbered tile, an average (?perhaps a better way is available?) 
is taken for that unknown tile. The tile with the least probability is chosen.

Non-nearby method is to assess the probability that any non-nearby unknown 
tile has a bomb. This is done by calculating the minimum number of possible 
bombs nearby (worst case scenario if choosing non-nearby unknown tile) and 
substracting that from the number of non-flagged tiles. We divide our resulting
number by the quantity of non-nearby numbers. This gives us the probability that
one of the non-nearby tiles is a bomb.

We then compare the lowest probability nearby tile with the non-nearby tiles'
probability.
If individual tile, choose that.
If non-nearby or equal, choose random tile which is not near walls.
"""
