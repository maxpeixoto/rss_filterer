from abc import ABC, abstractmethod


class LinkFilter(ABC):
    @abstractmethod
    def filter(self):
        return
