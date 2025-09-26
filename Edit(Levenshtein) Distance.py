class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)
        # word1 along columns, word2 along rows
        dp = [[0 for _ in range(n1 + 1)] for _ in range(n2 + 1)]

        # first row: convert "" (word2 prefix) into word1 prefix → insertions
        for j in range(1, n1 + 1):
            dp[0][j] = j

        # first col: convert word2 prefix into "" → deletions
        for i in range(1, n2 + 1):
            dp[i][0] = i

        # fill DP
        for i in range(1, n2 + 1):  # word2 chars (rows)
            for j in range(1, n1 + 1):  # word1 chars (cols)
                if word2[i - 1] == word1[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]  # match → no cost
                else:
                    dp[i][j] = 1 + min(
                        dp[i - 1][j],     # delete from word2
                        dp[i][j - 1],     # insert into word2
                        dp[i - 1][j - 1]  # replace
                    )

        return dp[n2][n1]
