from decouple import config
import googlemaps


class GoogleMapsApi:

    api_key = config('API_KEY')  # Get the api key from the .env file

    def __init__(self):
        # initiate the connection with the google maps API
        self.client = googlemaps.Client(key=self.api_key)

    def geolocate(self, sentence: str) -> dict:
        """
        This method calls the gelocalization google api to find a place from a sentence
        :param sentence: the sentence to send to the api
        :return: the result of the request
        """
        sentence = sentence.split(" ")  # Make the sentence into a list
        result = self.client.geocode([sentence])  # Try to find the place
        if not result:
            result = self.client.geocode([sentence, "france"])  # Try to get a bigger specimen by adding france
        return result
