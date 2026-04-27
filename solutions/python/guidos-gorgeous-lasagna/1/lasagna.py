"""
Functions used in preparing Guido's gorgeous lasagna.
"""

# Constants
EXPECTED_BAKE_TIME = 40  # minutes in oven
PREPARATION_TIME = 2     # minutes per layer


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - minutes already baked
    :return: int - remaining bake time
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """Calculate preparation time.

    :param number_of_layers: int - number of layers
    :return: int - total preparation time
    """
    return number_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate total elapsed cooking time.

    :param number_of_layers: int
    :param elapsed_bake_time: int
    :return: int - total time spent
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time