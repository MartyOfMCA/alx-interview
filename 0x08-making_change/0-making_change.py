#!/usr/bin/python3
"""
Define a module that defines a method to
determine the minimum possibilities to
obtain a given value.
"""


def makeChange(coins, total):
    """
    Find the minimum number of coins from
    the given list of coins to obtain the
    given total.

    Parameters:
        coins : list
        list of coins available to be
        use in computing the total.

        total : int
        The total amount of change
        obtained.

    Return:
        The minimum number of coins
        needed to obtain the total.
    """
    if (len(coins) == 0):
        return (-1)

    if (total < 1):
        return (0)

    # Make sure the highest coin is always
    # selected first.
    coins.sort(reverse=True)

    # Container to store any coin considered
    # to help obtain our total at a given
    # time.
    bag = []
    change = 0
    # Determine he index of the coin to be
    # added to our change and bag.
    selected_coin_index = 0

    # Add coins into our bag
    while change <= total:
        # Fetch the next bigger coin.
        coin = coins[selected_coin_index]

        # Keep the coin we greedily picked
        # in our bag.
        bag.append(coin)
        change += coin

        # Remove the previously added
        # coin should the change exceed
        # what we need at any given time.
        if (change > total):
            change -= coin
            del bag[len(bag) - 1]

            # Move to the next possible coin.
            selected_coin_index += 1
            if (selected_coin_index >= len(coins)):
                return (-1)

        if (change == total):
            break

    return (len(bag))
