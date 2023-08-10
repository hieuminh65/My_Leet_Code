def searchMatrix(matrix: list[list[int]], target: int) -> bool:
        # matrix[m][n]
        # if target < m // 2
        # [[1,3,5,7],l
        # [10,11,16,20],
        # [23,30,34,60],r


        # [70,80,94,110],
        # [223,330,434,660]]
        m = len(matrix) - 1
        n = len(matrix[0]) - 1
        l, r = 0, m
        if r == 0 and l == 0:
            if n == 0:
                return target == matrix[l][r]
            else:
                return target in matrix[l]

                # l = 0, r = 1
        while l < r:
            mid = (l + r) // 2 
            if target == matrix[mid][0]:
                return True
            if target < matrix[mid][0]:
                r = mid - 1
            else:
                l = mid + 1
        row = l
        l = 0
        r = n
        print(row, n, '\n')
        while l <= r:
            mid = (l+r) // 2
            if target == matrix[row][mid]:
                return True
            if target < matrix[row][mid]:
                r = mid - 1
            else:
                l = mid + 1
        return False 

print(searchMatrix([[1], [3]], 3))