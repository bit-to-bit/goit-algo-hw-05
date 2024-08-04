"""TASK 2 binary_search"""


def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    iterations = 0

    while low <= high:
        iterations += 1
        mid = (high + low) // 2

        # якщо x менше або дорівню значенню посередині списку, ігноруємо праву половину
        if arr[mid] >= x:
            high = mid

        # якщо x більше значення посередині списку, ігноруємо ліву половину
        elif arr[mid] < x:
            low = mid + 1

        if low == mid:
            return (iterations, arr[mid])

    # якщо елемент не знайдений
    return (iterations, None)
