from keyword_reader import KeywordReader


def test_keyword_reader():
    keywords = KeywordReader.read()
    assert type(keywords) is list
    assert len(keywords) is 5
    assert keywords[2] == 'WEGE3'
