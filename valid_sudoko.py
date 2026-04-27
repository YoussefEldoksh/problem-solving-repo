from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowsSet = set()
        colsSet = set()
        boxRowsSet = set()
        boxColsSet = set()
        row = 0

        for i in board[row]:
            if i in rowsSet:
                return False
            if i != '.':
                rowsSet.add(i)
        
            print(i)

        row = 0

        # for i in board[j]:
        #     if i in colsSet:
        #         return False
        #     if i != '.':
        #         colsSet.add(i)
        #     j += 1

result = Solution()

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

print(result.isValidSudoku(board))