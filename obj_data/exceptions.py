class StorageCapacityError(Exception):
    """
    Исключение при переполнении склада
    """
    pass


class ItemNotFoundError(Exception):
    """
    Исключение при отсутствии товара на складе
    """
    pass


class StorageItemsQntError(Exception):
    """
    Исключение при наличии уникальных товаров большего количества, чем задано
    """
    pass


class RemoveQntError(Exception):
    """
    Исключение при попытке удалить товаров больше, чем их на складе
    """
    pass