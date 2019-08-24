import json
import logging


class RssConfigIO:
    _file = "rss_configuration.json"

    def read(self):
        try:
            with open(self._file) as f:
                return json.load(f)
        except OSError as e:
            logging.warning("New config file on read: %s" % e)
            return {}

    def add(self, my_dict):
        data = self.read()
        data.update(my_dict)
        self.write(data)

    def write(self, data):
        with open(self._file, 'w') as f:
            json.dump(data, f)
