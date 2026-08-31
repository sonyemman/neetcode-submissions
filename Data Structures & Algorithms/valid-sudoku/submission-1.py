class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = len(board), len(board[0])
        rowsSet = [set() for _ in range(ROWS)]
        colSet = [set() for _ in range(COLS)]
        boxSet = [set() for _ in range(ROWS)]  

        for i in range(ROWS): 
            for j in range(COLS): 
                if board[i][j] != '.': 
                    
                    if board[i][j] in rowsSet[i]:
                        return False
                    rowsSet[i].add(board[i][j])

                    if board[i][j] in colSet[j]:
                        return False
                    colSet[j].add(board[i][j])
                    
                    box_index = (i // 3) * 3 + (j // 3)
                    if board[i][j] in boxSet[box_index]: 
                        return False
                    boxSet[box_index].add(board[i][j])
                    
        return True