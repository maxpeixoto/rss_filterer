import urllib.request
from threading import Thread

class LinkFilterer:
    def __init__(self, keywords):
        self.keywords = keywords

    def filter_links(self, links):
        return list(filter(self._has_keyword, links))

    def _has_keyword(self, link):
        page = str(urllib.request.urlopen(link, timeout=20).read())
        return any(word in page for word in self.keywords)

    def _filter_link_thread(self, link, filtered_list):
        if self._has_keyword(link):
            filtered_list.append(link)

    def filter_links_parallel(self, links):
        filtered = []
        thread_list = []
        for link in links:
            t = Thread(target=self._filter_link_thread, args=(link, filtered))
            t.start()
            thread_list.append(t)
        [thread.join() for thread in thread_list]
        return filtered
