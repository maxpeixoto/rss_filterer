import pytest

from filter_keyword import FilterKeyword


class TestFilterKeyword:

    @pytest.fixture(autouse=True)
    def before_all(self):
        self.filter = FilterKeyword()

    def test_init(self):
        assert type(self.filter._keywords) is list

    def test_get_page_content(self):
        page = self.filter._get_page_content("http://www.google.com")
        assert type(page) is str
        assert len(page) is not 0

    def test_has_keyword(self):
        assert self.filter._has_keyword("http://www.google.com")
