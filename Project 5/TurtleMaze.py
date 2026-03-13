######################################
# DCS 229 -- TurtleMaze
# Utility file with the TurtleMaze class.
# Date: March 13, 2026
# Name: Prof. Andy Ricci
# Resources Used: https://runestone.academy/ns/books/published/pythonds/Recursion/ExploringaMaze.html
##########################################

from __future__ import annotations

from enum import Enum
import turtle



################################################################################
class Contents(str, Enum):
    ''' create an enumeration to define what the visual contents of a Cell are;
        using str as a "mixin" (multiple inheritance) forces all the entries to
        be strings; using an Enum means no cell entry can be anything other
        than the options here
    '''

    EMPTY = ' '
    START = 'S'
    GOAL = 'G'
    PART_OF_PATH = 'O'
    TRIED = '.'
    OBSTACLE = '+'
    DEAD_END = '-'

    def __str__(self) -> str:
        return self.value


################################################################################
class Cell:
    ''' class that allows us to use Cell as a data type -- an ordered triple
        of row, column, & cell contents
        (see Contents class enumeration above)
    '''

    def __init__(self, row: int, col: int, contents: Contents):
        self._contents: Contents = contents
        self._parent: Cell = None  # parent of this Cell during exploration
        self.x = col
        self.y = row

    def getParent(self) -> Cell:
        ''' method to return the parent of this Cell object as determined during
            maze exploration
        Returns:
            a Cell object corresponding to the cell that considered this cell
            during the exploration process
        '''
        return self._parent

    def setParent(self, parent: Cell) -> None:
        ''' setter method to update this Cell's parent
        Parameters:
            parent: a different Cell object
        Raises:
            ValueError if self == parent
        '''
        if self == parent: raise ValueError(f"a Cell cannot be its own parent")
        self._parent = parent

    def markOnPath(self) -> None:
        ''' method to identify this cell as being on the path from source
            to goal
        '''
        self._contents = Contents.PART_OF_PATH

    def isBlocked(self) -> bool:
        ''' Boolean method to indicate whether this cell contains a block
        Returns:
            True if the cell is blocked (cannot be explored), False o/w
        '''
        return self._contents == Contents.OBSTACLE

    def isGoal(self) -> bool:
        ''' Boolean method to indicate whether this cell is the goal
        Returns:
            True if the cell is the maze goal, False o/w
        '''
        return self._contents == Contents.GOAL

    def __str__(self) -> str:
        ''' creates and returns a string representation of this cell
        Returns:
            a string identifying the cell's row, col, and cell contents
        '''
        string = f"({self.x}, {self.y}, {self._contents}) "
        if self._parent is not None:
            string += f"Parent is: ({self._parent.x}, {self._parent.y})"
        return string

    def __repr__(self) -> str:
        ''' overriding __repr__ so that printing, e.g., a list of Cell objects
            (which will call __repr__ for each) will call __str__ for each, printing
            nicely
        Returns:
            a string identifying the cell's row, col, and cell contents
        '''
        return self.__str__()

    def __eq__(self, other: Cell) -> bool:
        ''' indicates whether a given other Cell is equal to this Cell
        Returns:
            True if this Cell and the other Cell are the same, False o/w
        '''
        return self.x == other.x and \
            self.y == other.y


################################################################################
class TurtleMaze:
    def __init__(self, mazeFileName):
        rowsInMaze = 0
        columnsInMaze = 0
        self.maze_grid = []
        mazeFile = open(mazeFileName, 'r')
        rowsInMaze = 0
        for line in mazeFile:
            rowList = []
            col = 0
            for ch in line[:-1]:  #
                # make new cell:  (row, col, contents)
                cell = Cell(rowsInMaze, col, ch)
                rowList.append(cell)
                if ch == Contents.START:
                    self.startRow = rowsInMaze
                    self.startCol = col
                    self._start = cell
                if ch == Contents.GOAL:
                    self._goal = cell

                col = col + 1
            rowsInMaze = rowsInMaze + 1
            self.maze_grid.append(rowList)
            columnsInMaze = len(rowList)

        self._num_rows = rowsInMaze
        self._num_cols = columnsInMaze
        self.xTranslate = -columnsInMaze / 2
        self.yTranslate = rowsInMaze / 2
        self.t = turtle.Turtle()
        self.t.shape('turtle')
        self.wn = turtle.Screen()
        self.wn.setworldcoordinates(-(columnsInMaze - 1) / 2 - .5, -(rowsInMaze - 1) / 2 - .5,
                                    (columnsInMaze - 1) / 2 + .5, (rowsInMaze - 1) / 2 + .5)


    def drawMaze(self):
        self.t.speed(10)
        self.wn.tracer(0)
        for y in range(self._num_rows):
            for x in range(self._num_cols):
                cell = self.maze_grid[y][x]
                if cell._contents == Contents.OBSTACLE:
                    self.drawCenteredBox(x + self.xTranslate, -y + self.yTranslate, 'orange')
        self.updatePosition(self.getStart())
        self.t.color('black')
        self.t.fillcolor('blue')
        self.wn.update()
        self.wn.tracer(1)

    def drawCenteredBox(self, x, y, color):
        self.t.up()
        self.t.goto(x - .5, y - .5)
        self.t.color(color)
        self.t.fillcolor(color)
        self.t.setheading(90)
        self.t.down()
        self.t.begin_fill()
        for i in range(4):
            self.t.forward(1)
            self.t.right(90)
        self.t.end_fill()

    def moveTurtle(self, x, y):
        self.t.up()
        self.t.setheading(self.t.towards(x + self.xTranslate, -y + self.yTranslate))
        self.t.goto(x + self.xTranslate, -y + self.yTranslate)

    def dropBreadcrumb(self, color):
        self.t.dot(10, color)

    def updatePosition(self, cell, val=None):
        if val:
            cell._contents = val
        self.moveTurtle(cell.x, cell.y)

        if val == Contents.PART_OF_PATH:
            color = 'green'
        elif val == Contents.TRIED:
            color = 'black'
        elif val == Contents.DEAD_END:
            color = 'red'
        else:
            color = None

        if color:
            self.dropBreadcrumb(color)


    def getStart(self) -> Cell:
        ''' accessor method to return the Cell object corresponding to the Maze start
        Returns:
            the Cell object at the Maze start location
        '''
        return self._start

    def getGoal(self) -> Cell:
        ''' accessor method to return the Cell object corresponding to the Maze goal
        Returns:
            the Cell object at the Maze goal location
        '''
        return self._goal

    def __getitem__(self, idx):
        """
        Magic method for accessing element with square brackets []

        Example usage:

        maze = TurtleMaze(file)
        maze[4] # the row at index 4 (the 5th row in the maze)
        maze[4][0] # the first cell in the row at index 4
        """

        return self.maze_grid[idx]



def main():

    maze = TurtleMaze('maze_3.txt')
    maze.drawMaze()
    # print("row at index 4", maze[4])
    # print("cell at index 4, 4", maze[4][4])

    maze.updatePosition(maze.getStart())
    print(maze.getStart())

    maze.t.screen.mainloop()


if __name__ == "__main__":
    main()