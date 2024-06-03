class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        left, right = 0 , len(matrix) - 1

        while left < right:
            for i in range(right - left):

                top, btm = left, right

                topLeft = matrix[top][left + i]

                matrix[top][left + i] = matrix[btm - i][left]

                matrix[btm - i][left] = matrix[btm][right - i]

                matrix[btm][right - i] = matrix[top + i][right]

                matrix[top + i][right] = topLeft

            left += 1
            right -= 1