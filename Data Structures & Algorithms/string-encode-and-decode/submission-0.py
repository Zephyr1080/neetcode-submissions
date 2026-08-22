class Solution:
    def encode(self, strs: list[str]) -> str:
        st = ""
        for s in strs:
            st += str(len(s)) + "#" + s
        return st

    def decode(self, s: str) -> list[str]:
        dec_s = []
        i = 0
        n = len(s)
        
        while i < n:
            j = i
            while j < n and s[j] != '#':
                j += 1
            
            length = int(s[i:j])
            
            start = j + 1
            end = start + length
            dec_s.append(s[start:end])
            
            i = end
            
        return dec_s
