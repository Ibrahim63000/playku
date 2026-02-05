"""
Docstring for core.grid
"""
import math
import logging

logging.basicConfig(
    level = logging.DEBUG,
    format = "{asctime}-{levelname}-{message}",
    datefmt ="%Y-%m-%d %H:%M"
)
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

    DEFAULT_GRID =  [0,0,7, 8,0,0, 4,0,0,
                     0,0,4, 0,9,3, 0,8,0,
                     3,5,0, 0,1,4, 0,0,9,
                     0,6,0, 3,0,0, 0,0,8,
                     4,7,0, 0,8,0, 0,6,3,
                     8,0,0, 0,0,9, 0,5,0,
                     1,0,0, 9,2,0, 0,7,5,
                     0,3,0, 5,7,0, 8,0,0,
                     0,0,5, 0,0,6, 9,0,0]
    
                

    def __init__(self, grid= DEFAULT_GRID, size =GRID_SIZE):
        self.size =size
        self.grid =grid

    
    @property
    def grid(self):
        return self._grid
    
    @grid.setter
    def grid(self, value):
        if not isinstance(value, list):
            raise TypeError(f"{value} must be of type list")


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
        
    def _get_box(self):
        ...