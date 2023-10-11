"""Given an array arr[] of size N, check if it can be partitioned into two parts such that the sum of elements in both parts is the same.

Example 1:

Input: N = 4
arr = {1, 5, 11, 5}
Output: YES
Explanation:
The two parts are {1, 5, 5} and {11}.
Example 2:

Input: N = 3
arr = {1, 3, 5}
Output: NO
Explanation: This array can never be
partitioned into two such parts.
Your Task:
You do not need to read input or print anything. Your task is to complete the function equalPartition() which takes the value N and the array as input parameters and returns 1 if the partition is possible. Otherwise, returns 0.

Expected Time Complexity: O(N*sum of elements)
Expected Auxiliary Space: O(N*sum of elements)

Constraints:
1 ≤ N ≤ 100
1 ≤ arr[i] ≤ 1000
N*sum of elements ≤ 5*106"""

class Solution:
    def equalPartition(self, N, arr):
        total_sum = sum(arr)

        # If the total sum is odd, it cannot be divided into two equal parts
        if total_sum % 2 != 0:
            return False

        target_sum = total_sum // 2

        # Initialize a 2D DP table to store the results of subproblems
        dp = [[False for _ in range(target_sum + 1)] for _ in range(N + 1)]

        # Base case: If target sum is 0, it is always possible to form an empty subset
        for i in range(N + 1):
            dp[i][0] = True

        # Fill the DP table using a bottom-up approach
        for i in range(1, N + 1):
            for j in range(1, target_sum + 1):
                if arr[i - 1] <= j:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]

        # Return whether it is possible to partition the array into two equal sum parts
        return dp[N][target_sum]


# Example usage
solution = Solution()
N = 4
arr = [1, 5, 11, 5]
print(solution.equalPartition(N, arr))  # Output: True
