class Bike:
    def __init__(self, number, is_electric=False):
        """Початкова ініціалізація велосипеда: номер і тип (звичайний чи електричний)."""
        self.number = number
        self.is_electric = is_electric

    def get_price_per_minute(self):
        """Повертає вартість хвилини: 5 грн для ел, 2 грн для звичайного."""
        if self.is_electric:
            return 5
        else:
            return 2

class Station:
    def __init__(self, name):
        """Початкова ініціалізація станції: назва та порожній список велосипедів."""
        self.name = name
        self.bikes = []

    def add_bike(self, bike):
        """Додає велосипед на станцію."""
        self.bikes.append(bike)

    def remove_bike(self):
        """Знімає велосипед зі станції (повертає об'єкт велосипеда або None, якщо їх немає)."""
        if len(self.bikes) > 0:
            return self.bikes.pop(0)
        return None

    def get_bikes_count(self):
        """Повертає кількість велосипедів на станції."""
        return len(self.bikes)
