class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res, c = [], '0'
        i, j = len(a) - 1, len(b) - 1
        while i >= 0 or j >= 0 or c == '1':
            if i >= 0:
                ai = a[i]
            else:
                ai = '0'
            
            if j >= 0:
                bj = b[j]
            else:
                bj = '0'
                
            if ai == bj:
                res.append(c)
                c = ai
            else:
                if c == '1':
                    res.append('0')
                else:
                    res.append('1')
                
            i, j = i-1, j-1
            
        return ''.join(res[::-1])