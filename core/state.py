"""
Core.state:
-Keeps track of player entries to enable moving back to a former state
"""
import logging
from  .grid import SudokuGrid

logging.basicConfig(
    level = logging.DEBUG,
    format = "{asctime}-{levelname}-{message}",
    datefmt ="%Y-%m-%d %H:%M",
    style="{"
)
logger = logging.getLogger(__name__)


class SudokuState:

    def __init__(self, grid: SudokuGrid, state):
        self.grid = grid
        self.state =state

    def update_state(self):
        ...

    def rollback_state(self):
        ...

if __name__ == "__main__":
    print("Tests here")