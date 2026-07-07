class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
        anagrams = defaultdict(list)
    
        for word in strs:
            # Sort characters and use as key
            sorted_key = ''.join(sorted(word))
            anagrams[sorted_key].append(word)
        
        return list(anagrams.values())