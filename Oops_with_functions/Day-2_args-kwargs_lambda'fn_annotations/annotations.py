# Python Annotations are a Python feature that tells developers the data type of variables or function parameters.


# def sum_of(n1: int, n2: int, n3: int) -> int:  # int are here annotations
#     print(n1 + n2 + n3)


# sum_of(1, 2, 30)  # output-->33


def sum_of(l: list[int] = []) -> float:
    print(f"List is : {l}")
    print(f"Sum of list is : {sum(l)}")


sum_of([1, 2.2, 3])
