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

weights = [2, 3, 6]
values = [3, 9, 7]

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



"First, we pass weights, values, capacity and n into the function. "
"Then we check the base condition."
" If there are no items left or no capacity left, we return 0."
" Otherwise, we look at the current item using n - 1 and check whether its weight fits in the current capacity. "
"If it doesn't fit, we have no choice except to skip it and recursively move to the next item."
" If it fits, we have two choices: TAKE or SKIP."
" If we TAKE it, we add its value, reduce the capacity by its weight, and reduce n by 1."
" If we SKIP it, the capacity stays the same and n is reduced by 1. "
"Both choices recursively continue until the base condition. "
"When the recursive calls return, we compare TAKE and SKIP using max() and return the larger value."
" Finally, the first function call receives the maximum possible value."