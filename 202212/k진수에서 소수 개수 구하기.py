"""
문제 링크:
https://school.programmers.co.kr/learn/courses/30/lessons/92335?language=python3
"""

def _to_k_notation(n, k):
    result = []
    while n > 0:
        quotient, remainder = divmod(n, k)
        result.append(str(remainder))
        n = quotient
    result.reverse()
    return ''.join(result)


def _is_prime_number(k):
    if k in [2, 3]:
        return True
    elif k % 2 == 0 or k < 2:
        return False
    else:
        for i in range(3, int(k ** 0.5) + 1, 2):
            if k % i == 0:
                return False
        return True


def solution(n, k):
    answer = 0
    k_notation = _to_k_notation(n, k)
    for n in k_notation.split('0'):
        if n == "":
            continue
        if _is_prime_number(int(n)):
            answer += 1
    return answer