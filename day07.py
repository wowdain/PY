# Lambda function (before)


import random

def process(no_lists, f):
    """
    리스트와 함수를 받아 리스트의 원소들을 받은 함수에 모두 적용
    :param no_lists: 리스트
    :param f: 함수
    :return: void
    """
    for no in no_lists:
        print(f(no))


def squares(n):
    """
    제곱 함수
    :param n: integer
    :return: integer * integer
    """
    return n * n


numbers = [random.randint(1, 10) for i in range(5)]
print(numbers)
process(numbers, squares)