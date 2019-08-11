from threading import Thread

from filter_keyword import FilterKeyword


# from filter_timestamp import FilterTimestamp


class PageFilterer:
    def __init__(self, pages):
        self._pages = pages
        self._filters = [
            # FilterRepeated(), # TODO descomentar
            FilterKeyword()
        ]

    def _filter_page_thread(self, page, filtered_list):
        for f in self._filters:
            if not f.filter(page):
                return
        filtered_list.append(page)

    def filter_pages_parallel(self):
        filtered = []
        thread_list = []
        for page in self._pages:
            t = Thread(target=self._filter_page_thread, args=(page, filtered))
            t.start()
            thread_list.append(t)
        [thread.join() for thread in thread_list]
        return filtered
