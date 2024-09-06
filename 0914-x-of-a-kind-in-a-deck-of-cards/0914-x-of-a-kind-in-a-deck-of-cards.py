class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = Counter(deck)
        freqs = list(count.values())
        
        gcd_all = reduce(gcd, freqs)
        
        return gcd_all > 1