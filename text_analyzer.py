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

def analyze_file(file_path: str) -> dict:
    """Аналізує файл та повертає статистику"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            return {
                'word_count': count_words(content),
                'sentence_count': count_sentences(content),
                'file_path': file_path
            }
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл {file_path} не знайдено")
    except Exception as e:
        raise Exception(f"Помилка при читанні файлу: {str(e)}")