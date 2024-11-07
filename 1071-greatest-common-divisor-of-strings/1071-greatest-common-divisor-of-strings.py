class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        gcd_len = math.gcd(len(str1), len(str2))

        gcd_str = str1[:gcd_len]

        if str1 == gcd_str * (len(str1) // gcd_len) and str2 == gcd_str * (len(str2) // gcd_len):
            return gcd_str
        return ""