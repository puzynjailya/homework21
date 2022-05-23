from obj_data import Shop, Store, Request, exceptions
from time import sleep


def delivery_club():

    print('********************')
    print('Добро пожаловать в сервис доставки товаров')
    print('********************')
    store = Store()
    shop = Shop()

    shop.add(title='ежики', qnt=3)
    shop.add(title='улитки', qnt=3)
    shop.add(title='котята', qnt=4)

    store.add(title='ежики', qnt=15)
    store.add(title='котята', qnt=20)
    store.add(title='улитки', qnt=15)
    store.add(title='щенки', qnt=20)
    store.add(title='утята', qnt=5)
    store.add(title='сороки', qnt=5)
    store.add(title='мармозетки', qnt=5)


    sleep(1)

    # Зададим флаг для остановки программы
    flag = False
    print('Введите ваш запрос. Пример: Доставить 3 собачки из склад в магазин')
    print('Программа остановится если вы введете слово "Флюгогенхаймен"')
    while not flag:
        user_request = input('Пользователь: ')

        # Если стоп слово, то тормозим программу
        if user_request == 'Флюгогенхаймен':
            print('Спасибо! С Вами было классно доставлять разные товары')
            flag = True
            break

        # Создаем объект request из запроса
        request = Request(user_request)

        # Если в запросе "из" = "склад" то проверяем наличие товара
        if request.away_from == 'склад':
            try:
                store.remove(title=request.product, qnt=request.amount)
                print('Программа: ')
                print('Нужное количество есть на складе')
                print(f'Курьер забрал {request.amount} {request.product} из {request.away_from}')
                print(f'Курьер везет {request.amount} {request.product} из {request.away_from} в {request.to_store}')
                shop.add(title=request.product, qnt=request.amount)
                print(f'Курьер доставил {request.amount} {request.product} в {request.to_store}')

            except exceptions.ItemNotFoundError as e:
                print(f'Товара {request.product} нет на складе')
                print(e)

            except exceptions.RemoveQntError as e:
                print(f'На складе недостаточно товара {request.product}. \
                Доступно только {store.get_items().get(request.product)}')
                print(e)

            except exceptions.StorageCapacityError as e:
                print('Превышена вместимость магазина')
                print(e)

            except exceptions.StorageItemsQntError as e:
                print('Превышена вместимость уникальных товаров')
                print(e)

            print(f'В {request.away_from} хранится:')
            for key, value in store.get_items().items():
                print(key, ' ', value)
            print(f'В {request.to_store} хранится:')
            for key, value in shop.get_items().items():
                print(key, ' ', value)
            print('-------')
        else:
            print('Тут лапки. Не успел дописать')
            print('Когда-нибудь здесь появится логика отправки магазин-склад')
            print('А пока =^_^= ')


if __name__ == '__main__':
    delivery_club()



