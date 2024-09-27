from typing import Generator


def generate_sequence(n: int) -> Generator[int, None, None]:
    """
    Генерирует последовательность, в которой число повторяется столько раз, чему оно равно.
    Args:
        n (int): Количество элементов последовательности, которые необходимо вывести.
    Returns:
        generator: Генератор, возвращающий заданную последовательность чисел.
    """

    item_count = 0
    num = 1
    while True:
        for _ in range(num):
            if item_count >= n:
                return
            yield num
            item_count += 1
        num += 1


if __name__ == "__main__":
    gen = generate_sequence(10)
    print(*gen, sep="")
