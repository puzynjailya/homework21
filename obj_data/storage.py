# ** Методы: **
# `add`( < название >, < количество >)  - увеличивает запас items
# `remove`( < название >, < количество >) - уменьшает запас items
# `get_free_space()` - вернуть количество свободных мест
# `get_items()` - возвращает содержание склада в словаре {товар: количество}
# `get_unique_items_count()` - возвращает  количество уникальных товаров.

from abc import ABC, abstractmethod


class Storage(ABC):
    # Создаем абстрактное поле items
    @property
    @abstractmethod
    def items(self):
        pass

    # Создаем абстрактное поле capacity
    @property
    @abstractmethod
    def capacity(self):
        pass

    # Создаем абстрактный метод add
    @abstractmethod
    def add(self, title, qnt):
        pass

    # Создаем абстрактный метод remove
    @abstractmethod
    def remove(self, title, qnt):
        pass

    # Создаем абстрактный метод get_items
    @abstractmethod
    def get_items(self):
        pass

    # Создаем абстрактный метод get_free_space
    @abstractmethod
    def get_free_space(self):
        pass

    # Создаем абстрактный метод get_unique_items_count
    @abstractmethod
    def get_unique_items_count(self):
        pass


