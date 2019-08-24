import json
import os
import time

import pytest

from rss_config_io import RssConfigIO
from rss_configuration import RssConfiguration


class TestRssConfiguration:
    rss = "http://g1.globo.com/dynamo/rss2.xml"
    timestamp = [2019, 8, 24, 2, 56, 52, 5, 236, 0]
    temp = "missing_file.json"
    base_content = json.dumps({rss: {RssConfiguration._timestamp_field: timestamp}})

    @pytest.fixture(autouse=True)
    def before_after_all(self):
        try:
            os.remove(self.temp)
        except:
            pass
        yield
        with open(RssConfigIO()._file, 'w') as f:
            f.write(self.base_content)

    def test_is_callable(self):
        assert RssConfiguration(self.rss) is not None

    def test_config_is_json(self):
        json_config = RssConfiguration(self.rss)._config
        assert (type(json_config) is dict)
        assert json.dumps(json_config) is not None

    def test_config_is_consistent(self):
        json_config = str(RssConfiguration(self.rss)._config)
        json_config2 = str(RssConfiguration(self.rss)._config)
        assert (json_config == json_config2)

    def test_update_on_destroy(self):
        config = RssConfiguration(self.rss)
        assert "x" not in config._future_config
        config._future_config["x"] = "y"
        del config

        new_config = RssConfiguration(self.rss)._config
        assert type(new_config) is dict
        assert new_config["x"] == "y"

    def test_default(self):
        sample = RssConfiguration('b')._get_default()
        assert 'timestamp' in sample

    def test_default_values(self):
        config = RssConfiguration('non_existing')._config
        assert config['timestamp'] is not None
        assert type(config['timestamp']) is list
        assert config['timestamp'] == list(time.gmtime(1))

    def test_get_timestamp(self):
        timestamp = RssConfiguration(self.rss).get_timestamp()
        assert timestamp is not None

    def test_set_timestamp(self):
        config = RssConfiguration(self.rss)
        timestamp = [2022, 8, 24, 2, 56, 52, 5, 236, 0]
        assert timestamp > config._future_config[config._timestamp_field]
        config.set_timestamp(timestamp)
        assert timestamp == config._future_config[config._timestamp_field]

    def test_set_timestamp_no_downgrade(self):
        config = RssConfiguration(self.rss)
        old_timestamp = config.get_timestamp()
        assert old_timestamp == self.timestamp
        new_timestamp = list(time.gmtime(200))
        assert old_timestamp > new_timestamp
        config.set_timestamp(new_timestamp)
        assert config.get_timestamp() == old_timestamp
