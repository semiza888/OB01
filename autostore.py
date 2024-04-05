# Автомагазин

class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price, currency):
        self.items[item_name] = {"price": price, "currency": currency}
        print(f"Товар '{item_name}' добавлен в ассортимент")

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f"Товар '{item_name}' удален из ассортимента")
        else:
            print(f"Товара '{item_name}' нет в ассортименте")

    def get_item_price(self, item_name):
        if item_name in self.items:
            return self.items[item_name]["price"], self.items[item_name]["currency"]
        else:
            return None, None

    def update_item_price(self, item_name, new_price, new_currency):
        if item_name in self.items:
            self.items[item_name]["price"] = new_price
            self.items[item_name]["currency"] = new_currency
            print(f"Цена на товар '{item_name}' изменена")
        else:
            print(f"Товара '{item_name}' нет в ассортименте")

stores = [
    Store("Автосалон 'Mercedes'", "ул. Ленина, 10"),
    Store("Автосалон 'Haval'", "пр. Победы, 5")
]

while True:
    print("\nВыберите магазин:")
    for i, store in enumerate(stores):
        print(f"{i + 1}. {store.name}")
    print(f"{len(stores) + 1}. Добавить новый магазин")
    print(f"{len(stores) + 2}. Выйти")
    store_choice = input("Выберите магазин: ")

    if store_choice.isdigit():
        store_choice = int(store_choice)
        if 1 <= store_choice <= len(stores):
            current_store = stores[store_choice - 1]
            while True:
                print("\n1. Добавить товар")
                print("2. Удалить товар")
                print("3. Получить цену товара")
                print("4. Обновить цену товара")
                print("5. Вывести список товаров")
                print("6. Выбрать другой магазин")
                print("7. Выйти")
                choice = input("Выберите действие: ")

                if choice == "1":
                    item_name = input("Введите название товара: ")
                    price = float(input("Введите цену товара: "))
                    currency = input("Введите валюту: ")
                    current_store.add_item(item_name, price, currency)
                elif choice == "2":
                    item_name = input("Введите название товара: ")
                    current_store.remove_item(item_name)
                elif choice == "3":
                    item_name = input("Введите название товара: ")
                    item_price, item_currency = current_store.get_item_price(item_name)
                    if item_price is not None:
                        print(f"Цена товара '{item_name}': {item_price} {item_currency}")
                    else:
                        print(f"Товар '{item_name}' не найден")
                elif choice == "4":
                    item_name = input("Введите название товара: ")
                    new_price = float(input("Введите новую цену товара: "))
                    new_currency = input("Введите новую валюту: ")
                    current_store.update_item_price(item_name, new_price, new_currency)
                elif choice == "5":
                    print("Товары в наличии:")
                    for item_name, details in current_store.items.items():
                        print(f"{item_name} - Цена: {details['price']} {details['currency']}")
                elif choice == "6":
                    break
                elif choice == "7":
                    exit()
                else:
                    print("Некорректный выбор")
        elif store_choice == len(stores) + 1:
            name = input("Введите название нового магазина: ")
            address = input("Введите адрес нового магазина: ")
            stores.append(Store(name, address))
            print(f"Магазин '{name}' добавлен в список")
        elif store_choice == len(stores) + 2:
            exit()
        else:
            print("Некорректный выбор")
    else:
        print("Некорректный выбор")