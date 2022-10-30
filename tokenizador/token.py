class Token:
    def __init__(self, begin, end, value, type):
        self.begin = begin
        self.end = end
        self.value = value
        self.type = type

    def __str__(self):
        return self.value + '\t\t' + self.type.name

    __repr__ = __str__
