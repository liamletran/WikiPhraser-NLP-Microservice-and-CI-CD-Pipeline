from textblob import TextBlob
import wikipedia


def search_wikipedia(name):
    """Search Wikipedia for a given name and return search results."""
    print(f"Searching Wikipedia for: {name}")
    return wikipedia.search(name)


def summarize_wikipedia(name):
    """Summarize Wikipedia page for a given name."""
    print(f"Getting Wikipedia summary for: {name}")
    return wikipedia.summary(name)


def get_text_blob(text):
    """Create a TextBlob object from the given text."""
    blob = TextBlob(text)
    return blob


def get_phrases(name):
    """Get noun phrases from the Wikipedia summary of the given name."""
    text = summarize_wikipedia(name)
    blob = get_text_blob(text)
    phrases = blob.noun_phrases
    return phrases


# golden_state_warriors_text = wikipedia.summary("Golden State Warriors")
# blob.noun_phrases
# wikipedia.summary("Golden State Warriors")
