class Bike:
    def __init__(self, number, is_electric=False):
        """Початкова ініціалізація велосипеда: номер і тип (звичайний чи електричний)."""
        pass

    def get_price_per_minute(self):
        """Повертає вартість хвилини: 5 грн для ел, 2 грн для звичайного."""
        pass


class Station:
    def __init__(self, name):
        """Початкова ініціалізація станції: назва та порожній список велосипедів."""
        pass

    def add_bike(self, bike):
        """Додає велосипед на станцію."""
        pass

    def rmv_bike(self):
        """Знімає велосипед зі станції (повертає об'єкт велосипеда або None, якщо їх немає)."""
        pass

    def get_bikes_count(self):
        """Повертає кількість велосипедів на станції."""
        pass
