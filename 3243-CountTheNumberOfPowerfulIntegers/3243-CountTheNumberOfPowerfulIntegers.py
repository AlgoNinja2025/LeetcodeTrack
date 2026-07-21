# Last updated: 7/21/2026, 7:07:40 PM
class Solution:
    def numberOfPowerfulInt(self, start, finish, limit, s):
        suffix = s
        suffix_len = len(suffix)
        suffix_val = int(suffix)
        suffix_div = 10 ** suffix_len

        def adjust_bounds(start, finish):
            if finish < suffix_val:
                return 0, -1
            lower, rem = divmod(start, suffix_div)
            if rem > suffix_val:
                lower += 1
            upper, rem = divmod(finish, suffix_div)
            if rem < suffix_val:
                upper -= 1
            return lower, upper

        def count_valid_prefixes(n):
            if n < 0:
                return 0 

            digits = list(map(int, str(n)))
            length = len(digits)
            memo = {}

            def dfs(pos, tight):
                key = (pos, tight)
                if key in memo:
                    return memo[key]
                if pos == length:
                    return 1
                max_digit = digits[pos] if tight else limit
                res = 0
                for d in range(0, min(limit, max_digit) + 1):
                    new_tight = tight and (d == max_digit)
                    res += dfs(pos + 1, new_tight)
                memo[key] = res
                return res

            return dfs(0, True)

        low_prefix, high_prefix = adjust_bounds(start, finish)
        if high_prefix < low_prefix:
            return 0

        return count_valid_prefixes(high_prefix) - count_valid_prefixes(low_prefix - 1)
