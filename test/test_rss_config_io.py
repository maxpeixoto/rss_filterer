import os
import random

import pytest

from rss_config_io import RssConfigIO


class TestRssConfigIO:
    temp = "missing_file.json"

    @pytest.fixture(autouse=True)
    def before_each(self):
        self.config = RssConfigIO()
        try:
            os.remove(self.temp)
        except:
            pass

    def test_read_new_file(self):
        self.config._file = self.temp
        data = self.config.read()
        assert type(data) is dict
        assert len(data) is 0

    def test_add_new_file(self):
        self.config._file = self.temp
        self.config.add({"b": 2})

        data = self.config.read()
        assert type(data) is dict
        assert len(data) is 1
        assert data["b"] == 2

    def test_write_new_file(self):
        self.config._file = self.temp
        self.config.add({"c": 3})

        data = self.config.read()
        assert type(data) is dict
        assert len(data) is 1
        assert data["c"] == 3

    def test_read(self):
        data = self.config.read()
        assert type(data) is dict

    def test_add(self):
        size = len(self.config.read())

        test_case = random.randint(1, 1000)
        self.config.add({"a": test_case})

        data = self.config.read()
        assert type(data) is dict
        assert data["a"] == test_case

    def test_write(self):
        test_case = random.randint(1, 1000)
        self.config.write({"d": test_case})

        data = self.config.read()
        assert type(data) is dict
        assert data["d"] == test_case

    def test_add_merging(self):
        self.config.write({"a": 1, 'b': 2})
        data = self.config.read()
        assert data['a'] == 1
        assert data['b'] == 2
        self.config.add({'b': 22, 'c': 3})
        data = self.config.read()
        assert data['c'] == 3
        assert data['b'] == 22
