from abc import ABC

from obj_data.exceptions import ItemNotFoundError, StorageCapacityError, RemoveQntError, StorageItemsQntError
from obj_data.storage import Storage


class Store(Storage):
    def __init__(self, items=None, capacity=100):
        if items is None:
            items = {}
        self._items = items
        self._capacity = capacity

    def __repr__(self):
        return f'{self.__class__.__name__}(items={self.items}, вместимость={self.capacity}'

    @property
    def items(self):
        return self._items

    @property
    def capacity(self):
        return self._capacity

    # Создаем приватный метод получения суммы всего товара
    def _get_total_items(self):
        """
        Приватный метод получения общего количества товара на складе
        :return: значение суммы значений словаря items
        """
        return sum(self.items.values())

    # Создаем приватный метод проверки наличия товара на складе
    def _check_item(self, title):
        """
        Метод проверки наличия товара в словаре items
        :param title: str - Наименование товара
        :return: bool: если товар есть на складе - True, иначе False
        """
        return title in self.items

    # Создаем задекларированный метод add
    def add(self, title, qnt):
        # Проверяем на вместимость
        if self.capacity < self._get_total_items() + qnt:
            raise StorageCapacityError
            print(f'Ошибка! Склад заполнен на {self._get_total_items()} ед. товара. Лимит {self.capacity}')
        else:
            self.items[title] = self.items.get(title, 0) + qnt

    # Создаем задекларированный метод remove
    def remove(self, title, qnt):
        """
        Метод удаления товара со склада
        :param title: str - наименование удаляемого товара
        :param qnt: int - количество товара, которое нужно удалить
        :return: Обновляет значение словаря
        """
        if not self._check_item(title):
            raise ItemNotFoundError

        else:
            if qnt > self.items.get(title):
                raise RemoveQntError

            else:
                self.items[title] = self.items.get(title) - qnt

    def get_items(self):
        """
        Метод получение словаря (данных о складе)
        :return: словарь с текущими данными
        """
        return self.items

    def get_free_space(self):
        if self.capacity == self._get_total_items():
            print(f'Заполнение {self._get_total_items()} из {self.capacity}')
            return 0
        else:
            return self.capacity - self._get_total_items()

    # Создаем задекларированный метод get_unique_items_count
    def get_unique_items_count(self):
        """
        Метод получения количества уникальных товаров (ключей словаря)
        :return: int: значение уникальных ключей
        """
        return len(self.items.keys())

    # Создаем сеттер абстрактного поля items
    # @items.setter
    # def items(self, value):
    #     self._items = value
    #
    # # Создаем сеттер абстрактного поля capacitiy
    # @capacity.setter
    # def capacity(self, value):
    #     self._capacity = value
