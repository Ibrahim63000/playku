"""
Docstring for core.grid
"""
import math
import logging

logger = logging.getLogger(__name__)

class SudokuGrid:
    """
    Docstring for SudokuGrid
    This class:
    1. represents the 9*9 grid as a data structure
    2. Know which cells are fixed clues vs player editable
    3. Validate moves against Sudoku rules
    4. Check for completion
    """
    GRID_SIZE =9

    def init(self, size =GRID_SIZE):
        self.size =size

    def generate_grid(self):
        """
        Generate a new grid based
        """
        ...

    def validate_grid(self):
        """
        Is the grid valid
        """
        ...

    def is_grid_complete(self):
        "Check if grid is completed"
        ...

    def _get_fixed_squares(self):
        """
        Return position of clues vs player editable squares
        """
        ...

    def _get_box_size(self):
        box_size = math.sqrt(self.size)
        if box_size -int(box_size) ==0:
            return box_size
        else:
            logger.warning("box size is not an integer. The sudodu grid is not standard")
            return NotImplemented
        