class RssReader:
    file = "rss.txt"
    @staticmethod
    def read():
        with open(RssReader.file) as urls:
            return [rss.strip() for rss in urls.read().split('\n') if rss]
