import os
from typing import TypeVarTuple

BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}

def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    stop_symbols: tuple = ('.', ',', '!', ':', ';', '?')

    if len(text) < start+size:
        size = len(text) - start
        if text[start+size-1] in stop_symbols:
            return (text[start:start+size], size)
    while size>0:
        if text[start+size-1] in stop_symbols and text[start+size] not in stop_symbols:
            return (text[start:start+size], size)
        else:
            size -= 1



def prepare_book(path: str) -> None:
    book_text = open(path, encoding='utf-8')
    text = book_text.read()
    start_page = 0
    pagenum: int = 1
    while start_page != len(text):
        book[pagenum], start = _get_part_text(text, start_page, PAGE_SIZE)
        book[pagenum] = book[pagenum].lstrip()
        start_page += start
        pagenum+=1
    return book



prepare_book(os.path.join(os.getcwd(), BOOK_PATH))
