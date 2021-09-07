class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        master = defaultdict(list)
        sub_board = defaultdict(list)
        for r in range(len(board)):
            temp = []
            if r%3==0:
                sub_board = defaultdict(list)
            for c in range(len(board[0])):
                if board[r][c] != ".":
                    if board[r][c] in temp or board[r][c] in master[c] or board[r][c] in sub_board[c//3]:
                        return False
                    else:
                        master[c].append(board[r][c])
                        sub_board[c//3].append(board[r][c])
                        temp.append(board[r][c])
        return True
