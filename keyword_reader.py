class KeywordReader:
    _file = "keywords.txt"
    @staticmethod
    def read():
        with open(KeywordReader._file) as keywords:
            return [word.strip() for word in keywords.read().split('\n') if word]
