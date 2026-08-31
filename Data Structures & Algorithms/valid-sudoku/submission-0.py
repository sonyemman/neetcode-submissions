from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #make row, col and boxes set 
        rowsDict = defaultdict(set)
        colsDict = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(len(board)): 
            for c in range(len(board[0])): 
                if board[r][c] == ".":
                    continue  
                if (board[r][c] in rowsDict[r] or 
                    board[r][c] in colsDict[c] or 
                    board[r][c] in boxes[(r // 3, c // 3)]): 
                    return False
                
                rowsDict[r].add(board[r][c])
                colsDict[c].add(board[r][c])
                boxes[(r // 3, c // 3)].add(board[r][c])

        
        return True 

                


        