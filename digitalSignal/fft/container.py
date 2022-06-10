class Container(object):
    def __init__(self, **kwargs):
        [setattr(self, key, kwargs.get(key)) for key in kwargs.keys()]

    def args(self):
        return self
