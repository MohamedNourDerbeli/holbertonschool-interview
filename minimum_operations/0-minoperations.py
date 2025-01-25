#!/usr/bin/python3
"""
This script calculates the minimum number of operations required to obtain a number `n` starting from 1,
using three operations: multiplication by 2, multiplication by 3, or adding 1.

Author: Your Name
Date: 2025-01-25
Version: 1.0
"""

import sys

def minOperations(n):
    """
    Calculate the minimum number of operations to obtain `n` starting from 1.

    Args:
        n (int): The target number.

    Returns:
        int: The minimum number of operations to reach `n`.
    """
    # Initialize the dp array to store the minimum operations for each number up to `n`.
    dp = [sys.maxsize] * (n + 1)

    # Base case: 1 requires 0 operations to reach.
    dp[1] = 0

    # Iterate through numbers from 2 to `n`.
    for i in range(2, n + 1):
        # Check if the number can be obtained by multiplying by 2.
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)

        # Check if the number can be obtained by multiplying by 3.
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)

        # Check if the number can be obtained by adding 1.
        dp[i] = min(dp[i], dp[i - 1] + 1)

    # Return the result for `n`.
    return dp[n]
