import json


class RssTime:
    file = 'data.json'
    def __init__(self):
        with open(self.file) as json_file:
            self.data = json.load(json_file)

    def get_time(self, link):
        return self.data[link]