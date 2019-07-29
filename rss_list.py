class RssList:
    _file = "rss.txt"

    @staticmethod
    def get():
        with open(RssList._file) as urls:
            return [rss.strip() for rss in urls.read().split('\n') if rss]
