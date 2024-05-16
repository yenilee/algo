from icecream import ic


def solution(sequence, k):
    end = 0
    range_sum = 0
    answer = []
    answer_length = len(sequence)

    for start in range(len(sequence)):
        while range_sum < k and end < len(sequence):
            range_sum += sequence[end]
            end += 1

        last_index = end - 1
        if range_sum == k and (last_index - start) < answer_length:
            answer = [start, last_index]
            answer_length = last_index - start
        range_sum -= sequence[start]
    return answer

def failed_solution(sequence, k):
    answer = []

#     start = 0
#     end = 0
#     seq_sum = 0
#
#     while start < len(sequence) and end < len(sequence):
#         if seq_sum == k:
#             if not answer:
#                 answer = [start, end]
#             else:
#                 if answer[1] - answer[0] > end-start:
#                     answer = [start, end]
#             seq_sum -= sequence[start]
#             start+=1
#         elif seq_sum < k:
#             seq_sum += sequence[end]
#             end+=1
#         else: # seq_sum > k
#             seq_sum -= sequence[start]
#             start+=1
#
#     answer[1] = answer[1] -1
    return answer



print(solution([1, 2, 3, 4, 5], 7))
print(solution([1, 1, 1, 2, 3, 4, 5], 5	))
print(solution([2, 2, 2, 2, 2], 6))