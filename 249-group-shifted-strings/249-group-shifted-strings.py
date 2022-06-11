class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        
        dic = collections.defaultdict(list)
        
        for str in strings:
            key = ""
            
            for i in range(len(str)-1):
                key += chr((ord(str[i])-ord(str[i+1])) %26)
            
            dic[key].append(str)
            
        return dic.values()
            