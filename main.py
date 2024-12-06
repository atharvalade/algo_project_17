def knapsack(weights, values, W):
    n = len(weights)
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    # Build the DP table
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if weights[i - 1] <= w:
                # Max of excluding or including the current item
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
            else:
                dp[i][w] = dp[i - 1][w]
    
    # Reconstruct the solution to find which experiences were selected
    chosen = []
    w = W
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:  # This item was included
            chosen.append(i)
            w -= weights[i - 1]
    
    return dp[n][W], chosen

# Experiences' data
weights = [8, 7, 6, 5, 4]
values = [1500, 1600, 1700, 1800, 3000]
W = 20

max_value, chosen_experiences = knapsack(weights, values, W)
print(f"Maximum Enjoyment Points: {max_value}")
print(f"Chosen Experiences: {chosen_experiences}")
