class SignalIndex(list):
    def __init__(self, *args):
        list.__init__([])
        if len(args) == 1:
            args = [i for i in args[0]]
            self.extend(args)
        else:
            self.extend([])

    def start(self):
        return self[0]

    def stop(self):
        return self[-1]

    def range(self):
        return range(self.start(), self.stop()+1)


class SignalElement(list):
    def __init__(self, *args):
        list.__init__([])
        if len(args) == 1:
            args = [i for i in args[0]]
            self.extend(args)
        else:
            self.extend([])

