"""Utils module"""

DELIMITER = "-" * 100
ROUND_NDIGITS = 4


def print_dataset_info(
    dataset_name,
    dataset,
    search_pattern,
    time_kmp_search,
    time_rabin_karp_search,
    time_boyer_moore_search,
):
    print(f"\nНабір дадних {dataset_name}:")
    print(DELIMITER)
    print(f"Кількість символів: {len(dataset)}")
    print(f"Шаблон пошуку: <{search_pattern}>")
    print(f"Час на пошук Кнута-Морріса-Пратта: {time_kmp_search}")
    print(f"Час на пошук Рабіна-Карпа: {time_rabin_karp_search}")
    print(f"Час на пошук Боєра-Мура: {time_boyer_moore_search}")

    print(
        f"\nСпіввідношення: Кнута-Морріса-Пратта \ Рабіна-Карпа \ Боєра-Мура = {round(time_kmp_search / time_boyer_moore_search, ROUND_NDIGITS)} \ {round(time_rabin_karp_search / time_boyer_moore_search, ROUND_NDIGITS)} \ {1}"
    )

    print(DELIMITER + "\n")
