def friend_circles(friends):
    def dfs(i, visited, friends):
        visited[i] = True
        for j in range(len(friends)):
            if friends[i][j] == 'Y' and not visited[j]:
                dfs(j, visited, friends)

    n = len(friends)
    visited = [False] * n
    circles = 0

    for i in range(n):
        if not visited[i]:
            dfs(i, visited, friends)
            circles += 1

    return circles

# Input reading and processing
friends_input = [
    "YYNN",
    "NYYN",
    "NNYN",
]

# Convert input to a 2D list
friends_matrix = [list(row) for row in friends_input]

# Output the result
result = friend_circles(friends_matrix)
print("The total number of friend circles in the class is:", result)
