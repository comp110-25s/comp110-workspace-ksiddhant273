"""Exercise for practice with dictionary functions."""

__author__ = "730734417"


def invert(x: dict[str, str]) -> dict[str, str]:
    inverted_x = {}
    for key, value in x.items():
        if value in inverted_x:
            raise KeyError(f"Duplicate value found: {value}")
        inverted_x[value] = key
    return inverted_x


def count(a: list[str]) -> dict[str, int]:
    new_dict: dict[str, int] = {}
    i = 0
    while i < len(a):
        if a[i] in new_dict:
            new_dict[a[i]] += 1
        else:
            new_dict[a[i]] = 1
        i += 1
    return new_dict


def favorite_color(x: dict[str, str]) -> str:
    color_count = count(list(x.values()))

    most_frequent_color = ""
    max_count = 0

    for color in x.values():
        count_value = color_count[color]
        if count_value > max_count:
            most_frequent_color = color
            max_count = count_value

    return most_frequent_color


def bin_len(string: list[str]) -> dict[int, set[str]]:
    len_dict: dict[int, set[str]] = {}  #
    for value in string:
        length = len(value)
        if length not in len_dict:
            len_dict[length] = set()
        len_dict[length].add(value)
    return len_dict
