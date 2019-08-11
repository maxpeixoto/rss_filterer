from rss_list import RssList


class TestRssList:
    def test_rss_list(self):
        rss_list = RssList.get()
        assert type(rss_list) is list
        assert len(rss_list) is 4
        assert rss_list[2] == "some_site"
