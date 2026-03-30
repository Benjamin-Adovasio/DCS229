######################################
# DCS 229 -- TurtleDFS
# Depth-First Search implementation for Turtle Maze
# Date: 03/29/2026
# Name: Benjamin Adovasio
# Resources Used: I worked with Pat Cohen on the project.
##########################################

import os
from Stack import Stack
from TurtleMaze import TurtleMaze, Cell, Contents

def get_neighbors(maze: TurtleMaze, cell: Cell) -> list[Cell]:
    '''returns a list of non-obstacle neighbors in north, south, east, west order'''

    neighbors = []
    row = cell.y
    col = cell.x

    # north
    if row - 1 >= 0:
        north = maze[row - 1][col]
        if not north.isBlocked():
            neighbors.append(north)

    # south
    if row + 1 < len(maze.maze_grid):
        south = maze[row + 1][col]
        if not south.isBlocked():
            neighbors.append(south)

    # east
    if col + 1 < len(maze[0]):
        east = maze[row][col + 1]
        if not east.isBlocked():
            neighbors.append(east)

    # west
    if col - 1 >= 0:
        west = maze[row][col - 1]
        if not west.isBlocked():
            neighbors.append(west)

    return neighbors