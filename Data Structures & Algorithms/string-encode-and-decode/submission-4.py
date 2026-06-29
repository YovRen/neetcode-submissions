class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for str_ in strs:
            s+=f"{len(str_)}#{str_}"
        return s

    def decode(self, s: str) -> List[str]:
        strs = []
        while len(s)>0:
            pos = s.index("#")
            len_ = eval(s[:pos])
            str_ = s[pos+1:pos+1+len_]
            strs.append(str_)
            s = s[pos+1+len_:]
        return strs
