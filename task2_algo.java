public class task2_algo
{
    public static void main(String[] args)
    {
        int[] weights = {8, 7, 6, 5, 4}; // these are the weights of luggage of each experience ID
        int[] values = {1500, 1600, 1700, 1800, 3000}; // these are enjoyment points each ID has
        int W = 20; // maximum luggage limit allowed
        int res = solvedp(weights, values, W); // sending value to function dp table
        System.out.println("Maximum enjoyment points: " + res); // printing enjoyment points
    }

    public static int solvedp(int[] weights, int[] values, int W)
    {
        int n = weights.length; // number of user IDs calculated
        int[][] dp = new int[n + 1][W + 1];

        // dp table begins to fill
        for (int i = 1; i <= n; i++)
        {
            for (int w = 0; w <= W; w++)
            {
                // checks for weight units to be less than the max(20)
                if (weights[i - 1] <= w)
                {
                    dp[i][w] = Math.max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1]);
                }
                else
                {
                    dp[i][w] = dp[i - 1][w];
                }
            }
        }
        return dp[n][W];
    }
}