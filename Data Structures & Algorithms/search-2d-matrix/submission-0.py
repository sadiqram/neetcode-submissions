class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r =len(matrix) - 1

        while l<=r:
            mid = (l + r)//2

            if  target < matrix[mid][0]:
                r = mid -1
            elif target > matrix[mid][-1] :
                l = mid + 1
            else:
                l2 = 0 
                r2 = len(matrix[mid]) - 1

                while l2 <= r2:
                    mid2 =(l2 + r2)//2
                    if matrix[mid][mid2] == target:
                        return True
                    elif matrix[mid][mid2] > target:
                        r2 = mid2 - 1
                    else:
                        l2 = mid2 + 1
                return False
        
        return False

        