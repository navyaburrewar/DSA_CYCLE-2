def knapsack(weights, values, capacity, n):

    # 1. Base case
    if n == 0 or capacity == 0:
        return 0

    # 2. If current item is too heavy
    if weights[n - 1] > capacity:
        return knapsack(
            weights,
            values,
            capacity,
            n - 1
        )

    # 3. TAKE the current item
    take = values[n - 1] + knapsack(
        weights,
        values,
        capacity - weights[n - 1],
        n - 1
    )

    # 4. SKIP the current item
    skip = knapsack(
        weights,
        values,
        capacity,
        n - 1
    )

    # 5. Choose whichever gives more value
    return max(take, skip)


# -------------------------
# Input
# -------------------------

weights = [2, 3, 4]
values = [4, 5, 7]

capacity = 5

n = len(weights)


# -------------------------
# Call the function
# -------------------------

answer = knapsack(
    weights,
    values,
    capacity,
    n
)

print(answer)