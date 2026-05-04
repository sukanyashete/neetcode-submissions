class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seenrow = set()
        seencol = set()
        seenbox = [set() for i in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    # row check
                    if board[i][j] in seenrow:
                        print(f"Row fail at {i},{j}: {board[i][j]}")
                        return False
                    else:
                        seenrow.add(board[i][j])
                if board[j][i] != ".":
                    # column check
                    if board[j][i] in seencol:
                        print(f"Col fail at {i},{j}: {board[j][i]}")
                        return False
                    else:
                        seencol.add(board[j][i])
                    # 3x3 sub boxes check
                whichbox = (i // 3) * 3 + (j // 3)
                if board[i][j] != ".":
                    if board[i][j] in seenbox[whichbox]:
                        print(f"Box fail at {i},{j}: {board[i][j]}")
                        return False
                    else:
                        seenbox[whichbox].add(board[i][j])

            seenrow = set()
            seencol = set()

        return True