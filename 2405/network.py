def solution(n, computers):
    visited = [0] * n
    answer = 0

    for computer in range(n):
        if visited[computer]:
            continue

        stack = [computer]

        while stack:
            current_node = stack.pop()
            if visited[current_node]:
                continue

            visited[current_node] = 1
            for node_idx, is_connected in enumerate(computers[current_node]):
                if current_node == node_idx:
                    continue
                if is_connected:
                    stack.append(node_idx)

        answer += 1
    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
