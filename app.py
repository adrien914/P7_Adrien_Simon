from flask import Flask, render_template, request, Response
from utils.google_maps_api import GoogleMapsApi
from utils.wikipedia import Wikipedia
from config import welcome_sentences
from utils.parser import Parser
from flask.json import jsonify
import random

app = Flask(__name__)
parser = Parser()
google_maps_api = GoogleMapsApi()


@app.route('/', methods=["GET"])
def index():
    # Choose a random welcome sentence from the config file
    welcome_sentence = welcome_sentences[random.randint(0, len(welcome_sentences) - 1)]
    return render_template('index.html', welcome_sentence=welcome_sentence, api_key=google_maps_api.api_key)


@app.route('/send_question', methods=["POST"])
def send_question() -> Response:
    """
    This method receives a question from a POST request, parses the text, sends it to the gmaps api and sends back
    a json response containing the message to be sent to the user and the location that need to be shown on the map
    :return: the response to the user and the location that the map needs to show
    """
    # Parse the question
    parsed_question = parser.parse_question(request.json['question'])
    # Try to locate the place asked by the user using the parsed question
    location = google_maps_api.geolocate(parsed_question)
    # Try to get the wikipedia summary
    wikipedia_summary = Wikipedia().get_request(parsed_question)
    try:
        text = location[0]["formatted_address"]  # The full address
        geometry_location = location[0]["geometry"]["location"]  # the gps coordinates

    except Exception:
        text = "Désolé, je n'ai pas compris la question"
        geometry_location = ""
    return jsonify(text=text, map_location=geometry_location, wikipedia_summary=wikipedia_summary)


if __name__ == '__main__':
    app.run(host="localhost", port=6080, debug=True)
