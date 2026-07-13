class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dic = {}
        for c in s1:
            if c in dic:
                dic[c] += 1
            else:
                dic[c] = 1
                
        found = False
        copied = dic.copy()
        

        
        l = 0
        r = len(s1) - 1
        
        while (not found) and r < len(s2):
            checked = 0
            checker = True
            x = r
            
            while x >= l and checker:
                
                if s2[x] in dic:
                    if dic[s2[x]] != 0:
                        dic[s2[x]] -= 1
                        x-=1
                        checked += 1
                    else:
                        l = x + 1
                        r = l + len(s1) - 1
                        checker = False
                        dic = copied.copy()
                        
                else:
                    l = x + 1
                    r = l + len(s1) - 1
                    checker = False
                    dic = copied.copy()
                
            if checked == len(s1):
                found = True
            
                
        return found
        

        