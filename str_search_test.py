"""Test str search algoritms"""

import timeit
from utils import print_dataset_info
from kmp_search import kmp_search
from rabin_karp_search import rabin_karp_search
from boyer_moore_search import boyer_moore_search

FILE_1 = "storage/стаття 1.txt"
FILE_2 = "storage/стаття 2.txt"
SEARCH_PATTERN_REAL = "даних"
SEARCH_PATTERN_FAKE = "Donald"
TEST_NUMBER = 1000

print("Stage 1 - # Завантажуємо текстові дані")

with open(FILE_1, "r", encoding="utf-8") as file:
    text_1 = file.read()

with open(FILE_2, "r", encoding="utf-8") as file:
    text_2 = file.read()

print("Stage 2 - # Алгоритм пошуку Боєра-Мура")
time_boyer_moore_text_1_real = timeit.timeit(
    lambda: boyer_moore_search(text_1, SEARCH_PATTERN_REAL), number=TEST_NUMBER
)
time_boyer_moore_text_1_fake = timeit.timeit(
    lambda: boyer_moore_search(text_1, SEARCH_PATTERN_FAKE), number=TEST_NUMBER
)
time_boyer_moore_text_2_real = timeit.timeit(
    lambda: boyer_moore_search(text_2, SEARCH_PATTERN_REAL), number=TEST_NUMBER
)
time_boyer_moore_text_2_fake = timeit.timeit(
    lambda: boyer_moore_search(text_2, SEARCH_PATTERN_FAKE), number=TEST_NUMBER
)

print("Stage 3 - # Алгоритм пошуку Кнута-Морріса-Пратта")
time_kmp_text_1_real = timeit.timeit(
    lambda: kmp_search(text_1, SEARCH_PATTERN_REAL), number=TEST_NUMBER
)
time_kmp_text_1_fake = timeit.timeit(
    lambda: kmp_search(text_1, SEARCH_PATTERN_FAKE), number=TEST_NUMBER
)
time_kmp_text_2_real = timeit.timeit(
    lambda: kmp_search(text_2, SEARCH_PATTERN_REAL), number=TEST_NUMBER
)
time_kmp_text_2_fake = timeit.timeit(
    lambda: kmp_search(text_2, SEARCH_PATTERN_FAKE), number=TEST_NUMBER
)

print("Stage 4 - # Алгоритм пошуку Рабіна-Карпа")
time_rabin_karp_text_1_real = timeit.timeit(
    lambda: rabin_karp_search(text_1, SEARCH_PATTERN_REAL), number=TEST_NUMBER
)
time_rabin_karp_text_1_fake = timeit.timeit(
    lambda: rabin_karp_search(text_1, SEARCH_PATTERN_FAKE), number=TEST_NUMBER
)
time_rabin_karp_text_2_real = timeit.timeit(
    lambda: rabin_karp_search(text_2, SEARCH_PATTERN_REAL), number=TEST_NUMBER
)
time_rabin_karp_text_2_fake = timeit.timeit(
    lambda: rabin_karp_search(text_2, SEARCH_PATTERN_FAKE), number=TEST_NUMBER
)


print("Stage 5 - # Оцінка алгоритмів")

print_dataset_info(
    "text_1_real",
    text_1,
    SEARCH_PATTERN_REAL,
    time_kmp_text_1_real,
    time_rabin_karp_text_1_real,
    time_boyer_moore_text_1_real,
)

print_dataset_info(
    "text_1_fake",
    text_1,
    SEARCH_PATTERN_FAKE,
    time_kmp_text_1_fake,
    time_rabin_karp_text_1_fake,
    time_boyer_moore_text_1_fake,
)

print_dataset_info(
    "text_2_real",
    text_2,
    SEARCH_PATTERN_REAL,
    time_kmp_text_2_real,
    time_rabin_karp_text_2_real,
    time_boyer_moore_text_2_real,
)

print_dataset_info(
    "text_2_fake",
    text_2,
    SEARCH_PATTERN_FAKE,
    time_kmp_text_2_fake,
    time_rabin_karp_text_2_fake,
    time_boyer_moore_text_2_fake,
)

print_dataset_info(
    "в середньому по чотирьом варіантам пошуку",
    "",
    "",
    (
        time_kmp_text_1_real
        + time_kmp_text_1_fake
        + time_kmp_text_2_real
        + time_kmp_text_2_fake
    )
    / 4,
    (
        time_rabin_karp_text_1_real
        + time_rabin_karp_text_1_fake
        + time_rabin_karp_text_2_real
        + time_rabin_karp_text_2_fake
    )
    / 4,
    (
        time_boyer_moore_text_1_real
        + time_boyer_moore_text_1_fake
        + time_boyer_moore_text_2_real
        + time_boyer_moore_text_2_fake
    )
    / 4,
)
