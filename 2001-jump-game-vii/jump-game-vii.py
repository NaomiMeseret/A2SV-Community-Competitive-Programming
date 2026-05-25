class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == "1":
            return False

        n = len(s)
        dp = [False] * n
        dp[0] = True

        valid_jump_positions = 0

        for i in range(1, n):
            if i > maxJump and dp[i - maxJump - 1]:
                valid_jump_positions -= 1

            if i >= minJump and dp[i - minJump]:
                valid_jump_positions += 1

            if s[i] == "0" and valid_jump_positions > 0:
                dp[i] = True


        return dp[-1]
        