"""Internal utility functions."""
import colorsys
import functools
import weakref

# from http://stackoverflow.com/questions/4103773/efficient-way-of-having-a-function-only-execute-once-in-a-loop
def once(func):
    """Runs a method (successfully) only once per instance."""

    has_run = weakref.WeakSet()

    name = func.__name__
    name = f'__has_run_{name}_once'

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        first = args[0] if len(args) > 0 else once
        if first not in has_run:
            result = func(*args, **kwargs)
            has_run.add(first)
            return result
        return None

    return wrapper

def network_color_for(network, number_of_networks):
    """Calculates a color on the hue-spectrum for a specific network.

    Parameters
    ----------
    network : int
        The 0-based index of the network.
    number_of_networks : int
        The overall number of networks available.

    Returns
    -------
    r : int
        The red value (0-255).
    g : int
        The green value (0-255).
    b : int
        The blue value (0-255).
    """
    hue = network / number_of_networks + 1
    (r, g, b) = colorsys.hsv_to_rgb(hue, 1, 1) # pylint: disable=invalid-name
    return (int(r * 255), int(g * 255), int(b * 255))

def unique(iterable):
    seen = set()
    for item in iterable:
        if item not in seen:
            seen.add(item)
            yield item

def unique_generator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return unique(func(*args, **kwargs))
    return wrapper
