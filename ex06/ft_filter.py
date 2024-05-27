def ft_filter(function, iterable):
    """
    Filters elements from the iterable for which the function returns True.

    Parameters:
    function (callable or None): A function to apply to each element
    of the iterable.If None, it will filter out elements that are false in
    a boolean context.iterable (iterable): An iterable to filter elements from.

    Returns:
    list: A list of elements from the iterable for which the
    function returns True. If function is None, it returns elements that
    are true in a boolean context.
    """

    # If no function is provided, filter out elements
    # that are false in a boolean context.
    if function is None:
        return [item for item in iterable if item]
    # Apply the provided function to filter elements.
    return [item for item in iterable if function(item)]
