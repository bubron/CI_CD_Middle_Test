import re

def count_sentences(text: str) -> int:
    """Підраховує кількість речень у тексті"""
    sentence_endings = r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!|\.{3})\s'
    sentences = re.split(sentence_endings, text.strip())
    return len([s for s in sentences if s])

def count_words(text: str) -> int:
    """Підраховує кількість слів у тексті"""
    word_separators = r'[,\s:;]+'
    words = re.split(word_separators, text.strip())
    return len([w for w in words if w])