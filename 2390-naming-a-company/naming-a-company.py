class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        groups = defaultdict(set)
        
        # Group suffixes by first letter
        for idea in ideas:
            groups[idea[0]].add(idea[1:])
        
        result = 0
        letters = list(groups.keys())
        
        # Compare each pair of starting letters
        for i in range(len(letters)):
            for j in range(i+1, len(letters)):
                set1, set2 = groups[letters[i]], groups[letters[j]]
                # Count unique suffixes
                common = len(set1 & set2)
                unique1 = len(set1) - common
                unique2 = len(set2) - common
                result += unique1 * unique2 * 2
        
        return result