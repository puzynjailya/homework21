class Request:

    def __init__(self, request_string: str):
        """
        При инициализации берем строку введенную пользователем и делим ее пробелами
        :param request_string: str - строка с данными о запросе доставки
        """
        separated_string = request_string.split(' ')

        # Задаем параметры в соответсвии с форматом строки:
        # Если строка вида: Доставить 3 собачки из склад в магазин
        if separated_string[0] == 'Доставить':
            self.away_from: str = separated_string[4]
            self.to_store: str = separated_string[6]
            self.amount: int = int(separated_string[1])
            self.product: str = separated_string[2]

        # Если строка вида: 'Курьер забирает 3 печеньки из склад'
        elif separated_string[0] == 'Курьер':
            self.away_from: str = separated_string[5]
            self.amount: int = int(separated_string[2])
            self.product: str = separated_string[3]

            # Так как не задано место куда везти, то задаем автоматически
            if separated_string[5] == 'склад':
                self.to_store = 'магазин'
            else:
                self.to_store = 'склад'

        else:
            self.away_from = None
            self.to_store = None
            self.amount = None
            self.product = None

    def __repr__(self):
        return f'from = {self.away_from}\nto = {self.to_store}\namount = {self.amount}\nproduct = {self.product}'
