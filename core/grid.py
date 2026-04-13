"""
Docstring for core.grid
"""
import math
import logging

logging.basicConfig(
    level = logging.DEBUG,
    format = "{asctime}-{levelname}-{message}",
    datefmt ="%Y-%m-%d %H:%M",
    style="{"
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
            raise TypeError(f"{value} must be of type array")
        if any([elt<= self.GRID_SIZE  for elt in value]):
            self._grid = value


    def validate_grid(self):
        """
        Is the grid valid
        """
        ...

    def is_grid_complete(self):
        "Check if grid is completed"
        return 0 not in self.grid

    def _get_fixed_squares(self):
        """
        Return position of clues vs player editable squares
        """
        ...

    def _get_box_size(self):
        box_size = math.sqrt(self.size)
        if box_size -int(box_size) ==0:
            return int(box_size)
        else:
            logger.warning("box size is not an integer. The sudodu grid is not standard")
            return NotImplemented
        
    def _get_row(self, row_number):
        return self.grid[row_number*self.size:(row_number+1)*self.size]
    
    def _get_col(self, col_number):
        return [self._get_row(row)[col_number] for row in range(self.GRID_SIZE)]
        
    def _get_box(self, position =(0,0)):
        box_size = self._get_box_size()
        box_rows = [position[0]*box_size +row for row in range(box_size)]
        box_cols = [position[1]*box_size +col for col in range(box_size)]
        return [self._get_row(row)[col] for row in box_rows for col in box_cols]