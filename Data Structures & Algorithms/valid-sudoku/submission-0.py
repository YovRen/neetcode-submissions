class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 定义哈希表：记录每一行、每一列、每个九宫格已经出现的数字
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == ".":
                    continue
                    
                # 计算属于第几个九宫格 (0-8)
                box_index = (i // 3) * 3 + j // 3
                
                # 检查是否冲突
                if num in rows[i] or num in cols[j] or num in boxes[box_index]:
                    return False
                
                # 如果不冲突，加入哈希表
                rows[i].add(num)
                cols[j].add(num)
                boxes[box_index].add(num)
                
        return True