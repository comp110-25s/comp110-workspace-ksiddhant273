"""Helping to plan a tea party through basic Python concepts"""

__author__ = "730734417"


def main_planner(guests: int) -> None:
    """Calculating the amount of tea bags, treats, and cost thereof based on attendance."""
    print("A cozy tea party for" + str(guests) + "people")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))


def tea_bags(people: int) -> int:
    """Calculating the number of tea bags required based on people present"""
    return people * 2


def treats(people: int) -> int:
    """Calculating the number of treats needed based on people attending"""
    return int(1.5 * tea_bags(people))


def cost(tea_count: int, treat_count: int) -> float:
    """Calculating the cost of bags and treats"""
    return tea_count * 0.50 + treat_count * 0.75
