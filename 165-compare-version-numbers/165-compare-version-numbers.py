class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        l1 = version1.split(".")
        l2 = version2.split(".")
        
        for i in range(max(len(l1), len(l2))):
            x, y = 0,0
            if i < len(l1):
                x = int(l1[i])
            if i < len(l2):
                y = int(l2[i])
                
            if x > y:
                 return 1
            
            if x < y:
                return -1
            
        return 0