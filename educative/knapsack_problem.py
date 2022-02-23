

def solve_knapsack(profits, weights, capacity):
    return knapsack_recursive(profits, weights, capacity, 0)



def knapsack_recursive(profits, weights, capacity, current_index):

    if capacity <= 0 or current_index >= len(profits):
        return 0



    profits1 = 0
    profits3 = 0
    if weights[current_index] <= capacity:
        profits1 += profits[current_index] + knapsack_recursive(profits, weights, capacity - weights[current_index], current_index + 1)
        profits3 += profits[current_index] + knapsack_recursive(
            profits, weights, capacity - weights[current_index], current_index )


    profits2 = knapsack_recursive(profits, weights, capacity, current_index + 1)


    return max(profits1, profits2, profits3)















print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 2], 7))