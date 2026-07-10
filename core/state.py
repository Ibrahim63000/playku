"""
Core.state:
-Keeps track of player entries to enable moving back nd forth over states
"""

import logging
from .grid import SudokuGrid

logging.basicConfig(
    level=logging.DEBUG,
    format="{asctime}-{levelname}-{message}",
    datefmt="%Y-%m-%d %H:%M",
    style="{",
)
logger = logging.getLogger(__name__)


class SudokuState:

    def __init__(self, initial_state: SudokuGrid):
        """."""
        self.initial_state = initial_state
        self.states = [(self.initial_state, None)]
        self.fixed_squares = initial_state._get_fixed_squares()

    def update_state(self, move_square, move_value):
        """."""
        if move_square[0] not in range(self.initial_state.size) or move_square[
            1
        ] not in range(self.initial_state.size):
            raise ValueError("The coordinates are outside of the sudoku grid")
        elif move_value not in range(self.initial_state.size + 1):
            raise ValueError(
                f"only {",".join([str(elt) for elt in range(1,self.initial_state.size+1)])} are permitted"
            )
        new_grid = self.initial_state.grid.copy()
        new_grid[move_square[0] * self.initial_state.size + move_square[1]] = move_value
        new_state = SudokuGrid(grid=new_grid, size=self.initial_state.size)
        return new_state

    def rollback_state(self):
        """."""
        ...


if __name__ == "__main__":
    print("Tests here")
