from threading import Thread

from filter_keyword import FilterKeyword
from filter_never_sent import FilterNeverSent
from rss_configuration import RssConfiguration


class PageFilterer:
    def __init__(self, rss):
        self._rss = rss
        config = RssConfiguration(rss)
        self._filters = [
            FilterNeverSent(config),
            FilterKeyword()
        ]

    def _filter_page_thread(self, page, filtered_list):
        for f in self._filters:
            if not f.filter(page):
                return
        filtered_list.append(page)
        pass

    def filter_pages_parallel(self, pages):
        filtered = []
        thread_list = []
        for page in pages:
            t = Thread(target=self._filter_page_thread, args=(page, filtered))
            t.start()
            thread_list.append(t)
        [thread.join() for thread in thread_list]
        return filtered
