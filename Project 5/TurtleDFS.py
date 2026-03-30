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

def dfs(maze: TurtleMaze) -> bool:
    '''runs a non-recursive depth first search on the maze with backtracking
    Returns:
        True if the goal is found, False otherwise
    '''

    stack = Stack()
    start = maze.getStart()
    visited = set()

    stack.push(start)
    visited.add((start.y, start.x))
    maze.updatePosition(start)

    while not stack.is_empty():
        current = stack.peek()

        # if we reached the goal, we are done
        if current.isGoal():
            return True

        found_next = False

        # look for an unvisited neighbor
        for neighbor in get_neighbors(maze, current):
            if (neighbor.y, neighbor.x) not in visited:
                neighbor.setParent(current)
                visited.add((neighbor.y, neighbor.x))
                stack.push(neighbor)

                if not neighbor.isGoal():
                    maze.updatePosition(neighbor, Contents.TRIED)
                else:
                    maze.updatePosition(neighbor)

                found_next = True
                break

        # if no unvisited neighbor exists, backtrack
        if not found_next:
            dead_end = stack.pop()

            if dead_end != start and not dead_end.isGoal():
                maze.updatePosition(dead_end, Contents.DEAD_END)

            if not stack.is_empty():
                maze.updatePosition(stack.peek())

    return False

def main():
    maze = TurtleMaze('maze_1.txt')
    maze.drawMaze()

    solved = dfs(maze)
    print("Maze solved:", solved)

    maze.t.screen.mainloop()

if __name__ == "__main__":
    main()