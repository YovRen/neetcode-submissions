class Solution:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""
        encoded_string = ""
        for s in strs:
            # 格式：长度 + "#" + 字符串本身
            encoded_string += str(len(s)) + "#" + s
        return encoded_string

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""
        strs = []
        i = 0
        while i < len(s):
            # 1. 找数字和 '#' 的位置
            j = i
            while s[j] != '#':
                j += 1
            
            # 2. 提取出长度
            length = int(s[i:j])
            
            # 3. 根据长度，直接截取字符串本身
            # 字符串的起点是 j+1，终点是 j+1+length
            strs.append(s[j+1 : j+1+length])
            
            # 4. 指针跳到下一个字符串的开头
            i = j + 1 + length
            
        return strs