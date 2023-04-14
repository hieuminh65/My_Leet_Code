
def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    result = {}
    for s in strs:
        key = ''.join(sorted(s))
        result[key] = result.get(key, []) + [s]
        print(result[key])
    return result.values()


#test
print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
