from obj_data.exceptions import StorageCapacityError, ItemNotFoundError, StorageItemsQntError, RemoveQntError
from obj_data.storage import Storage


class Shop(Storage):
    def __init__(self, items=None, capacity=20):
        if items is None:
            items = {}
        self._items = items
        self._capacity = capacity
        self.items_limit = 5

    def __repr__(self):
        return f'{self.__class__.__name__}(items={self.items}, вместимость={self.capacity}, лимит={self.items_limit}'

    @property
    def items(self):
        return self._items

    @property
    def capacity(self):
        return self._capacity

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

    def add(self, title, qnt):
        # Проверяем на вместимость
        if self.capacity < self._get_total_items() + qnt:
            raise StorageCapacityError
        # Проверяем на количество уникальных товаров
        if self.get_unique_items_count() >= self.items_limit:
            raise StorageItemsQntError
        # Если все ок, то добавляем
        self.items[title] = self.items.get(title, 0) + qnt

    def remove(self, title, qnt):
        """
        Метод удаления товара со склада
        :param title: str - наименование удаляемого товара
        :param qnt: int - количество товара, которое нужно удалить
        :return: Обновляет значение словаря
        """
        # Проверяем на наличие товара на складе
        if not self._check_item(title):
            raise ItemNotFoundError
        else:
            # Проверяем, что количество товара на складе, не меньше, чем можно удалить
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

    def get_unique_items_count(self):
        """
        Метод получения количества уникальных товаров (ключей словаря)
        :return: int: значение уникальных ключей
        """
        return len(self.items.keys())