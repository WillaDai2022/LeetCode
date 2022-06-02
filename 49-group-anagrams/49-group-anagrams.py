class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        container = collections.defaultdict(list)
        
        for str in strs:
            chars = [0]*26
            for c in str:
                chars[ord(c) - ord("a")] += 1
            
            container[tuple(chars)].append(str)
            
        return list(container.values())