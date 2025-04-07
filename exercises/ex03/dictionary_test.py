"""Testing the function skeletons here."""

__author__ = "730734417"

import pytest

from dictionary import invert


def test_invert() -> None:
    assert invert({"a": "z", "b": "y", "c": "x"}) == {"z": "a", "y": "b", "x": "c"}


def test_error_invert() -> None:
    with pytest.raises(KeyError):
        my_dictionary = {"kris": "jordan", "michael": "jordan"}
        invert(my_dictionary)


def test_invert_single() -> None:
    """Inverts a dictionary with one key-value pair."""
    assert invert({"apple": "cat"}) == {"cat": "apple"}


from dictionary import count


def test_count() -> None:
    assert count(
        ["Marathi", "Malayalam", "Hindi", "Hindi", "Korean", "Haitian Creole", "Tamil"]
    ) == {
        "Marathi": 1,
        "Malayalam": 1,
        "Hindi": 2,
        "Korean": 1,
        "Haitian Creole": 1,
        "Tamil": 1,
    }


def test_count_empty() -> None:
    """Returns empty dictionary when input is empty."""
    assert count([]) == {}


def test_count_one_item() -> None:
    """Counts one element correctly."""
    assert count(["a"]) == {"a": 1}


from dictionary import favorite_color


def test_favorite_color() -> None:
    assert (
        favorite_color(
            {
                "Yasin": "Blue",
                "Deven": "Red",
                "Sid": "Purple",
                "Aadhi": "Blue",
                "Heisenberg": "Purple",
            }
        )
        == "Blue"
    )


def test_favorite_color_single() -> None:
    """Handles dictionary with one color."""
    assert favorite_color({"Shinji": "green"}) == "green"


def test_favorite_color_majority() -> None:
    """Returns the most common color."""
    assert (
        favorite_color({"Carmy": "blue", "Sugar": "blue", "Sydney": "green"}) == "blue"
    )


from dictionary import bin_len


def test_bin_len() -> None:
    assert bin_len(["the", "quick", "fox"]) == {3: {"the", "fox"}, 5: {"quick"}}


def test_bin_len_duplicates() -> None:
    """Handles duplicates correctly using sets."""
    result = bin_len(["the", "the", "fox"])
    assert result == {3: {"the", "fox"}}


def test_bin_len_empty() -> None:
    """Handles empty list input."""
    assert bin_len([]) == {}
