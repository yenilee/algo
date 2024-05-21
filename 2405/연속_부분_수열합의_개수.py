def solution(elements):
    result = set(elements)

    for length in range(2, len(elements)):
        list_sum = sum(elements[:length])
        start_idx = 0
        last_idx = length - 1

        while start_idx < len(elements):
            result.add(list_sum)
            last_idx += 1

            if last_idx == len(elements):
                last_idx = 0
            list_sum = list_sum - elements[start_idx] + elements[last_idx]
            start_idx += 1

    result.add(sum(elements))
    return len(result)


print(solution([7, 9, 1, 1, 4]))
