import requests

class Wikipedia:
    """Class used for the media wiki API REST requests"""

    @staticmethod
    def get_request(sentence: str) -> str:
        url = "https://fr.wikipedia.org/w/api.php"
        parameters = {
            "action": "query",
            "list": "search",
            "format": "json",
            "utf8": True,
            "srsearch": sentence,
        }
        response = requests.get(url, parameters).json()
        if not response["query"]["searchinfo"]["totalhits"]:
            return ""
        page = response["query"]["search"][0]
        page_id = page["pageid"]
        parameters = {
            "action": "query",
            "format": "json",
            "prop": "extracts",
            "exintro": True,
            "explaintext": True,
            "redirects": 1,
            "exsentences": 2,
            "pageids": page_id,
        }
        response = requests.get(url, parameters).json()
        try:
            summary = response["query"]["pages"][str(page_id)]["extract"]
            return summary
        except KeyError:
            return ""
