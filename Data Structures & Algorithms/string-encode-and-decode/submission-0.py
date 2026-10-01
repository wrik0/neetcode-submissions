class Solution:

    delimiter = ":"
    def encode(self, strs: List[str]) -> str:
        master = ""
        for s in strs:
            strlen = len(s)
            meta = str(strlen) + self.delimiter 
            master += meta + s
        return master
        

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            delim_pos = s.find(self.delimiter, i)
            strlen = int(s[i:delim_pos])
            start = delim_pos + 1
            end = start + strlen
            res.append(s[start:end])
            i = end
        return res
