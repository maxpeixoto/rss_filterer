from time import gmtime

from rss_config_io import RssConfigIO


class RssConfiguration:
    _timestamp_field = "timestamp"
    _future_config = None
    _config = None

    def __init__(self, rss):
        self._rss = rss
        config = RssConfigIO().read()
        self._config = config.get(rss, self._get_default())
        self._future_config = dict(self._config)

    def __del__(self):
        RssConfigIO().add({self._rss: self._future_config})

    def _get_default(self):
        return {
            self._timestamp_field: list(gmtime(1))
        }

    def get_timestamp(self):
        return self._config[self._timestamp_field]

    def set_timestamp(self, timestamp):
        if timestamp > self.get_timestamp():
            self._future_config[self._timestamp_field] = timestamp
