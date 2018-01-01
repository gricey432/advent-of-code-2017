"""
Some common classes and functions to reduce duplication
"""


class CircularList(list):
    """
    Lets a list loop back on itself
    Doesn't support some slice stuff like [5:], where it wouldn't make sense on an 'infinite' list
    """
    def __getslice__(self, i, j):
        # Py2 compat
        return self.__getitem__(slice(i, j))

    def __getitem__(self, key):
        size = self.__len__()
        if isinstance(key, int):
            key %= size
        elif isinstance(key, slice):
            # Forgive this code, wow
            return [self.__getitem__(i) for i in range(key.start or 0, key.stop, key.step or 1)]
        return super(CircularList, self).__getitem__(key)

    def __setitem__(self, key, o):
        size = self.__len__()
        if isinstance(key, int):
            key %= size
        elif isinstance(key, slice):
            # Forgive this code, wow
            for oi, i in zip(o, range(key.start or 0, key.stop, key.step or 1)):
                self.__setitem__(i, oi)
            return
        return super(CircularList, self).__setitem__(key, o)
