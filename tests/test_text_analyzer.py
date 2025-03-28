import pytest
from text_analyzer import count_words, count_sentences, analyze_file

@pytest.fixture
def sample_text():
    return "Це перше речення. А це друге! А це третє, чи не так? Четверте... Ну і п'яте."

@pytest.fixture
def sample_text_with_commas():
    return "Слово, ще слово: третє; і останнє."

@pytest.fixture
def temp_text_file(tmp_path, sample_text):
    file = tmp_path / "test_file.txt"
    file.write_text(sample_text)
    return str(file)

@pytest.mark.parametrize("text,expected", [
    ("Одне речення.", 1),
    ("Перше. Друге! Третє?", 3),
    ("Без речень", 0),
    ("Кілька... крапок... рахуються як одне.", 2),
])
def test_count_sentences(text, expected):
    assert count_sentences(text) == expected
