from abc import ABC, abstractmethod


class PageFilter(ABC):
    @abstractmethod
    def filter(self, page):
        return
