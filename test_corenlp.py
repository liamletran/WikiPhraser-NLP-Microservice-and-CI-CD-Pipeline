from nlplogic.corenlp import get_phrases, search_wikipedia, summarize_wikipedia, get_text_blob

def test_get_phrases():
    phrases = get_phrases("Golden State Warriors")
    assert "golden state" in phrases
    # assert "state warriors" in phrases
    assert "warriors" in phrases