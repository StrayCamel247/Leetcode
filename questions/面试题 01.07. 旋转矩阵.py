class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 公式
        x = len(matrix)
        test = []
        for _ in matrix:
            test.extend(_)
        test = test[::-1]
        # print(id(matrix))
        matrix[:] = [[__ for __ in [test[(k+1)*x-(_+1)]  for k in range(x)]] for _ in range(x)]
        # print(id(matrix))

        # 翻转
        # n = len(matrix)
        # # 水平翻转
        # for i in range(n // 2):
        #     for j in range(n):
        #         matrix[i][j], matrix[n - i - 1][j] = matrix[n - i - 1][j], matrix[i][j]
        # # 主对角线翻转
        # for i in range(n):
        #     for j in range(i):
        #         matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]