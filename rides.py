
class Rides:
    def __init__(self):
        self.total_revenue = 0 #виручка
        
    def calculate_cost(self, bike, time):
        # рахує вартість поїздки
        return bike.get_price_per_minute() * time
            
    

    def trip_details(self, client, start_station, end_station, time):
        # клієнт бере велосипед на старт станції, катається тайм часу та повертає його на енд стаанцію
        if time <= 0:
            return False, "некоректний час"
        bike = start_station.remove_bike()
        if bike is None:
            return False, "немає вільних велосипедів"
        cost = self.calculate_cost(bike, time)
        if not client.pay(cost):
            start_station.add_bike(bike)
            return False, "недостатньо коштів"
        end_station.add_bike(bike)
        self.total_revenue += cost
        return True, cost
            

        
