def add_nums(*args, **kwargs):
    val = list((x for x in kwargs.values()))
    total = reduce(lambda x, y: x + y, args)
    return total + int(reduce(lambda x, y: x+y, val))


add_nums(2, 3, 5, 8)