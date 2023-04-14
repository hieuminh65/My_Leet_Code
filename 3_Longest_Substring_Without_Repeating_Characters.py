# Given a string s, find the length of the longest substring without repeating characters


def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    e_set = set()
    max_len = 0
    l=0
    for r in range(len(s)):
        while s[r] in e_set:
            e_set.remove(s[l])
            l+=1
        e_set.add(s[r])
        max_len= max(max_len, r-l+1)
    return max_len
if __name__ == '__main__':
    s = "pwwkew"
    print(lengthOfLongestSubstring(s))  # 3




 

