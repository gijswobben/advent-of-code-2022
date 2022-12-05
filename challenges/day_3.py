# https://adventofcode.com/2022/day/3

import functools
import string
from pathlib import Path

TEST_INPUT: list[str] = [
    "vJrwpWtwJgWrhcsFMMfFFhFp",
    "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
    "PmmdzqPrVvPwwTWBwg",
    "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
    "ttgJtRGJQctTZtZT",
    "CrZsJsPPZsGzwwsLwLmpwMDw",
]

SCORE: dict[str, int] = {
    character: index + 1
    for index, character in enumerate(string.ascii_lowercase + string.ascii_uppercase)
}


def test_part_one():
    """Test based on the example provided in the challenge."""

    result = part_one(TEST_INPUT)
    assert result == 157


def test_part_two():
    """Test based on the example provided in the challenge."""

    result = part_two(TEST_INPUT)
    assert result == 70


def part_one(input_lines: list[str]) -> int:

    # Loop over the lines
    score = 0
    for line in input_lines:

        # Determine the midpoint for this line
        midpoint = len(line) // 2

        # Find the common character in the characters before and after
        # the midpoint
        common = list(set(line[:midpoint]) & set(line[midpoint:]))

        # Lookup the score for the common character
        score += SCORE[common[0]]

    return score


def part_two(input_lines: list[str]) -> int:

    # Loop groups of 3 lines
    score = 0
    group_size = 3
    groups = zip(*(iter(input_lines),) * group_size)
    for group in groups:

        # Determine the common character in the lines of this group
        common = list(
            functools.reduce(
                lambda a, b: a.intersection(b),  # type: ignore
                [set(element) for element in group],
            )
        )

        # Lookup the score for the common character
        score += SCORE[common[0]]

    return score


if __name__ == "__main__":

    # Read the input
    with open(Path(__file__).parents[1] / "data/day_3.txt", "r") as f:
        input_lines = [line.strip() for line in f.readlines()]

    # Determine the output for part one
    result = part_one(input_lines)
    print("Part one:", result)

    # Determine the output for part two
    result = part_two(input_lines)
    print("Part two:", result)
