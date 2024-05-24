class Solution(object):
    def isValidSudoku(self, board):
        rows = [[] for _ in range(9)]
        columns = [[] for _ in range(9)]
        box = [[] for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != ".":
                    box_index = (i // 3) * 3 + (j // 3)
                    if num in rows[i] or num in columns[j] or num in box[box_index]:
                        return False
                    rows[i].append(num)
                    columns[j].append(num)
                    box[box_index].append(num)

        return True