######################################
# DCS 229 -- Turtle DFS
# Non-recursive depth first search for solving turtle mazes
# Date: 03/29/2026
# Name: Benjamin Adovasio
# Resources Used: Project 5 handout and TurtleMaze.py
##########################################

from __future__ import annotations

from pathlib import Path
import sys
from types import SimpleNamespace

from Stack import Stack

try:
    import turtle
    TURTLE_AVAILABLE = True
except ModuleNotFoundError:
    TURTLE_AVAILABLE = False

    class _StubTerminator(Exception):
        """Fallback replacement for turtle.Terminator."""

    class _StubScreen:
        def setworldcoordinates(self, *args) -> None:
            pass

        def tracer(self, *args) -> None:
            pass

        def update(self) -> None:
            pass

        def mainloop(self) -> None:
            pass

    class _StubTurtle:
        def __init__(self):
            self.screen = _StubScreen()

        def shape(self, *args) -> None:
            pass

        def speed(self, *args) -> None:
            pass

        def up(self) -> None:
            pass

        def goto(self, *args) -> None:
            pass

        def color(self, *args) -> None:
            pass

        def fillcolor(self, *args) -> None:
            pass

        def setheading(self, *args) -> None:
            pass

        def down(self) -> None:
            pass

        def begin_fill(self) -> None:
            pass

        def forward(self, *args) -> None:
            pass

        def right(self, *args) -> None:
            pass

        def end_fill(self) -> None:
            pass

        def dot(self, *args) -> None:
            pass

        def towards(self, *args) -> int:
            return 0

    turtle = SimpleNamespace(
        Turtle=_StubTurtle,
        Screen=_StubScreen,
        Terminator=_StubTerminator,
    )
    sys.modules["turtle"] = turtle

from TurtleMaze import Cell, Contents, TurtleMaze


class TestMaze:
    """Lightweight maze implementation used for non-GUI testing."""

    def __init__(self, maze_file_name: str | Path):
        self.maze_grid: list[list[Cell]] = []
        self._path_log: list[tuple[int, int, Contents | None]] = []

        maze_path = Path(maze_file_name)
        for row_index, line in enumerate(maze_path.read_text().splitlines()):
            row_list: list[Cell] = []
            for col_index, char in enumerate(line):
                cell = Cell(row_index, col_index, Contents(char))
                row_list.append(cell)

                if cell._contents == Contents.START:
                    self._start = cell
                if cell._contents == Contents.GOAL:
                    self._goal = cell

            self.maze_grid.append(row_list)

    def updatePosition(self, cell: Cell, val: Contents | None = None) -> None:
        """Track visited positions during tests without opening a turtle window."""
        if val is not None:
            cell._contents = val
        self._path_log.append((cell.x, cell.y, val))

    def getStart(self) -> Cell:
        return self._start

    def getGoal(self) -> Cell:
        return self._goal

    def __getitem__(self, idx: int) -> list[Cell]:
        return self.maze_grid[idx]


def get_neighbors(maze: TurtleMaze, cell: Cell) -> list[Cell]:
    """Return each non-obstacle neighbor in north, south, east, west order."""
    neighbors: list[Cell] = []
    candidate_positions = (
        (cell.y - 1, cell.x),  # north
        (cell.y + 1, cell.x),  # south
        (cell.y, cell.x + 1),  # east
        (cell.y, cell.x - 1),  # west
    )

    for row, col in candidate_positions:
        if 0 <= row < len(maze.maze_grid) and 0 <= col < len(maze[row]):
            neighbor = maze[row][col]
            if not neighbor.isBlocked():
                neighbors.append(neighbor)

    return neighbors


def _mark_solution_path(maze: TurtleMaze, goal: Cell) -> None:
    """Walk the successful route without teleporting and color it green."""
    goal_to_start: list[Cell] = []
    current: Cell | None = goal

    while current is not None:
        goal_to_start.append(current)
        current = current.getParent()

    for cell in goal_to_start:
        maze.updatePosition(cell, Contents.PART_OF_PATH)

    for cell in reversed(goal_to_start[:-1]):
        maze.updatePosition(cell, Contents.PART_OF_PATH)


def dfs(maze: TurtleMaze) -> bool:
    """Solve a maze using a non-recursive depth first search."""
    start = maze.getStart()
    stack: Stack[Cell] = Stack()
    visited: set[tuple[int, int]] = set()

    stack.push(start)
    visited.add((start.x, start.y))
    maze.updatePosition(start, Contents.TRIED)

    while not stack.is_empty():
        current = stack.peek()

        if current.isGoal():
            _mark_solution_path(maze, current)
            return True

        next_cell = None
        for neighbor in get_neighbors(maze, current):
            coordinates = (neighbor.x, neighbor.y)
            if coordinates not in visited:
                neighbor.setParent(current)
                next_cell = neighbor
                break

        if next_cell is not None:
            visited.add((next_cell.x, next_cell.y))
            stack.push(next_cell)

            if next_cell.isGoal():
                maze.updatePosition(next_cell)
            else:
                maze.updatePosition(next_cell, Contents.TRIED)
            continue

        dead_end = stack.pop()
        if dead_end != start and not dead_end.isGoal():
            maze.updatePosition(dead_end, Contents.DEAD_END)

        if not stack.is_empty():
            maze.updatePosition(stack.peek())

    return False


def _project_path(file_name: str) -> Path:
    """Return a path inside the Project 5 directory."""
    return Path(__file__).resolve().with_name(file_name)


def _test_get_neighbors() -> None:
    maze = TestMaze(_project_path("maze_1.txt"))
    start = maze.getStart()
    neighbor_coordinates = [(cell.x, cell.y) for cell in get_neighbors(maze, start)]

    assert neighbor_coordinates == [(5, 1), (3, 1)]


def _test_dfs() -> None:
    for maze_name in ("maze_1.txt", "maze_2.txt", "maze_3.txt"):
        maze = TestMaze(_project_path(maze_name))
        solved = dfs(maze)

        assert solved is True
        assert maze.getStart()._contents == Contents.PART_OF_PATH
        assert maze.getGoal()._contents == Contents.PART_OF_PATH


def main() -> None:
    _test_get_neighbors()
    _test_dfs()
    print("All TurtleDFS tests passed.")

    if not TURTLE_AVAILABLE:
        print("Skipping turtle visualization: turtle graphics are unavailable in this Python environment.")
        return

    maze_path = _project_path("maze_2.txt")
    try:
        maze = TurtleMaze(str(maze_path))
        maze.drawMaze()
        solved = dfs(maze)
        print(f"Visual DFS demo on {maze_path.name}: {solved}")
        maze.t.screen.mainloop()
    except Exception as err:
        print(f"Skipping turtle visualization: {err}")


if __name__ == "__main__":
    main()
