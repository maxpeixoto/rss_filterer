import feedparser


class RssParser:
    @staticmethod
    def _filter_rss(rss_link):
        return rss_link.entries

    @staticmethod
    def _get_rss_links(rss):
        parsed_rss = feedparser.parse(rss)
        return [i.link for i in RssParser._filter_rss(parsed_rss)]

    @staticmethod
    def get_links(rss_list):
        links = []
        for rss in rss_list:
            links.extend(RssParser._get_rss_links(rss))
        return links
