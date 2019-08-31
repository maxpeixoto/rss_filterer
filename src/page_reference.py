class PageReference:
    def __init__(self, dictionary):
        for key in dictionary:
            setattr(self, key, dictionary[key])

    def add(self, key, value):
        setattr(self, key, value)
