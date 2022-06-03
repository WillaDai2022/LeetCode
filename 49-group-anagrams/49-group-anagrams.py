class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        container = collections.defaultdict(list)
        
        for str in strs:
            s = "".join(sorted(str))
            
            container[s].append(str)
            
        return list(container.values())
            
            