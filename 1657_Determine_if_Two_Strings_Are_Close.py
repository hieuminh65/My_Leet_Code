class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        map1 = {}
        map2 = {}

        for word in word1:
            map1[word] = map1.get(word, 0) + 1
        for word in word2:
            map2[word] = map2.get(word, 0) + 1

        for k in map1.keys():
            if k not in map2:
                return False

        return sorted(map1.values()) == sorted(map2.values())


s = Solution()
print(s.closeStrings("aaabbbbccddeeeeefffff", "aaaaabbcccdddeeeeffff"))