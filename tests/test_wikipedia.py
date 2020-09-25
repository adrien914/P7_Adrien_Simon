from utils.wikipedia import Wikipedia
import requests


def test_wikipedia(monkeypatch):
    """
    Mock for google maps api calls
    """
    results = {
       "query": {
           "searchinfo": {
               "totalhits": 1
           },
           "search": [{
              "pageid": 16
           }],
          "pages": {
             "16": {
                "extract":"L\u2019arc de triomphe de l\u2019\u00c9toile, souvent appel\u00e9 simplement l\u2019Arc de triomphe, dont la construction, d\u00e9cid\u00e9e par l'empereur Napol\u00e9on Ier, d\u00e9buta en 1806 et s'acheva en 1836 sous Louis-Philippe, est situ\u00e9 \u00e0 Paris, dans les 8e, 16e, et 17e arrondissements."
             }
          }
       }
    }


    class MockResponse:
        def __init__(self, url, params):
            return

        def json(self):
            return results

    monkeypatch.setattr(requests, 'get', MockResponse)
    assert "L’arc de triomphe de l’Étoile" in Wikipedia().get_summary("Arc triomphe")

