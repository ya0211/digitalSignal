class SignalIndex(list):
    def __init__(self, *args):
        list.__init__([])
        if len(args) == 1:
            args = [i for i in args[0]]
            self.extend(args)
        else:
            self.extend([])

    def start(self):
        if len(self) == 0:
            return None
        else:
            return self[0]

    def stop(self):
        if len(self) == 0:
            return None
        else:
            return self[-1]

    def range(self):
        if self.start() == self.stop():
            return self.start()
        else:
            return range(self.start(), self.stop()+1)
