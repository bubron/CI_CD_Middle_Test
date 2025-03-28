import pytest
from text_analyzer import count_words, count_sentences, analyze_file

@pytest.fixture
def sample_text():
    return "Це перше речення. А це друге! А це третє, чи не так? Четверте... Ну і п'яте."

@pytest.fixture
def sample_text_with_commas():
    return "Слово, ще слово: третє; і останнє."