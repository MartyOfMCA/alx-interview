#!/usr/bin/python3
"""
Define a module for parsing a log.
"""
from sys import stdin
from signal import signal, SIGINT, SIG_IGN

total_size = 0
methods = set()
metrics = {}


def signal_handler(signum, frame):
    """
    Print metrics when Ctrl + C signal is
    raised.
    """
    print_metrics()


def process_input():
    """
    Accept user input from stdin to compute
    metrics from user input.
    """
    global total_size
    counter, method_metric = 0, 0
    tokens = []

    for line in stdin:
        counter += 1
        tokens = _tokenize(line)

        if (not check_tokens(tokens)):
            continue

        total_size += int(tokens[8])
        compute_metric(tokens, methods, metrics)

        if (counter % 10 == 0):
            print_metrics()

    print_metrics()


def print_metrics():
    """
    Print metrics for user input.
    """
    print(f"File size: {total_size}")
    [print(f"{method}: {metrics[method]}") for method in sorted(methods)]


def compute_metric(tokens, methods, metrics):
    """
    Compuete the metrics for the given line
    from user input.

    Parameters:
        tokens : list
        A list containing the tokens extracted
        from a line from the users input.

        methods : set
        A set containing all the methods found
        in user input.

        metrics : dictionary
        A dictionary containing the methods found
        along with their count.
    """
    method_metric = 0

    method = int(tokens[7])
    method_metric = metrics.get(method)
    method_metric = 0 if not method_metric else method_metric
    methods.add(method)
    metrics[method] = method_metric + 1


def _tokenize(input):
    """
    Retrieves tokens from the given input.

    Parameters:
        input : string
        The string entered by the user.

    Returns:
        A list containing all the tokens
        found in the given string.
    """
    return (input.split())


def check_tokens(tokens):
    """
    Check the input provided by the user
    to ensure it matches the required
    format. The tokens are inspected.
    Valid line from user input contains
    exactly 9 tokens.

    Parameters:
        tokens : list
        A list containing the tokens extracted
        from a line from the users input.

    Returns:
        A flag indicating whether the
        user input matches the required
        format.
    """
    return (1 if len(tokens) == 9 else 0)


if (__name__ == "__main__"):
    signal(SIGINT, signal_handler)
    process_input()
