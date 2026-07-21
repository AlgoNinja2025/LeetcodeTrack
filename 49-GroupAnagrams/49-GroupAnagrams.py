# Last updated: 7/21/2026, 7:10:11 PM
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hmap = collections.defaultdict(list)
        for st in strs:
            array = [0] * 26
            for l in st:
                array[ord(l)-ord('a')] += 1
            hmap[tuple(array)].append(st)
        return hmap.values()