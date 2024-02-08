#!/usr/bin/python3
"""
N queens challenge
"""
import sys


def solve(n):
    if not n.isdigit():
        print("N must be a number")
        exit(1)
    n = int(n)
    if n < 4:
        print("N must be at least 4")
        exit(1)

    state = []
    solutions = []
    search(state, solutions, n)
    # print(solutions)
    format_output(solutions)


def format_output(solutions):
    for ways in solutions:
        output = []
        for row, col in enumerate(ways):
            output.append([row, col])
        print(output)


def search(state, solutions, n):
    if is_valid_state(state, n):
        solutions.append(state.copy())
        # print(solutions)
        return

    for value in get_state_value(state, n):
        state.append(value)
        search(state, solutions, n)
        state.pop()


def is_valid_state(state, n):
    return len(state) == n


def get_state_value(state, n):
    if not state:
        return range(n)

    values = set(range(n))
    total_col = len(state)
    for row, col in enumerate(state):
        values.discard(col)
        check_diagonal = total_col - row
        values.discard(col + check_diagonal)
        values.discard(col - check_diagonal)
    return values


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
    solve(sys.argv[1])
