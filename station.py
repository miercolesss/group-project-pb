class Bike:
    def __init__(self, number, is_electric=False, battery=100):
        """Ініціалізація велосипеда: номер, тип, і заряд батареї (за замовчуванням 100)."""
        self.number = number
        self.is_electric = is_electric
        self.battery = battery  # Рівень заряду від 0 до 100

    def get_price_per_minute(self):
        """Повертає вартість хвилини: 5 грн для ел., 2 грн для звичайного."""
        return 5 if self.is_electric else 2


class Station:
    def __init__(self, name):
        """Ініціалізація станції: назва та порожній список велосипедів."""
        self.name = name
        self.bikes = []

    def add_bike(self, bike):
        """Додає велосипед на станцію."""
        self.bikes.append(bike)

    def rmv_bike(self):
        """
        Знімає велосипед зі станції.
        Нова вимога: електричний велосипед із зарядом < 20 не можна видавати, 
        якщо є інші придатні велосипеди.
        """
        if not self.bikes:
            return None

        # Шукаємо придатний велосипед (звичайний або з зарядом >= 20)
        for i, bike in enumerate(self.bikes):
            if not bike.is_electric or bike.battery >= 20:
                return self.bikes.pop(i)
        
        # Якщо всі велосипеди електричні і розряджені (< 20), повертаємо None (або перший розряджений за логікою)
        return None

    def get_bikes_count(self):
        """Повертає кількість велосипедів на станції."""
        return len(self.bikes)
