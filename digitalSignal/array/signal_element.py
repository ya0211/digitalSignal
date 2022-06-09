class SignalElement(list):
    def __init__(self, *args):
        list.__init__([])
        if len(args) == 1:
            args = [i for i in args[0]]
            self.extend(args)
        else:
            self.extend([])

    def max(self):
        return max(self)

    def min(self):
        return min(self)
