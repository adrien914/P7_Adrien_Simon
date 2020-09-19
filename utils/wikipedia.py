import wikipedia


class Wikipedia:
    """Class used for the media wiki API REST requests"""

    @staticmethod
    def get_request(sentence: str) -> str:
        wikipedia.set_lang("fr")
        try:
            result = wikipedia.summary(sentence, sentences=2)
        except:
            result = None
        return result
