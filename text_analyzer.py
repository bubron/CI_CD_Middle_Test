import re

def count_sentences(text: str) -> int:
    """Підраховує кількість речень у тексті"""
    sentence_endings = r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!|\.{3})\s'
    sentences = re.split(sentence_endings, text.strip())
    return len([s for s in sentences if s])
