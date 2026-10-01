class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_tally = [SudokuCounter(f"row {i}") for i in range(len(board))]
        col_tally = [SudokuCounter(f"col {j}") for j in range(len(board))]
        sq_tally  = [[SudokuCounter(f"row {i} col {j}") for j in range(3)] for i in range(3)]

        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] == ".": continue 
                # row tally
                if not row_tally[row].s_add(board[row][col]): return False
                # col tally
                if not col_tally[col].s_add(board[row][col]): return False
                # sub square tally
                if not sq_tally[int(row/3)][int(col/3)]. \
                    s_add(board[row][col]): return False

        return True

class SudokuCounter:

    def __init__(self, name: string) -> 'SudokuCounter':
        self.__name = name
        self.__tally = dict()
        return
    
    def s_add(self, n: int) -> bool:
        self.__tally[n] = self.__tally.get(n, 0) + 1
        return True if self.__tally.get(n) == 1  else False

    def name(self) -> str:
        return self.__name