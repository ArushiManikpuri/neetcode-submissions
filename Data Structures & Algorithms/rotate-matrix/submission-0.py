class Solution:
    def transpose(self, matrix: list) -> None:
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    def reverse_rows(self, matrix: list) -> None:
        for row in matrix:
            row.reverse()

    def rotate(self, matrix: List[List[int]]) -> None:
        self.transpose(matrix)
        self.reverse_rows(matrix)


        
        