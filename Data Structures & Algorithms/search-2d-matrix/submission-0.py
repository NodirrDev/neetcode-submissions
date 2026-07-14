class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r_len = len(matrix[0])
        c_len = len(matrix)
        r = c_len * r_len - 1
        while l<=r:
            mid = (l+r)//2
            c = mid//r_len
            ri = mid%r_len
            if matrix[c][ri] == target:
                return True
            elif matrix[c][ri] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False