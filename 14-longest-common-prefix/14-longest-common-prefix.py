class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = strs[0]
        
        for str in strs:
            while str.find(prefix) != 0:
                prefix = prefix[:len(prefix) - 1]
                
        return prefix