class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hors = {}
        vers = {}
        cubs = {}
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                if row in hors:
                    if board[row][col] in hors[row]:
                        return False
                    else:
                        hors[row].append(board[row][col])
                else:
                    hors[row] = [board[row][col]]

                if col in vers:
                    if board[row][col] in vers[col]:
                        return False
                    else:
                        vers[col].append(board[row][col])
                else:
                    vers[col] = [board[row][col]]

                sq = (row//3)*3 + (col//3)
                if sq in cubs:
                    if board[row][col] in cubs[sq]:
                        return False
                    else:
                        cubs[sq].append(board[row][col])
                else:
                    cubs[sq] = [board[row][col]]

                
                

        return True
            