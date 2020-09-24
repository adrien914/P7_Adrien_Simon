from utils.parser import Parser
import pytest


@pytest.fixture
def question():
    return "où se trouve l'arc de triomphe?"


def test_parse_question(question: str):
    """
    Test for the method parse_question
    """
    question = Parser().parse_question(question)
    assert question == 'arc triomphe'


def test_remove_stopwords(question: str):
    """
    Test for the method remove_stopwords
    """
    question = Parser().remove_stopwords(question)
    assert question == 'trouve arc triomphe'


def test_extract_question(question: str):
    """
    Test for the method extract_question
    """
    question = Parser().extract_question(question)
    assert question == "ou se l'arc de triomphe?"

