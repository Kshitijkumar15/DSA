def max_step(N, K):
    total_steps = 0

    for i in range(1, N + 1):
        total_steps += i
        if total_steps == K:
            total_steps -= i

    return total_steps

# Example usage:
N = int(input("Enter the value of N: "))
K = int(input("Enter the value of K: "))
result = max_step(N, K)
print("The topmost step that can be reached by Jack is:", result)
