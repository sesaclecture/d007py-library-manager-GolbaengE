
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Iterable
from library.models.book import Book

class BaseService(ABC):
    """서비스 공통 인터페이스.
    TODO: 아래 메서드를 하위 클래스에서 구현하도록 하세요.
    """

    @abstractmethod
    def add_book(self, book: Book) -> None:
        """
        책을 추가한다.
        Raises:
            ValueError: 동일한 title의 책이 이미 존재하는 경우
        """
        ...

    @abstractmethod
    def remove_book(self, title: str) -> None:
        """
        title 입력 시 해당 책을 제거한다.
        Raises:
            ValueError: 해당 책이 존재하지 않는 경우
        """
        ...

    @abstractmethod
    def list_books(self) -> Iterable[Book]:
        """
        책 목록을 반환한다.
        (list(self._books) 같은 복사본을 반환한다)
        """
        ...

    @abstractmethod
    def find_book(self, title: str) -> Book:
        """
        title 입력 시 해당 책을 찾아 반환한다.
        Raises:
            ValueError: 해당 책이 존재하지 않는 경우
        """    
        ...