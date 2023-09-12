import os
import sys

BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    page: str = text[start: start + size + 1]
    symbols: tuple[str] = (', ', '. ', '! ', ': ', '; ', '? ', ',\n', '.\n',
                           '!\n', ':\n', ';\n', '?\n')
    if len(text[start:]) == len(page) or\
            page[-1] + text[start + size] in symbols:
        return page, len(page)
    while page[-2:] not in symbols:
        page = page[:-1]
    return page[:-1], len(page) - 1


# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:
    with open(path, 'r', encoding='utf-8') as file:
        text: str = file.read()
        page_number: int = 1
        start: int = 0
        while start < len(text):
            page: tuple[str, int] = _get_part_text(text, start, PAGE_SIZE)
            book[page_number] = page[0].lstrip()
            page_number += 1
            start += page[1] + 1


# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(os.path.join(sys.path[0], os.path.normpath(BOOK_PATH)))
