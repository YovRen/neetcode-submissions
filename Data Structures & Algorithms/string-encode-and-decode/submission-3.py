class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "#.#"
        strs = [s if s!="" else "#!#" for s in strs]
        return "#.#".join(strs)
    def decode(self, s: str) -> List[str]:
        if s == "#.#":
            return []
        strs =  s.split("#.#")
        strs = [s if s!="#!#" else "" for s in strs ]
        return strs
