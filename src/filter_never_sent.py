from src.page_filter import PageFilter


class FilterNeverSent(PageFilter):

    def __init__(self, config):
        self._config = config
        self._threshold = config.get_timestamp()
        self._last = self._threshold

    def filter(self, page):
        time = list(page.published_parsed)
        self._config.set_timestamp(time)
        return time > self._threshold
