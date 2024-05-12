class Square:
    def __init__(self, length):
        self._length = length

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        if value > 0:
            self._length = value
        else:
            raise ValueError("Length must be positive")

    @length.deleter
    def length(self):
        print('deleting ...')
        del self._length

# #####
