
from __future__ import annotations
from typing import Iterable, List
from library.models.book import Book
from library.services.base_service import BaseService


class LibraryService(BaseService):
    """도서 목록을 메모리에서 관리하는 서비스.
    TODO:
      - 내부 상태를 캡슐화하기 위해 _books(list[Book])를 사용
      - add_book/remove_book/list_books/find_book 구현
      - 존재하지 않는 책 삭제/검색 시 ValueError 발생
    """

    def __init__(self) -> None:
        self._books: List[Book] = []
        # TODO: 내부 리스트 초기화

    def add_book(self, book: Book) -> None:
        if any(b.title == book.title for b in self._books):
            raise ValueError(f"Book with title '{book.title}' already exists.")
        self._books.append(book)
        # TODO: 책 추가

    def remove_book(self, title: str) -> None:
        for i, b in enumerate(self._books):
            if b.title == title:
                del self._books[i]
                return
        raise ValueError(f"No book with title '{title}' found.")
        # TODO: 제목으로 책 삭제 (없으면 ValueError)

    def list_books(self) -> Iterable[Book]:
        return list(self._books)
        # TODO: 책 목록 반환 (복사본 반환 권장)

    def find_book(self, title: str) -> Book:
        for b in self._books:
            if b.title == title:
                return b
        raise ValueError(f"No book with title '{title}' found.")
        # TODO: 제목으로 책 찾기 (없으면 ValueError)
