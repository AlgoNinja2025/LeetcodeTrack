# Last updated: 7/21/2026, 7:08:57 PM
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()  # Sort the folders lexicographically
        res = []

        for dir in folder:
            if not res or not dir.startswith(res[-1] + '/'):
                res.append(dir)

        return res
        