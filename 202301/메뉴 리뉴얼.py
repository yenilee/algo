from collections import Counter
from itertools import combinations

def solution(orders, course):
    """
    문제 링크:
    https://school.programmers.co.kr/learn/courses/30/lessons/72411
    """

    results = []
    for num in course:
        order_combinations = []
        for order in orders:
            order_combinations += combinations(sorted(order), num)

        most_ordered = Counter(order_combinations).most_common()
        results += [k for k, v in most_ordered if v > 1 and v == most_ordered[0][1]]

    return [''.join(item) for item in sorted(results)]