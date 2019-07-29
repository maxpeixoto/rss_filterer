from keyword_reader import KeywordReader


def test_keyword_reader():
    KeywordReader._file = "test_%s" % KeywordReader._file
    keywords = KeywordReader.read()
    assert type(keywords) is list
    assert len(keywords) is 18
    assert keywords[2] == 'Magazine Lu'
