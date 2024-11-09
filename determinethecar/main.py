car_catalog = [
    {"Model": "Toyota Camry", "Release Date": "2023", "Installment": True,
     "Price": "25,000$", "Engine": "2.5L 4-cylinder", "Drive": "FWD",
     "Acceleration": "7.5 seconds", "Country": "Japan", "Year": 2023},
    {"Model": "BMW X5", "Release Date": "2022", "Installment": False,
     "Price": "60,000$", "Engine": "3.0L 6-cylinder", "Drive": "AWD",
     "Acceleration": "5.5 seconds", "Country": "Germany", "Year": 2022},
    {"Model": "Ford Mustang", "Release Date": "2021", "Installment": True,
     "Price": "30,000$", "Engine": "5.0L V8", "Drive": "RWD",
     "Acceleration": "4.5 seconds", "Country": "USA", "Year": 2021},
    {"Model": "Honda Civic", "Release Date": "2022", "Installment": True,
     "Price": "22,000$", "Engine": "1.5L 4-cylinder", "Drive": "FWD",
     "Acceleration": "8.0 seconds", "Country": "Japan", "Year": 2022},
    {"Model": "Audi A4", "Release Date": "2023", "Installment": False,
     "Price": "40,000$", "Engine": "2.0L 4-cylinder", "Drive": "FWD",
     "Acceleration": "6.5 seconds", "Country": "Germany", "Year": 2023},
    {"Model": "Mercedes-Benz C-Class", "Release Date": "2022",
     "Installment": True, "Price": "45,000$", "Engine": "2.0L 4-cylinder",
     "Drive": "RWD", "Acceleration": "6.0 seconds", "Country": "Germany",
     "Year": 2022},
    {"Model": "Nissan Altima", "Release Date": "2023", "Installment": True,
     "Price": "24,000$", "Engine": "2.5L 4-cylinder", "Drive": "FWD",
     "Acceleration": "7.0 seconds", "Country": "Japan", "Year": 2023},
    {"Model": "Hyundai Sonata", "Release Date": "2022",
     "Installment": False, "Price": "23,000$", "Engine": "2.5L 4-cylinder",
     "Drive": "FWD", "Acceleration": "7.8 seconds", "Country": "South Korea",
     "Year": 2022},
    {"Model": "Kia Optima", "Release Date": "2023", "Installment": True,
     "Price": "24,000$", "Engine": "1.6L Turbo", "Drive": "FWD",
     "Acceleration": "7.2 seconds", "Country": "South Korea", "Year": 2023},
    {"Model": "Mazda3", "Release Date": "2022", "Installment": True,
     "Price": "22,000$", "Engine": "2.5L 4-cylinder", "Drive": "FWD",
     "Acceleration": "7.3 seconds", "Country": "Japan", "Year": 2022}
    ]


def find_cars_by_criteria(catalog, criteria, parameter):
    """
    Функция поиска машин по заданному критерию.

    Args:
        catalog: Список словарей с информацией о машинах.
        criteria: Значение критерия для поиска.
        parameter: Ключ параметра для поиска.

    Returns:
        Список словарей с информацией о машинах, удовлетворяющих критерию.
    """
    matching_cars = []
    for car in catalog:
        if car[parameter] == criteria:
            matching_cars.append(car)
    return matching_cars


# критерий
release_year = input("Введите год выпуска: ")

# поиск по критерию
matching_cars = find_cars_by_criteria(car_catalog, release_year,
                                     "Release Date")

# результат поиска
if matching_cars:
    print("Найдены следующие машины:")
    for car in matching_cars:
        print(f" - {car['Model']}")
else:
    print("Машин, удовлетворяющих критерию, не найдено.")