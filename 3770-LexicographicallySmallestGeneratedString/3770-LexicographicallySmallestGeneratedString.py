# Last updated: 7/21/2026, 7:07:00 PM
class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        total_len = n + m - 1
        res = [None] * total_len
        locked = [False] * total_len
        
        # Phase 1: Fill 'T' constraints
        for i in range(n):
            if str1[i] == 'T':
                for j in range(m):
                    if res[i + j] is not None and res[i + j] != str2[j]:
                        return ""
                    res[i + j] = str2[j]
                    locked[i + j] = True
        
        # Phase 2: Fill gaps with 'a'
        for i in range(total_len):
            if res[i] is None:
                res[i] = 'a'
        
        # Phase 3: Fix 'F' constraints
        for i in range(n):
            if str1[i] == 'F':
                # Check if it currently matches str2
                match = True
                for j in range(m):
                    if res[i + j] != str2[j]:
                        match = False
                        break
                
                if match:
                    # Must break the match. Try changing the rightmost unlocked char.
                    fixed = False
                    for j in range(m - 1, -1, -1):
                        if not locked[i + j]:
                            # Change to the smallest char that isn't str2[j]
                            for char_code in range(ord('a'), ord('z') + 1):
                                if chr(char_code) != str2[j]:
                                    res[i + j] = chr(char_code)
                                    break
                            fixed = True
                            break
                    if not fixed:
                        return ""
        
        # Final Verification: Breaking one 'F' might have accidentally created another 'F' match or corrupted a 'T'
        # (Though with rightmost greedy, 'T' is safe because of 'locked' array)
        for i in range(n):
            current_sub = "".join(res[i:i+m])
            if str1[i] == 'T' and current_sub != str2: return ""
            if str1[i] == 'F' and current_sub == str2: return ""

        return "".join(res)