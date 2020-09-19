from unidecode import unidecode
import json
import re
from config import recurring_words

class Parser:

    def parse_question(self, question: str) -> str:
        """
        This method calls the necessary methods to parse a string to the format we want for google maps
        :param question: The base string sent by the user
        :return:
        """
        question = self.remove_stopwords(question)  # remove the stopwords
        question = self.extract_question(question)  # remove some more recurring words
        return question

    def remove_stopwords(self, question: str) -> str:
        """
        This method removes the french stopwords and punctuation from a string
        :param question: The string to remove the stopwords from
        :return: The string without stopwords and punctuation
        """
        with open('static/json/stopwords.json', 'r') as file:
            stopwords = json.loads(file.read())
        question = question.lower()
        question_list = question.split(" ")
        # build a clean list without the stopwords
        question_list_clean = [word for word in question_list if word not in stopwords]
        question_without_stopwords = " ".join(question_list_clean)
        # remove d', l' and punctuation
        question_without_stopwords = re.sub(r"d'|l'|[^\w\s]", '', question_without_stopwords)
        return question_without_stopwords

    def extract_question(self, question: str) -> str:
        """
        This method is used to remove some more words from the sentence
        :param question: the question/sentence of the uesr
        :return: the extracted sentence
        """
        final_string = []
        bad_words = []
        regex = r"|".join(recurring_words) + "[a-zA-Z]"
        liste = re.findall(regex, question)
        for bad_word in liste:
            bad_words.append(bad_word)  # List of the words containing the bad words we found via re
        question = question.split(' ')
        for word in question:
            if word not in bad_words:
                final_string.append(word)
        extracted_question = unidecode(" ".join(final_string))
        return extracted_question
